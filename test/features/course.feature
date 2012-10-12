Feature: As a professor I want to see the course list

    Scenario: No courses
        Given I have opened the browser for "http://localhost:8000/admin"
		  And I log in as "seal" "seal"
          And I am in the course list page
          And there are no courses 
         Then I should see "0 courses"

	Scenario: No courses
	   Given I have opened the browser for "http://localhost:8000/admin"
		When I log in as "seal" "seal" 
		 And I enter in the course list
		Then I should see "0 courses"
		 And I logout
		 And I close de browser

    Scenario: Courses ordered by newest first
       Given I have opened the browser for "http://localhost:8000/admin"
        When I log in as "seal" "seal" 
         And I enter in the course list
         And course "2012-1" exists
         And course "2011-1" exists
        Then I should seee "2012-1" before "2011-1" 
         And I logout
	     And I close de browser
