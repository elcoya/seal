Feature: As a user I want to see the practice list
    
    Scenario: No practice
        Given there are no practices
          And course "2012-1" exists
          And I am in the index page
         When I click in the "2012-1" link
         Then I should see "There are yet no Practices"
         
    Scenario: Practices in course 2012-1 order by Dead Line
        Given course "2012-1" exists
          And practice "TP 1" exists in course "2012-1" with deadline "2012-12-02"
          And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
         when I am in the modifier page of course "2012-1"
         Then I should see "TP Intro" before "TP 1" 
