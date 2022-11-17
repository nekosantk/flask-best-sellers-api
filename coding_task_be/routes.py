from flask import current_app as app
from . import db

@app.route("/api/v1/sellers/top", methods=["GET"])
def top_sellers():
    db.fetch_top_sellers()
    return "Fetching top sellers of all time"


@app.route("/api/v1/sellers/<year>/top", methods=["GET"])
def top_sellers_by_year(year):
    db.fetch_top_sellers_by_year()
    return f"Fetching top sellers for {year}"
