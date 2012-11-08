Feature: As a teacher I want to create a practice

	 Scenario: Create Practice
	 	Given Teacher "teacher" exists with password "teacher"
          And there are no practices
    	  And course "2012-1" exists
          And I log in as "teacher" "teacher"
          And I am at the new practice form for course "2012-1" 
         When I fill the practice form with uid "practice_1" and default data for course "2012-1"
          And I submit the form
		 Then I should see "practice_1"