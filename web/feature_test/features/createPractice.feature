Feature: As a teacher I want to create a practice

	Scenario: Create practice with valid data
	   Given Teacher "teacher" exists with password "teacher"
		 And course "2012-1" exists
		 And I log in as "teacher" "teacher"
	     And I am at the new practice form for course "2012-1" 
	    When I will the form with name "Practice_1"
		 And Deadline "tomorrow" 
	  	 And I submit the form
	  	Then I should see "Practice_1"

	Scenario: Create practice with invalid deadline
	   Given Teacher "teacher" exists with password "teacher"
		 And course "2012-1" exists
		 And I log in as "teacher" "teacher"
	     And I am at the new practice form for course "2012-1" 	
		When I will the form with name "Practice_1"
		 And Deadline "yesterday"
		 And I submit the form
		Then I should see "The deadline should be a date in the future"
		
	Scenario: Create practice with invalid date
		Given Teacher "teacher" exists with password "teacher"
		  And course "2012-1" exists
		  And I log in as "teacher" "teacher"
		  And I am at the new practice form for course "2012-1" 
		 When I will the form with name "Practice_1"
		  And Deadline "05-05-2000"
		  And I submit the form
		 Then I should see "Invalid date format, date should be in format yyyy-mm-dd"
			
	Scenario: Create practice with blank name
		Given Teacher "teacher" exists with password "teacher"
		  And course "2012-1" exists
		  And I log in as "teacher" "teacher"
		  And I am at the new practice form for course "2012-1"
		 When I will the form with blank name
		  And Deadline "tomorrow"
		  And I submit the form
		 Then I should see "Name cannot be blank"
