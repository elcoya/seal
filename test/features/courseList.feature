Feature: As a professor I want to see the course list

Scenario: No courses
		Given I am in the course list page "http://localhost:8000/admin/model/course/"
		When we input login data "seal|seal" 
		Then we should see "0 courses"
		And we logout and close de browser

Scenario: Courses ordered by newest first
		Given I am in the course list page "http://localhost:8000/admin/model/course/"
		When we input login data "seal|seal" 
		And course "2012-1" exists
		And course "2011-1" exists
		Then I should see "2012-1" before "2011-1" 