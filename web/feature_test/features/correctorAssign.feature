Feature: As a teacher I want to assing a correction of another teacher

	Scenario: No assing correction
	 	Given course "2012-1" exists 
		  And Teacher "teacher" exists with password "teacher"	
	 	  And Student "martin" exists with password "martin"
	 	  And student "martin" exists in course "2012-1"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And exist delivery of "TP Intro" from student "martin" whit dalivery date "2012-11-01"
	 	 When I log in as "teacher" "teacher"
	 	 Then I should see "There are no corrections"
	 	 
	Scenario: No assing correction
	 	Given course "2012-1" exists 
		  And Teacher "teacher" exists with password "teacher"	
	 	  And Student "martin" exists with password "martin"
	 	  And student "martin" exists in course "2012-1"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And exist delivery of "TP Intro" from student "martin" whit dalivery date "2012-11-01"
	 	 When I log in as "teacher" "teacher"
		  And I click in the "2012-1" link
		  And I click in the "martin" link
		  And I select the corrector "teacher"
		  And I submit the form
		  And I am in the index page
		 Then I should see "Pending"
