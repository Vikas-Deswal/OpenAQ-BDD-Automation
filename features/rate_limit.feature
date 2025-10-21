# Author: Vikas Deswal
# Created on 15/10/25

Feature: Rate Limit and Header Validation
  As a responsible API user
  I want to verify rate-limit headers and their behavior
  So that I understand and respect API usage limits

  @headers @smoke
  Scenario: Validate rate-limit headers are present
    Given I make a GET request to /locations
    When I receive the response
    Then response headers should include "x-ratelimit-used", "x-ratelimit-remaining", and "x-ratelimit-reset"

  @headers @regression
  Scenario: Rate limit decreases on consecutive requests
    Given I make multiple requests to /locations
    When I compare rate-limit-remaining headers
    Then the remaining limit should decrease or stay consistent across calls