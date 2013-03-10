Feature: As a user I want to see the course list on the home page

    Scenario: Index page shows course list ordered
       Given Teacher "teacher" exists with password "teacher"
         And course "2012-1" exists
         And course "2011-1" exists
         And I log in as "teacher" "teacher"
         And I am in the index page
        Then I should see "2012-1" before "2011-1" 
    
    Scenario: Index page course list links to edit courses
       Given Teacher "teacher" exists with password "teacher"
         And course "2012-1" exists
         And I log in as "teacher" "teacher"
         And I am in the index page
        Then I should see link to "2012-1" in the list
         
    Scenario: Index page follow link to edit course
       Given Teacher "teacher" exists with password "teacher"
         And course "2012-1" exists
         And I log in as "teacher" "teacher"	
         And I am in the index page
        When I click in the "2012-1" link
        Then I should see "Course 2012-1 edit"
         And I should have the edit form for courses with "2012-1" course data in it	
    
	Scenario: Index page shows course list empty
       Given Teacher "teacher" exists with password "teacher"
         And there are no courses
         And I log in as "teacher" "teacher"
         And I am in the index page
        Then I should see "There are yet no courses"