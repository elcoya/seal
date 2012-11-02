Feature: As a teacher I want to create a practice

	 Scenario: Create Practice
	 	Given there are no practices
	 	  And course "2012-1" exists
          And I am at the new practice form for course "2012-1" 
         When I fill the practice form with uid "practice_uid_1" and default data for course "2012-1"
          And I submit the form
		 Then I should see "practice_uid_1"