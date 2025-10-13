# Author: Vikas Deswal
# Created on 09/10/25

Feature: Pagination and Limit Behavior
    As a user of the OpenAQ API
    I want to verify pagination and limit behavior
    So that I can ensure consistent and efficient data retrieval

  Scenario Outline: Limit parameter is respected
    Given I call the <endpoint> endpoint with limit <limit> and page <page>
    When I fetch the response
    Then the response status should be 200
    And the response should contain limit or fewer items

    Examples:
      | endpoint | limit | page |
      | /locations | 20 | 1 |
      | /countries | 10 | 2 |

  Scenario Outline: Pagination returns distinct results
    Given I call the <endpoint> endpoint with limit <limit> for multiple pages
    When I fetch page 1 and page 2
    Then Items in both pages should not overlap

    Examples:
      | endpoint   | limit |
      | /locations | 5     |