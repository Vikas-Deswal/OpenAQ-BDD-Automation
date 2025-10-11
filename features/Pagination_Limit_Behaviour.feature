# Author: Vikas Deswal at 09/10/25
  # In Progress Now

Feature: Pagination and limit behavior
  # Enter feature description here

  Scenario: Limit parameter respected
    Given I request locations with limit=5
    When I fetch page 1
    Then I should get exactly 5 items (or ≤ 5 if total < 5)