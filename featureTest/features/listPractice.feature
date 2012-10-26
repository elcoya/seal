Feature: As a user I want to see the practice list
    
    Scenario: No practice
        Given there are no practice
          And I am in the practice list page
         Then I should see "0 practice"
