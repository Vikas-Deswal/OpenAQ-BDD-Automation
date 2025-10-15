from utilities.api_client import *
from resources.endpoints import *

# Hitting Location Endpoint & needs coordinates & radius in KM
def get_location_data(coordinates, radius):
    params = get_locations_payload(coordinates, radius)
    return get_endpoint_response(V3ApiEndpoints.locations, params=params)

# Hitting Sensors Endpoint & need sensor ID to get measurement value
def get_sensors_data(sensor_id):
    return get_endpoint_response(f"{V3ApiEndpoints.sensors}/{sensor_id}")

# Function to process the location API response & matching the pollutant
def get_sensors_id(location_api_response, pollutant):
    loc_data = get_results(location_api_response)
    sensors_id = []
    for location in loc_data:
        for sensor in location['sensors']:
            if sensor['parameter']['displayName'] == pollutant:
                sensors_id.append(sensor['id'])
    return sensors_id

# Function to get the latest measurement for the provided sensors
def get_latest_measurements(location_api_response, pollutant):
    all_measurements = []
    all_sensors_id = get_sensors_id(location_api_response, pollutant)
    for sensor_id in all_sensors_id:
        measurements_response = get_endpoint_response(f"/sensors/{sensor_id}")
        response_sensors = get_results(measurements_response)
        for measurement in response_sensors:
            if measurement["latest"] is not None:
                all_measurements.append({
                    "sensor_id": sensor_id,
                    "value": measurement["latest"]["value"],
                    "datetime": measurement["latest"]['datetime']['utc']
                })
    return all_measurements

def get_pagination_length(endpoint_response):
    response_json = get_results(endpoint_response)
    return len(response_json["results"])

def extract_item_ids(response):
    item_ids = []
    results = get_results(response)
    for item in results:
        if "id" in item:
            item_ids.append(item["id"])
    return item_ids

# Function to verify overlapping of IDs in multiple pages
def verify_multi_pagination_items(page_1_response, page_2_response):
    ids_page_1 = extract_item_ids(page_1_response)
    ids_page_2 = extract_item_ids(page_2_response)

    overlap = set(ids_page_1).intersection(set(ids_page_2))
    return len(overlap) > 0