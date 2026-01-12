from flask import Blueprint, render_template, request, redirect
from ..models import WorkerProfile
from ..extensions import db

worker = Blueprint("worker", __name__)

@worker.route("/worker/register", methods=["GET", "POST"])
def worker_register():
    if request.method == "POST":
        profile = WorkerProfile(
            user_id=1,
            service=request.form["service"],
            city=request.form["city"],
            areas=request.form["areas"],
            experience=request.form["experience"],
            phone=request.form["phone"]
        )
        db.session.add(profile)
        db.session.commit()
        return redirect("/search")
    return render_template("worker_register.html")
