import sqlite3
from flask import g, current_app


# Grab top seller by a specific year
def fetch_top_sellers_by_year(year: int):

    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM vw_top_sellers WHERE DateYear = ?", (year,))

    rows = cursor.fetchall()
    return rows


# Grab top sellers and order by year
def fetch_top_sellers():
    cursor = get_db().cursor()
    cursor.execute("SELECT * from vw_top_sellers ORDER BY DateYear DESC")
    rows = cursor.fetchall()
    return rows


# Initialize DB
def init_app(app):

    # Close the connection on request end
    app.teardown_appcontext(close_db)


# Get connection for new request
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )

    return g.db


# Close database connection
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
