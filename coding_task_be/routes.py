from flask import current_app as app
from . import db
from decimal import *
from werkzeug.exceptions import HTTPException
import json
from flask import abort
from .models import vw_top_sellers


@app.get("/api/v1/sellers/top")
def top_sellers():

    # Fetch raw rows from database
    rows = vw_top_sellers.query.all()

    # Invalid year check
    if len(rows) == 0:
        abort(400, description="No data for year")

    results = []

    # Format rows into json
    for row in rows:
        results.append({
            "Sales Rep": row.sales_rep,
            "Total Sales": row.total_sales,
            "Year": row.year
        })

    return results


@app.get("/api/v1/sellers/<year>/top")
def top_sellers_by_year(year):

    # Fetch raw rows from database
    row = vw_top_sellers.query.filter_by(year=year).first()

    # Invalid year check
    if row is None:
        abort(400, description="No data for year")

    return {
            "Sales Rep": row.sales_rep,
            "Total Sales": row.total_sales,
            "Year": row.year
        }


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
