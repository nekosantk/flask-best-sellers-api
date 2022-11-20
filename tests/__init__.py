import json
import os


def get_test_data(filename: str):
    full_path = os.path.join(os.path.dirname(__file__), 'test_data/') + filename
    with open(full_path) as file:
        return json.load(file)
