# Author: Vikas Deswal
# Created on 22/10/25

Feature: Response Time Validation
  As a QA Engineer
  I want to ensure the API responds within an acceptable time
  So that system performance remains consistent

  @performance
  Scenario Outline: Validate response time for major endpoints
    Given I call the <endpoint> endpoint
    When I record the response time
    Then it should be less than 2000 milliseconds
    Examples:
      | endpoint     |
      | /locations   |
      | /parameters  |
      | /countries   |