Feature: As a user I want to see the practice list
    
    Scenario: No practice
        Given there are no practices
          And course "2012-1" exists
          And I am in the index page
         When I click in the "2012-1" link
         Then I should see "There are yet no Practices"
