import requests
import os
import json
from flask import Flask, render_template, request, redirect
from ast import literal_eval

app = Flask(__name__)

# specifying proposal directory (easier to specify here than repeating same string across programme)
proposalsDir = "acceptedProposals/"

@app.route("/login", methods=["GET", "POST"])
def login():

    global RESEARCHER_NAME

    # if user wants to login to their DCU account to view their approved projects, display them in table
    if request.method == "POST":
        RESEARCHER_NAME = request.form["name"]
        return redirect(f"http://localhost:5002/dcu", code=302)

    # else just display the login page
    else:
        return render_template("login.html")

@app.route('/dcu', methods=["GET", "POST", "PUT"])
def dcuHome():

    global projects

    # if user login approved, display projects associated with that user
    if request.method == "GET":
        try:
            f = open(f"acceptedProposals/{RESEARCHER_NAME}.txt")
            projects = json.load(f)
        except:
            return render_template("dcuHome.html")
        return render_template("dcuHome.html", json_object=projects)

    # else if user wants to withdraw funds from project, or add/remove members to project
    elif request.method == "POST":

        # if user wants to withdraw, withdraw specified amount and update corresponding text file and update the table
        if "withdraw" in request.form.keys():

            f = open(f"acceptedProposals/{request.form['name']}.txt")
            ongoing_projects = json.load(f)
            f.close()
            # find the selected project to withdraw funds from
            for p in ongoing_projects:
                if p["title"] == request.form["project"]:
                    p["funding"] = int(p["funding"]) - int(request.form["amount"])
                    break
            # then overwrite the text file with the updated fund amount (since user withdrew some funds)
            f = open(f"acceptedProposals/{request.form['name']}.txt", "w")
            json.dump(ongoing_projects, f)
            f.close()

        # else if user wants to add/remove member from a project
        elif "addRemoveMember" in request.form.keys():
            f = open(f"acceptedProposals/{request.form['name']}.txt")
            ongoing_projects = json.load(f)
            f.close()
            for p in ongoing_projects:

                if p["title"] == request.form["project"]:
                    # if researcher wants to add member to project
                    if "Add" in request.form.values():
                        p["other_researchers"].append(request.form["member"])
                        newMemberFile(request.form["member"])
                        # passing new member, all projects, and the project they're assigned to
                        newMemberProject(request.form["member"], ongoing_projects, p)

                    # else if researcher wants to remove member from project
                    elif "Remove" in request.form.values():
                        try:
                            p["other_researchers"].remove(request.form["member"])
                            os.remove(f"{proposalsDir}{request.form['member']}.txt")
                        except:
                            return render_template("dcuHome.html")
                    break

            f = open(f"acceptedProposals/{request.form['name']}.txt", "w")
            json.dump(ongoing_projects, f)
            f.close()

        return render_template("dcuHome.html", json_object=ongoing_projects)

# creating new file when researcher's proposal is approved
@app.route('/newFile', methods=["GET", "POST"])
def new_file():
    name = request.data.decode("utf-8")
    if request.method == "POST":
        if os.path.exists("{}{}.txt".format(proposalsDir, name)):
            return name
        else:
            f = open("{}{}.txt".format(proposalsDir, name), "x")
            json.dump([], f)
            f.close()
    return name

# helper function for creating file for new member of project
def newMemberFile(newMember):
    if os.path.exists("{}{}.txt".format(proposalsDir, newMember)):
        return newMember
    else:
        f = open("{}{}.txt".format(proposalsDir, newMember), "x")
        json.dump([], f)
        f.close()
    return

# adding proposal contents to researcher file when approved
@app.route('/addProject', methods=["GET", "POST"])
def add_project():
    project = request.get_json()
    project["other_researchers"] = []
    file_name = project["name"]
    with open("{}{}.txt".format(proposalsDir, file_name)) as f:
        projects = json.load(f)
    with open("{}{}.txt".format(proposalsDir, file_name), "w") as f:
        projects.append(project)
        json.dump(projects, f)
    return project

# helper function for adding project info for new member of project
def newMemberProject(newMember, project, assignedProject):
    with open("{}{}.txt".format(proposalsDir, newMember)) as f:
        projects = json.load(f)
    with open("{}{}.txt".format(proposalsDir, newMember), "w") as f:
        projects.append(assignedProject)
        json.dump(projects, f)

    return project

if __name__ == "__main__":
    app.run(port=5002)
