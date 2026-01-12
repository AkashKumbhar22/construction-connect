from flask import Blueprint, render_template, request, redirect

auth = Blueprint("auth", __name__)

@auth.route("/")
def home():
    return render_template("index.html")

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect("/login")
    return render_template("register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect("/search")
    return render_template("login.html")
