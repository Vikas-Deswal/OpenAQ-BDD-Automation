from behave import *
from services.openAQ_service import *
from utilities.logging_config import logger

# --Scenario 1 of Pagination & Limit Behaviour --
@given('I call the {endpoint} endpoint with limit {limit} and page {page}')
def step_given_endpoint_pagination(context, endpoint, limit, page):
    context.endpoint = endpoint
    context.limit = int(limit)
    context.page = int(page)
    logger.info(f"-- Starting Pagination Scenario --")
    logger.info(f"Endpoint: {endpoint}, Limit: {limit}, Page: {page}")

@when('I fetch the response')
def step_fetch_response(context):
    logger.info(f"Fetching response from endpoint: {context.endpoint}")
    context.response = get_endpoint_response(context.endpoint, params={"page": context.page, "limit": context.limit})
    logger.info(f"Response received from endpoint: {context.endpoint}")

@then('the response should contain limit or fewer items')
def step_check_limit(context):
    logger.info(f"Validating pagination limit for endpoint: {context.endpoint}")
    items_count = get_pagination_length(context.response)
    if items_count is False:
        logger.error("Response JSON does not contain 'results' key.")
        assert False, "Invalid response structure — missing 'results' key."
    logger.info(f"Items returned: {items_count}, Limit set: {context.limit}")

    assert items_count <= context.limit, f"Expected ≤ {context.limit} items, but got {items_count}"
    logger.info("Pagination limit validation passed successfully")

# --Scenario 2 of Pagination & Limit Behaviour --
@given('I call the {endpoint} endpoint with limit {limit} for multiple pages')
def step_given_multi_pages(context, endpoint, limit):
    context.endpoint = endpoint
    context.limit = int(limit)
    logger.info(f"Starting test for 1st & 2nd page: {context.endpoint}, limit: {context.limit}")

@when('I fetch page 1 and page 2')
def step_fetch_multi_pages_response(context):
    logger.info(f"Fetching response of page 1 and page 2")
    context.page_1_response = get_endpoint_response(context.endpoint, params={"page": 1 ,"limit": context.limit})
    context.page_2_response = get_endpoint_response(context.endpoint, params={"page": 2, "limit": context.limit})
    logger.info(f"Page 1 Status={context.page_1_response.status_code}, Page 2 Status={context.page_2_response.status_code}")

@then('Items in both pages should not overlap')
def step_then_verify_items_overlap(context):
    overlap = verify_multi_pagination_items(context.page_1_response, context.page_2_response)
    if overlap:
        logger.error("Duplicate items found across pages")
    else:
        logger.info("No overlapping items found between Page 1 and Page 2")
    assert not overlap, "Some items are repeated across page 1 and page 2"