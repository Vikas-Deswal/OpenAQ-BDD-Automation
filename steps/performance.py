from behave import *
from utilities.logging_config import logger

@when('I record the response time')
def step_record_response_time(context):
    time_to_hit_api_ms = round(context.response.elapsed.total_seconds(),2)*1000
    context.time_to_hit_api_ms = time_to_hit_api_ms
    logger.info(f'The response time to hit {context.endpoint}is {time_to_hit_api_ms} ms')

@then('it should be less than {threshold:d} milliseconds')
def step_measure_performance(context, threshold):
    assert context.time_to_hit_api_ms < threshold, f"Request to {context.endpoint} took {context.time_to_hit_api_ms} ms"