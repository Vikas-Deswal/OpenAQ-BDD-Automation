# Author: Vikas Deswal
# Created on 14/10/25

Feature: Country Metadata and Filtering
  As an API user
  I want to verify country details and their use in filtering data
  So that I can ensure data integrity across countries

  @metadata @smoke
  Scenario: Validate country metadata contains India
    Given I call the /countries endpoint
    When I receive the response
    Then the response should contain country code IN and name India

  @integration @regression
  Scenario Outline: Validate country details using country ID
    Given I call the /countries endpoint
    And I get the country id for code <code>
    When I call the countries with the id
    Then the response status should be 200
    And the response should contain country code <code> and name <expected_name>
    Examples:
      | code | expected_name |
      | IN   |  India        |
      | DE   |  Germany      |