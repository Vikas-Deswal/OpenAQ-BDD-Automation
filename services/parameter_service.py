from utilities.api_client import get_results
from utilities.logging_config import logger

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