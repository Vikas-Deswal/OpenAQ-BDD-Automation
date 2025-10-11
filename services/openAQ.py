from utilities.api_client import ApiClient
from resources.endpoints import *

# Initialising the API Client having headers & params
client = ApiClient()

# Hitting Location Endpoint & needs coordinates & radius in KM
def get_location_data(coordinates, radius):
    params = get_locations_payload(coordinates, radius)
    return client.get(V3ApiEndpoints.locations, params=params)

# Hitting Sensors Endpoint & need sensor ID to get measurement value
def get_sensors_data(sensor_id):
    return client.get(f"{V3ApiEndpoints.sensors}/{sensor_id}")

# Function to process the location API response & matching the pollutant
def get_sensors_id(location_api_response, pollutant):
    loc_data = location_api_response.json()['results']
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
        measurements_response = client.get(f"/sensors/{sensor_id}")
        response_sensors = measurements_response.json()['results']
        for measurement in response_sensors:
            if measurement["latest"] is not None:
                all_measurements.append({
                    "sensor_id": sensor_id,
                    "value": measurement["latest"]["value"],
                    "datetime": measurement["latest"]['datetime']['utc']
                })
    return all_measurements