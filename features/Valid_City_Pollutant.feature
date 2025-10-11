# Author: Vikas Deswal
# Created on 3rd Oct 2025

Feature: Air Quality API - Get latest pollutant measurements
  As a user of the OpenAQ API
  I want to request pollutant measurements for a given city
  So that I can verify the availability and quality of air quality dat

  @smoke @regression @positive
  Scenario: Fetch coordinates for a valid city
    Given a city <city>
    When I fetch the coordinates for that city
    Then I should receive valid latitude and longitude values

  @positive @regression
  Scenario Outline: Get latest pollutant measurement using city coordinates
    Given city <city> with pollutant <pollutant> and search radius <radius> KM
    And I have valid coordinates <coordinates> for that city
    When I request the latest measurement for that pollutant within the radius
    Then the response status should be 200
    And the system should return recent pollutant measurements for city

    Examples:
      | city | pollutant | radius | coordinates |
      | Delhi | PM2.5 | 20 | 28.744,77.12 |

  @negative @regression
  Scenario Outline: Invalid pollutant should return no results
    Given city <city> with pollutant <pollutant> and search radius <radius> KM
    And I have valid coordinates <coordinates> for that city
    When I request the latest measurement for that pollutant within the radius
    Then the response status should be 200
    And the system should return empty results
    Examples:
      | city | pollutant | radius | coordinates |
      | Mumbai | xyz123 | 15 | 18.95,72.83 |