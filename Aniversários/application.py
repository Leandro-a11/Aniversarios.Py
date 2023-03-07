import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configurar a Aplicação
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configurar a Lib Cs50 com o Sqlite
db = SQL("sqlite:///birthdays.db")

#Formulário inicial
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

#Rota para Deletar um cadastro
@app.route("/delete/<id>")
def Delete(id):
    rows = db.execute("SELECT id, name, day, month FROM birthdays WHERE id = ?", id)
    return render_template("delete.html", rows=rows)

#Rota para Alterar um cadastro
@app.route("/update/<id>")
def Update(id):
    rows = db.execute("SELECT id, name, day, month FROM birthdays WHERE id = ?", id)
    return render_template("update.html", rows=rows)

#Rota para fazer o Delete e o Update de acordo com o metodo recebido
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