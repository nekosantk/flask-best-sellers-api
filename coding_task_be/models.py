from sqlalchemy import Numeric
from . import db


class vw_top_sellers(db.Model):
    sales_rep = db.Column(db.String(100))
    total_sales = db.Column(Numeric(10, 2))
    year = db.Column(db.Integer, primary_key=True)

    def __init__(self, sales_rep, total_sales, year):
        self.sales_rep = sales_rep
        self.total_sales = total_sales
        self.year = year

    def __repr__(self):
        return f'<vw_top_sellers {self.sales_rep} {self.total_sales} {self.year}>'
