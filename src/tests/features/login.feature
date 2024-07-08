
Feature: User Login
  As a registered user
  I want to be able to login to the application
  So that I can access my account

  Scenario: Successful login
    Given I open "https://carturesti.ro/?lang=en-US"
    When I navigate to login page
    And I enter valid username "testuser@example.com"
    And I enter a valid password "123456"
    And I click the login button
    Then I should be redirected to the dashboard