from behave import *
from utilities.api_client import get_endpoint_response
from utilities.logging_config import logger

# Scenario 1: Hitting Invalid Endpoints
@given('I hit invalid {endpoint}')
def step_hit_invalid_endpoint(context, endpoint):
    context.endpoint = endpoint
    logger.info(f"Hitting Invalid Endpoint {endpoint}")
    context.response = get_endpoint_response(endpoint)

# Scenario 2: Hitting with Invalid API Key
@given('I make a request to {endpoint} without a valid API key')
def step_make_a_request_without_valid_api_key(context, endpoint):
    context.endpoint = endpoint
    logger.info(f"Making a request to {endpoint} without a valid API key")
    context.response = get_endpoint_response(endpoint, headers={"x-api-key": "abc1234"})