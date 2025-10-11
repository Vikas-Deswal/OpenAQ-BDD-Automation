from behave import *
import logging
from services.openAQ import *

# ---- Scenario 1 ----
@given('a city {city}')
def step_set_city(context, city):
    context.city = city

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

@given('I have valid coordinates {coordinates} for that city')
def step_reuse_coordinates(context, coordinates):
    context.coordinates = coordinates

@when('I request the latest measurement for that pollutant within the radius')
def request_latest_measurements(context):
    context.response = get_location_data(context.coordinates, context.radius)
    logging.info(f"Response status code is {context.response.status_code}")

@then('the response status should be {status_code_value:d}')
def verify_response_status(context, status_code_value):
    assert context.response.status_code == status_code_value

@then('the system should return recent pollutant measurements for city')
def retrieve_pollutant_measurements(context):
    latest_measurements = get_latest_measurements(context.response, context.pollutant)
    assert len(latest_measurements) > 0, "No measurements returned"

    for m in latest_measurements:
        assert isinstance(m["value"], (int, float)), f"Invalid value: {m['value']}"
        assert m["datetime"] is not None, "Missing datetime"

@then('the system should return empty results')
def verify_empty_results(context):
    latest_measurements = get_latest_measurements(context.response, context.pollutant)
    assert len(latest_measurements) == 0, f"Expected no results, got {len(latest_measurements)}"