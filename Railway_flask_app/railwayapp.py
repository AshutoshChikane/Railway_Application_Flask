from flask import Flask, redirect, render_template, request, url_for
from datetime import datetime

app = Flask(__name__)


def check(curt, des, r):
    if r == 1:
        t1 = ["PANVEL", "NERUL", "VASHI", "VADALA", "CSMT"]
        if curt in t1:
            if des in t1:
                return True
    elif r == 2:
        t1 = ["THANE", "MULUND", "KURLA", "VADALA", "CSMT"]
        if curt in t1:
            if des in t1:
                return True
    else:
        return False


def costing(cls, curt, des, r):
    if r == 1:
        t1 = ["PANVEL", "NERUL", "VASHI", "VADALA", "CSMT"]
        c1 = t1.index(curt)
        c2 = t1.index(des)
        total = (c2-c1)*5
        total = abs(total)
        if cls == 1:
            return total*5
        else:
            return total
    elif r == 2:
        t1 = ["THANE", "MULUND", "KURLA", "VADALA", "CSMT"]
        c1 = t1.index(curt)
        c2 = t1.index(des)
        total = (c2-c1)*5
        total = abs(total)
        if cls == 1:
            return total*5
        else:
            return total


@app.route("/", methods=["GET", "POST"])
def welcome():
    if request.method == "POST":
        return redirect("/routes")
    return render_template("welcome.html")


@app.route("/routes", methods=["GET", "POST"])
def routtes():
    if request.method == "POST":
        if request.form["action"] == "CSMT-PANVEL":
            return redirect("/CSMT-PANVEL")
        elif request.form["action"] == "CSMT-THANE":
            return redirect("/CSMT-THANE")
        elif request.form["action"] == "HOME":
            return redirect("/")
    return render_template("route.html")


stops_panvel = "PANVEL <=> NERUL <=> VASHI <=> VADALA <=> CSMT"


@app.route("/CSMT-PANVEL", methods=["GET", "POST"])
def csmt_panvel(l=stops_panvel):
    if request.method == "POST":
        name = request.form["username"]
        current = (request.form["from"]).upper()
        destini = (request.form["dest"]).upper()
        a = check(current, destini, r=1)
        if a:
            if request.form["action"] == "I CLASS":
                cost1 = costing(1, current, destini, 1)
                return render_template("ticket.html", cost=cost1, name1=name, cur=current, des=destini, date=datetime.today(), cls="I", route="CSMT-PANVEL")

            elif request.form["action"] == "II CLASS":
                cost1 = costing(2, current, destini, 1)
                return render_template("ticket.html", cost=cost1, name1=name, cur=current, des=destini, date=datetime.today(), cls="II", route="CSMT-PANVEL")
        elif request.form["action"] == "HOME":
            return redirect("/")
    return render_template("details.html", lis=l)


stops_thane = "THANE <=> MULUND <=> KURLA <=> VADALA <=> CSMT"


@app.route("/CSMT-THANE", methods=["GET", "POST"])
def csmt_thane(l=stops_thane):
    if request.method == "POST":
        name = request.form["username"]
        current = (request.form["from"]).upper()
        destini = (request.form["dest"]).upper()
        a = check(current, destini, r=2)
        if a:
            if request.form["action"] == "I CLASS":
                cost1 = costing(1, current, destini, 2)
                return render_template("ticket.html", cost=cost1, name1=name, cur=current, des=destini, date=datetime.today(), cls="I", route="CSMT-THANE")
            elif request.form["action"] == "II CLASS":
                cost1 = costing(2, current, destini, 2)
                return render_template("ticket.html", cost=cost1, name1=name, cur=current, des=destini, date=datetime.today(), cls="II", route="CSMT-THANE")
        elif request.form["action"] == "HOME":
            return redirect("/")
    return render_template("details.html", lis=l)


if __name__ == "__main__":
    app.run(debug=True)
