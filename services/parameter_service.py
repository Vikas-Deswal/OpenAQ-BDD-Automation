import requests

from utilities.api_client import get_results, get_endpoint_response
from utilities.logging_config import logger
import time

# Countries and parameters metadata service
def validate_parameters(endpoint_response, expected_keys):
    results = get_results(endpoint_response)
    if not results:
        raise AssertionError("No parameters found in the response")

    # Checking the parameters for each return item
    for parameter in results:
        for key in expected_keys:
            if key not in parameter:
                raise AssertionError(f"Missing key: '{key}' in parameter: {parameter}")
            if parameter[key] in ["None", "", []]:
                raise AssertionError(f"Empty or Missing value: '{key}' in parameter: {parameter}")

    return True

def get_country_from_code(response, country_code):
    results = get_results(response)
    if not results:
        raise AssertionError("No countries found in the response")

    for country in results:
        if country["code"].upper() == country_code.upper():
            logger.info(f"Found valid country: {country_code}")
            return country
    return None

def validate_country_metadata(response, country_code, country_name):
    country_match_result = get_country_from_code(response, country_code)
    if not country_match_result:
        raise AssertionError(f"No valid country found for code: {country_code}")

    if country_match_result["name"] != country_name:
        raise AssertionError(
            f"Country name mismatch for code={country_code}: expected '{country_name}', got '{country_match_result['name']}'"
        )

    logger.info(f"Validated metadata for code={country_code}, name={country_name}")
    return True

def validate_endpoint_headers(endpoint_response, required_headers):
    actual_headers = endpoint_response.headers
    for header in required_headers:
        missing_header = []
        if header not in actual_headers:
            missing_header.append(header)
        if missing_header:
            raise AssertionError(f"Missing header: '{header}'")
    logger.info(f"All required headers found: {required_headers}")
    return True

def hit_multiple_requests(endpoint, delay=1):
    responses = []
    for i in range(3):
        try:
            resp = get_endpoint_response(endpoint)
            if resp.status_code == 200:
                responses.append(resp)
            else:
                logger.warning(f"Request {i + 1} failed with status {resp.status_code}")

            time.sleep(delay)

        except requests.exceptions.RequestException as e:
            logger.error(f"Request {i + 1} failed with exception: {e}")
    return responses

def verify_ratelimit_decrease(responses):
    ratelimit_values = []
    for idx, response in enumerate(responses, start=1):
        header_idx = response.headers.get("x-ratelimit-remaining")

        if header_idx is None:
            raise AssertionError(f"Missing header: 'x-ratelimit-remaining' in response {idx}")
        try:
            remaining_value = int(header_idx)
        except ValueError:
            raise AssertionError(f"Header value not integer in response #{idx}: {header_idx}")

        ratelimit_values.append(int(header_idx))
        logger.info(f"Request #{idx + 1}: Remaining = {header_idx}")

    return ratelimit_values