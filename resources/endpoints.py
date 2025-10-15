from utilities.configurations import *

class V3ApiEndpoints:
    url = base_url
    api_key = api_key
    locations = "/locations"
    sensors = "/sensors"
    parameters = "/parameters"
    countries = "/countries"

def get_locations_payload(coordinates, radius, limit=5, page=1):
    payload = {
        "coordinates": coordinates,
        "radius": radius,
        "limit": limit,
        "page": page
    }
    return payload

