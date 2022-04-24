import requests
from flask import Flask, request

app = Flask(__name__)

# specifying DCU URL which will receive the accepted proposals to be displayed in the DCU page
DCU = "http://127.0.0.1:5002"

# update/refresh budget in text file
def update_budget(new_balance):
    f = open("total_budget.txt", "w")
    f.write(new_balance)
    f.close()

# helper function for getting current funding budget
def get_budget():
    f = open("total_budget.txt", "r")
    budget = f.readline()
    f.close()
    print(budget)
    return int(budget)

# determine if proposal is accepted/rejected
@app.route("/", methods=["GET", "POST"])
def consider_proposal():

    # if user sent in a proposal
    if request.method == "POST":
        # obtain proposal details
        project = request.get_json()
        total_budget = get_budget()
        amt_requested = int(project["funding"])

        # if researcher's requested amount is within the 200k-500k range and the total budget will not be exceeded, accept proposal
        if 200000 <= amt_requested <= 500000 and amt_requested < total_budget:
            total_budget -= int(amt_requested)
            update_budget(str(total_budget))

            # since DCU handles the text files per account, call the flask routes via the DCU URL
            # researcher name = file name, proposal/project specs added to it
            newFile = requests.post("{}/newFile".format(DCU), data=project["name"])
            proposal = requests.post("{}/addProject".format(DCU), json=project)
            
            return f"Your proposal to research {project['title']} has been accepted"

        # else reject proposal
        else:
            return f"Your proposal to research {project['title']} has been rejected"

if __name__ == "__main__":
    app.run(port=5001)
    # resets the budget if program killed
    update_budget("2000000")
