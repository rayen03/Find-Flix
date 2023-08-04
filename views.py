from flask import Blueprint, render_template, redirect, url_for, request, json
from search import search

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/result", methods=["POST", "GET"])
def handle_query():
    if request.method == "POST":
        squery = request.form["query"]
        return redirect(url_for("views.result", query=squery))
    else:
        return render_template("result.html")
    
@views.route("/result_for+<query>")
def result(query):
    results = json.dumps(search(query))
    return render_template("result.html", text=results, searchquery = query)