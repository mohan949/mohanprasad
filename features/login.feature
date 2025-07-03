Feature: Login

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I login with username "user1" and password "pass1"
    Then I should see the dashboard
