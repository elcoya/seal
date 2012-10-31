Feature: As a user I want to see the student list
    
    Scenario: No student in course 2012-1
        Given there are no student in "2012-1"
          And course "2012-1" exists
          And I am in the index page
         When I click in the "2012-1" link
         Then I should see "There are yet no Students"