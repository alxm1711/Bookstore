
Feature: User Login and shopping E2E
  As a registered user
  I want to be able to login to the application
  So that I can access my account and shop for books

  Scenario: Successful login
    Given I open "https://books-store.ro/"
    When I navigate to login page
    And I enter valid username "alexandramunteanu1711@gmail.com"
    And I enter a valid password "Testpassw0rd12!@3"
    And I click the login button
    Then I should be redirected to my account section

  Scenario: Shopping for a book
    When I search for "Pachet George Orwell"
    And I select the book from the search results
    And I view the book's detail page
    And I add the book to shopping cart
    And I navigate to the shopping cart page
    And I proceed to the checkout page
#    And I enter billing details
#    And I enter shipping details
#    And I place the order
#    Then I should see a confirmation of my order