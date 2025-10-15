import requests
import json
from utilities.configurations import *

"""
This module combines both the HTTP client and service layer for simplicity.
In an enterprise setup, these would be separated for scalability, but here it's
kept in one place for easier demonstration.
"""

class ApiClient:
    def __init__(self):
        self.base_url = base_url
        self.headers = {"x-api-key": api_key}

    def get(self, endpoint, params=None):
        url = self.base_url + endpoint
        return requests.get(url, headers=self.headers, params=params)

# -- Base Service Layer (Can be separate file but keeping here for simple structure) --
def get_endpoint_response(endpoint, params=None):
    client = ApiClient()
    return client.get(endpoint, params=params)

def safe_json(response):
    try:
        return response.json()
    except json.JSONDecodeError:
        raise AssertionError("Response is not valid JSON")

def get_results(response):
    response_json = safe_json(response)
    if "results" not in response_json:
        raise AssertionError("Response JSON does not contain 'results' key")
    return response_json["results"]