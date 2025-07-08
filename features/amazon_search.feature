Feature: Amazon Product Search

  Scenario Outline: List highest and lowest price products for a search
    Given I am on the Amazon India homepage
    When I search for "<product_name>"
    Then I list the product with the highest price
    And I list the product with the lowest price
    
  Examples:
    | product_name |
    | laptop       |
    