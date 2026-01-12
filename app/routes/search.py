from flask import Blueprint, render_template, request
from ..models import WorkerProfile

search = Blueprint("search", __name__)

@search.route("/search")
def search_workers():
    city = request.args.get("city")
    service = request.args.get("service")

    query = WorkerProfile.query
    if city:
        query = query.filter_by(city=city)
    if service:
        query = query.filter_by(service=service)

    workers = query.all()
    return render_template("search.html", workers=workers)
