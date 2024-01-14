# Created by adam at 11/01/2024
Feature: Sauce Demo Login and Add to Cart

  Scenario: Standard user logs in and adds a product to the cart
    Given I am on the Sauce Demo login page
    When I enter valid credentials
    And I add a product to the cart
    Then the product should be added to the cart successfully
