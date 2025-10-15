import ast
from behave import *
from utilities.api_client import get_endpoint_response
from services.parameter_service import *
from utilities.logging_config import logger


# -- Scenario 1: Business readable parameters check --
@given('I call the {endpoint} endpoint')
def step_call_endpoint(context, endpoint):
    context.endpoint = endpoint
    logger.info(f'Calling the {context.endpoint} endpoint')
    context.response = get_endpoint_response(endpoint)

@when('I receive the response')
def step_receive_response(context):
    assert context.response is not None, "No response received from API"

@then('each parameter should have "id", "displayName", "name", and "units"')
def step_valid_parameters(context):
    expected_parameters = ["id", "displayName", "name", "units"]
    parameters_presence = validate_parameters(context.response, expected_parameters)
    assert parameters_presence is True
    logger.info("All parameters contain expected keys and valid values")

@then('each parameter should have correct {expected_keys}')
def step_valid_endpoint_parameters(context, expected_keys):
    context.expected_keys = ast.literal_eval(expected_keys)
    parameters_presence = validate_parameters(context.response, context.expected_keys)
    assert parameters_presence is True
    logger.info("All endpoint parameters contain expected keys and valid values")

# -- Scenario 2: Negative Scenario --
@given('I call invalid parameters/{param_id} endpoint')
def step_invalid_parameters(context, param_id):
    logger.info(f"Calling invalid /parameters/{param_id} endpoint")
    context.response = get_endpoint_response(f"/parameters/{param_id}")