import requests
from os.path import exists
import json
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# specifying funding agency URL for sending the proposal to it
FUNDING_AGENCY = "http://127.0.0.1:5001"

@app.route('/', methods=["GET", "POST"])
def login():

    global RESEARCHER_NAME

    # if user wants to submit proposal, obtain their name and allow user to create proposal
    if request.method == "POST":
        RESEARCHER_NAME = request.form["name"]
        # new_file(RESEARCHER_NAME)
        return redirect(f"http://localhost:5000/researcher", code=302)

    # else, just load the login page
    else:
        return render_template("login.html")

@app.route("/researcher", methods=["GET", "POST"])
def researcher():
    proposal = ""
    # if user submits proposal, send it to funding agency where it is accepted/rejected
    if request.method == "POST":
        project = request.form.copy()
        project["name"] = RESEARCHER_NAME
        proposal = requests.post(FUNDING_AGENCY, json=project)
        proposal = proposal.text

    # pass researcher name and proposal message to inform researcher if their proposal got accepted/rejected
    return render_template("researcher_page.html", researcher=RESEARCHER_NAME, proposal=proposal)

if __name__ == "__main__":
    app.run()
