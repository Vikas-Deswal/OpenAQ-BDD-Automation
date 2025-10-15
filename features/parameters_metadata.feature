# Author: Vikas Deswal
# Created on 14/10/25

Feature: Pollutant Parameters Metadata
  As a developer or data analyst
  I want to validate available pollutant parameters and their attributes
  So that I can ensure pollutant data consistency

  @metadata @smoke
  Scenario: Validate all pollutant parameters are listed
    Given I call the /parameters endpoint
    When I receive the response
    Then the response status should be 200
    And each parameter should have "id", "displayName", "name", and "units"

  @schema @regression
  Scenario Outline: Validate all pollutant parameters are listed
    Given I call the <endpoint> endpoint
    When I receive the response
    Then the response status should be 200
    And each parameter should have correct <expected_keys>
    Examples:
      | endpoint  | expected_keys |
      | /parameters  | ["id", "name", "units", "displayName"] |
      | /countries  | ["id", "code", "name"] |


  @negative
  Scenario: Invalid parameter ID should return 404
    Given I call invalid parameters/9999 endpoint
    When I receive the response
    Then the response status should be 404