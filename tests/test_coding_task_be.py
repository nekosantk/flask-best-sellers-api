from coding_task_be import create_app
from coding_task_be.models import vw_top_sellers
from tests import get_test_data
import pytest


@pytest.mark.xfail
@pytest.mark.parametrize("test_data", ["ASD", "DFG", "GFG", "HGF", "AAD"])
def test_best_sellers_endpoint_by_year_string_input(test_data):
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get(f'/api/v1/sellers/{test_data}/top')
        assert response.status_code == 200


@pytest.mark.parametrize("test_data", [1990, 1991, 1992, 1993, 1994])
def test_best_sellers_endpoint_by_year_no_data(test_data):
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get(f'/api/v1/sellers/{test_data}/top')
        assert response.status_code == 400
        assert response.json.get("code") == 400
        assert response.json.get("name") == "Bad Request"
        assert response.json.get("description") == "No data for year"


@pytest.mark.parametrize("test_data", get_test_data("api_v1_sellers_top.json"))
def test_best_sellers_endpoint_by_year(test_data):

    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get(f'/api/v1/sellers/{test_data.get("Year")}/top')
        assert response.status_code == 200
        assert response.json.get("Sales Rep") == test_data.get("Sales Rep")
        assert response.json.get("Total Sales") == test_data.get("Total Sales")
        assert response.json.get("Year") == test_data.get("Year")


def test_best_sellers_endpoint():

    # Don't want to parameterize here, we need the entire json array
    test_data = get_test_data("api_v1_sellers_top.json")

    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get(f'/api/v1/sellers/top')
        assert response.status_code == 200
        assert response.json == test_data


def test_vw_top_sellers_model():

    sales_rep = "Mark Louw"
    total_sales = 205.40
    year = 2020

    top_seller_model = vw_top_sellers(sales_rep, total_sales, year)

    assert top_seller_model.sales_rep == sales_rep
    assert top_seller_model.total_sales == total_sales
    assert top_seller_model.year == year

