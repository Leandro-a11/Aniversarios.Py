import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    Name = request.form.get("name")
    Day = request.form.get("day")
    Month = request.form.get("month")
    if request.method == "POST":
        db.execute("INSERT INTO birthdays(name, day, month) VALUES(?, ?, ?)", Name, Day, Month)
        return redirect("/")
    else:
        rows = db.execute("SELECT id, name, day, month FROM birthdays")
        return render_template("index.html" , rows=rows , lenth=len(rows))

@app.route("/delete/<id>")
def Delete(id):
    rows = db.execute("SELECT id, name, day, month FROM birthdays WHERE id = ?", id)
    return render_template("delete.html", rows=rows)

@app.route("/update/<id>")
def Update(id):
    rows = db.execute("SELECT id, name, day, month FROM birthdays WHERE id = ?", id)
    return render_template("update.html", rows=rows)

@app.route("/success/<id>", methods=["POST", "GET"])
def Success(id):
    Name = request.form.get("name")
    Day = request.form.get("day")
    Month = request.form.get("month")
    if request.method == "POST":
        db.execute("UPDATE birthdays SET name = ? , day = ? , month = ? WHERE id = ? ", Name, Day, Month, id)
    if request.method == "GET":
        db.execute("DELETE FROM birthdays WHERE id = ?", id)

    return redirect("/")