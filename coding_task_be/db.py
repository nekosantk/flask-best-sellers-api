import sqlite3
from flask import g, current_app


def fetch_top_sellers():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM Genre")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def fetch_top_sellers_by_year():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM Genre")
    rows = cur.fetchall()
    for row in rows:
        print(row)


# Make sure we close the connection when the request ends
def init_app(app):
    app.teardown_appcontext(close_db)


# Get fresh connection for every request
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
