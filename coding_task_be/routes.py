from flask import current_app as app
from . import db
from decimal import *


@app.route("/api/v1/sellers/top", methods=["GET"])
def top_sellers():
    db.fetch_top_sellers()
    return "Fetching top sellers of all time"


@app.route("/api/v1/sellers/<year>/top", methods=["GET"])
def top_sellers_by_year(year: int):

    # Fetch raw rows from database
    rows = db.fetch_top_sellers_by_year(year)

    # Invalid year check
    if len(rows) == 0:
        return "No data for year", 400

    results = []

    # Format rows into json
    for row in rows:
        results.append({
            "Sales Rep": row[0],
            "Total Sales": round(Decimal(row[1]), 2)
        })

    return results
