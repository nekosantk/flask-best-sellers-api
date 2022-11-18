from flask import current_app as app
from . import db
from decimal import *
from werkzeug.exceptions import HTTPException
import json
from flask import abort


@app.get("/api/v1/sellers/top")
def top_sellers():

    # Fetch raw rows from database
    rows = db.fetch_top_sellers()

    # Invalid year check
    if len(rows) == 0:
        abort(400, description="No data for year")

    results = []

    # Format rows into json
    for row in rows:
        print(row)
        results.append({
            "Sales Rep": row[0],
            "Total Sales": round(Decimal(row[1]), 2),
            "Year": int(row[2])
        })

    return results


@app.get("/api/v1/sellers/<year>/top")
def top_sellers_by_year(year):

    # Fetch raw rows from database
    rows = db.fetch_top_sellers_by_year(year)

    # Invalid year check
    if len(rows) == 0:
        abort(400, description="No data for year")

    results = []

    # Format rows into json
    for row in rows:
        results.append({
            "Sales Rep": row[0],
            "Total Sales": round(Decimal(row[1]), 2)
        })

    return results


# Return JSON errors instead of HTML
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response, e.code
