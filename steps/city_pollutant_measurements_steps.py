from behave import *
from services.openAQ_service import *
from utilities.logging_config import logger
import allure

# ---- Scenario 1 ----
@given('a city {city}')
def step_set_city(context, city):
    context.city = city
    logger.info("city set to {}".format(context.city))

@when('I fetch the coordinates for that city')
def step_fetch_coordinates(context):
    # Fake lookup / API call
    context.coordinates = {"lat": 28.6139, "lng": 77.2090}  # Example: Delhi

@then('I should receive valid latitude and longitude values')
def step_validate_coordinates(context):
    coords = context.coordinates

# ---- Scenario 2 ----
@given('city {city} with pollutant {pollutant} and search radius {radius} KM')
def step_set_pollutant_and_radius(context, city, pollutant, radius):
    context.radius = int(radius)*1000
    context.city = city
    context.pollutant = pollutant
    logger.info(f"City: {city}, Pollutant: {pollutant}, Radius: {radius} km")

@given('I have valid coordinates {coordinates} for that city')
def step_reuse_coordinates(context, coordinates):
    context.coordinates = coordinates
    logger.info(f"Reuse coordinates: {context.coordinates}")

@when('I request the location data for pollutant within the radius')
def request_latest_measurements(context):
    logger.info(f"Requesting location data for: {context.city} having coordinates: {context.coordinates} and radius: {context.radius} km")
    context.response = get_location_data(context.coordinates, context.radius)
    logger.info(f"Response status code: {context.response.status_code}")

@then('the response status should be {status_code_value:d}')
def verify_response_status(context, status_code_value):
    logger.info(f"Validating response status code")
    assert context.response.status_code == status_code_value,  f"Expected {status_code_value}, got {context.response.status_code}"

@then('the system should return recent pollutant measurements for city')
def retrieve_pollutant_measurements(context):
    latest_measurements = get_latest_measurements(context.response, context.pollutant)
    assert len(latest_measurements) > 0, "No measurements returned"
    logger.info(f"Received {len(latest_measurements)} measurements for pollutant {context.pollutant}")

    for m in latest_measurements:
        assert isinstance(m["value"], (int, float)), f"Invalid value: {m['value']}"
        assert m["datetime"] is not None, "Missing datetime"

    logger.info("Measurement validation passed successfully.")

@then('the system should return empty results')
def verify_empty_results(context):
    latest_measurements = get_latest_measurements(context.response, context.pollutant)
    assert len(latest_measurements) == 0, f"Expected no results, got {len(latest_measurements)}"
    logger.info(f"No results found as expected for pollutant: {context.pollutant}")