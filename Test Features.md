# OpenAQ Test Features

## Feature 1: Air Quality API - Get latest pollutant measurements
As a user of the OpenAQ API
I want to request pollutant measurements for a given city
So that I can verify the availability and quality of air quality dat

### Scenario: Fetch coordinates for a valid city**
- Given a city <city>
- When I fetch the coordinates for that city
- Then I should receive valid latitude and longitude values

### Scenario Outline: Get latest pollutant measurement using city coordinates
- Given city with pollutant and search radius KM 
- And I have valid coordinates <coordinates> for that city 
- When I request the latest measurement for that pollutant within the radius 
- Then the response status should be 200 
- And the system should return recent pollutant measurements for city

### Scenario: Invalid pollutant return empty results 
- GIVEN country "IN" and city "Delhi"  
- And pollutant "xyz123"  
- WHEN I request the latest measurement  
- THEN the response status should be 200"  
- And the result list should be empty 

---
## Feature 2: Pagination and limit behavior

### Scenario: Limit parameter respected 
- GIVEN I request locations with limit=5  
- WHEN I fetch page 1  
- THEN I should get exactly 5 items (or ≤ 5 if total < 5)  

### Scenario: Pagination returns distinct results
- GIVEN I fetch page 1 and page 2 with limit=5  
- WHEN I compare results  
- THEN items should not overlap between pages  
- And the combined unique items should equal the sum of the two pages  

### Scenario: Page beyond available results
- GIVEN I request locations with limit=50 
- WHEN I fetch a very high page number (e.g., page=1000)
- THEN the response status should be 200 
- AND the results list should be empty

---
## Feature 3: Rate limit header correctness

**Scenario: Rate limit headers present**  
- GIVEN I make a request to /locations  
- WHEN I check the response headers  
- THEN I should see "x-ratelimit-used", "x-ratelimit-remaining", and "x-ratelimit-reset"  

**Scenario: Rate limit decreases on multiple calls**  
- GIVEN I make 3 quick successive requests to /locations  
- WHEN I check "x-ratelimit-remaining" in each response  
- THEN the value should decrease or stay consistent across calls  

---

## Feature 5: Country metadata lookup and usage

**Scenario: Find country by code**  
- GIVEN a country code "IN"  
- WHEN I call /countries endpoint  
- THEN I get an entry where code == "IN"  
- And it has a numeric "id"  

**Scenario: Use numeric country ID in locations filter**  
- GIVEN I obtained India’s numeric country id  
- WHEN I call /locations with countries_id filter  
- THEN I get matching locations for that country  

---

## Feature 6: Latest across all locations for a parameter

**Scenario: Latest for valid parameter**  
- GIVEN a pollutant "pm25"  
- WHEN I call /parameters/{parameter_id}/latest  
- THEN status is 200  
- And I get a list of latest values from different locations  
- And each result has "value", "coordinates", and "locationsId"  

**Scenario: Invalid parameter id**  
- GIVEN an invalid parameter id "99999"  
- WHEN I call /parameters/{parameter_id}/latest  
- THEN the response status should be 404 or 200 with empty results  