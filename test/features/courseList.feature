Feature: As a professor I want to see the course list

	Scenario: No courses
		Given we have opened the browser for "http://ixion-tech.com.ar:8000/admin"
		When we input login data "seal|seal" 
		And we enter in the courser list
		Then we should see "0 courses"
		And we logout and close de browser

