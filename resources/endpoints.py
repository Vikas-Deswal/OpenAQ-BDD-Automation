from utilities.configurations import *

class V3ApiEndpoints:
    url = base_url
    api_key = api_key
    locations = "/locations"
    sensors = "/sensors"

def get_locations_payload(coordinates, radius):
    payload = {
        "coordinates": coordinates,
        "radius": radius,
        "limit": 5,
        "page": 1
    }
    return payload



