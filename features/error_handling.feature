# Author: Vikas Deswal
# Created on 22/10/25

Feature: Error Handling and Negative Scenarios
  As an API tester
  I want to validate API responses for invalid or missing inputs
  So that the system behaves gracefully under bad requests

  @negative
  Scenario Outline: Invalid endpoint should return 404
    Given I hit invalid <endpoint>
    When I receive the response
    Then the response status should be <status_code>
    Examples:
      | endpoint                    | status_code |
      | /measurements123            |  404        |
      | /locations?coordinates=abc  |  500        |

  @negative
  Scenario: Missing API key should return unauthorized error
    Given I make a request to /locations without a valid API key
    When I receive the response
    Then the response status should be 401