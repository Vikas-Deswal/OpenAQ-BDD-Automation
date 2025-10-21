from behave import *
from services.parameter_service import *
from utilities.logging_config import logger

# -- Scenario 1: Verifying the rate limit headers --
@given('I make a GET request to {endpoint}')
def step_get_request_headers(context, endpoint):
    context.endpoint = endpoint
    logger.info(f'Making the GET Request to {context.endpoint} endpoint')
    context.response = get_endpoint_response(endpoint)

@then('response headers should include "x-ratelimit-used", "x-ratelimit-remaining", and "x-ratelimit-reset"')
def step_verify_response_headers(context):
    required_headers = ["x-ratelimit-used", "x-ratelimit-remaining", "x-ratelimit-reset"]
    logger.info(f"Verifying response headers {required_headers}")
    headers_present = validate_endpoint_headers(context.response, required_headers)
    assert headers_present, f"Headers {required_headers} are missing"

# -- Scenario 2: Verifying if rate limit is decreasing or not --

@given('I make multiple requests to {endpoint}')
def step_multiple_requests(context, endpoint):
    context.endpoint = endpoint
    logger.info(f'Making the multiple requests to {context.endpoint} endpoint')
    context.responses = hit_multiple_requests(endpoint)

@when('I compare rate-limit-remaining headers')
def step_compare_rate_limits(context):
    logger.info(f'Comparing rate-limit-remaining headers')
    context.remaining_values = verify_ratelimit_decrease(context.responses)

@then('the remaining limit should decrease or stay consistent across calls')
def step_remaining_rate_limits(context):
    for i in range(1, len(context.remaining_values)):
        assert context.remaining_values[i] <= context.remaining_values[i - 1], (
            f"Rate limit increased between request {i} and {i + 1}"
        )
    logger.info("Rate limit headers behave correctly (decreasing or consistent).")