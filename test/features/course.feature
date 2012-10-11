Feature: As a professor I want to see the course list

	Scenario: No courses
	   Given we have opened the browser for "http://localhost:8000/admin"
		When we log in as "seal" "seal" 
		 And we enter in the course list
		Then we should see "0 courses"
		 And we logout
		 And we close de browser

    Scenario: Courses ordered by newest first
       Given we have opened the browser for "http://localhost:8000/admin"
       When we log in as "seal" "seal" 
        And we enter in the course list
        And course "2012-1" exists
        And course "2011-1" exists
       Then we should seee "2012-1" before "2011-1" 
       	And we logout
		And we close de browser