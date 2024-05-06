Feature: Login to NCC  
  Scenario: Login with valid credentials
    Given I am on the login page
    When I enter my username and password
    And I click the "btnLogin" button
    # Then I should see the homepage