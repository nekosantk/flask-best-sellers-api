import sqlite3
from flask import g, current_app


def fetch_top_sellers_by_year(year: int):
    cursor = get_db().cursor()

    cursor.execute("SELECT Employee.FirstName || ' ' || Employee.LastName, SUM(Invoice.Total)"
                   "FROM Invoice INNER JOIN Customer "
                   "ON Customer.CustomerId = Invoice.CustomerId "
                   "INNER JOIN Employee "
                   "ON Employee.EmployeeId = Customer.SupportRepId "
                   "WHERE strftime('%Y', InvoiceDate) = ? "
                   "GROUP BY Employee.EmployeeId "
                   "ORDER BY SUM(Invoice.Total) DESC", (year,))

    rows = cursor.fetchall()
    return rows


def fetch_top_sellers():
    sql_statement = "SELECT * FROM Genre"
    return []


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
