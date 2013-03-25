Feature: As a teacher I want to search a student for name or padron

	Scenario: Search and find a student for padron
	 	Given Teacher "teacher" exists with password "teacher"
		  And Student "martin" exists with email "martin@foo.foo"
		  And I log in as "teacher" "teacher"
		 When I am in the search page
		  And I fill the search form with data "martin"
		  And I submit the form
		 Then I should see "martin@foo.foo"
