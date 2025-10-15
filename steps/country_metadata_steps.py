from behave import *
from services.parameter_service import *
from utilities.api_client import get_endpoint_response
from utilities.logging_config import logger

# -- Scenario 1: Validate country metadata --
# Given and when of this scenario is covered in parameters_meta_data_steps

@then("the response should contain country code {code} and name {expected_name}")
def step_verify_country_code(context, code, expected_name):
    logger.info(f"Verifying returned country code={code}, expected_name={expected_name}")
    country_metadata_found = validate_country_metadata(context.response, code, expected_name)
    assert country_metadata_found, f"Mismatch in returned country details for {expected_name} & {code})"

# -- Scenario 2: Country ID to filter locations --
@given("I get the country id for code {code}")
def step_get_country_id(context, code):
    context.code = code
    logger.info(f"Getting country id for code={code}")
    country = get_country_from_code(context.response, code)
    assert country, f"Country with code '{code}' not found in /countries response"
    context.country_id = country["id"]
    context.actual_code = country["code"]
    context.actual_country_name = country["name"]

@when("I call the countries with the id")
def step_call_countries_id(context):
    context.response = get_endpoint_response(f"/countries?id={context.country_id}")
    logger.info(f"Called /countries?id={context.country_id}")