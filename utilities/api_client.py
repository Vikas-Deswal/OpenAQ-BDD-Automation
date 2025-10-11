import requests
from utilities.configurations import *

class ApiClient:
    def __init__(self):
        self.base_url = base_url
        self.headers = {"x-api-key": api_key}

    def get(self, endpoint, params=None):
        url = self.base_url + endpoint
        return requests.get(url, headers=self.headers, params=params)