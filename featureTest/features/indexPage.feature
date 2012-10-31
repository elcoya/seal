Feature: As a user I want to see the course list on the home page

    Scenario: Index page shows course list
       Given course "2012-1" exists
         And course "2011-1" exists
         And I am in the index page
        Then I should see "2012-1" before "2011-1" 
    
    Scenario: Index page shows course list
        Given there are no courses
          And I am in the index page
         Then I should see "There are yet no courses"
    
    Scenario: Index page course list links to edit courses
        Given course "2012-1" exists
          And I am in the index page
         Then I should see link to "2012-1" in the list
         
    Scenario: Index page follow link to edit course
        Given course "2012-1" exists
          And I am in the index page
         When I click in the "2012-1" link
         Then I should see "Course edit"
          And I should have the edit form for courses with "2012-1" course data in it
