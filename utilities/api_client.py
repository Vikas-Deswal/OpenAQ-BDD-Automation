import requests
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

# -- Service Layer --
def get_endpoint_response(endpoint, params=None):
    client = ApiClient()
    return client.get(endpoint, params=params)