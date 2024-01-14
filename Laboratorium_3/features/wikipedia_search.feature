# Created by adam at 11/01/2024
Feature: Wikipedia Search Functionality

  Scenario: Searching for a term on Wikipedia
    Given I am on the Wikipedia home page
    When I search for "Python"
    Then the search results should include "Python"