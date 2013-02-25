Feature: As a teacher I want to see the correction list on the home page

	Scenario: No correction
	 	Given Teacher "teacher" exists with password "teacher"	
	 	  And there are no corrections
	 	 When I log in as "teacher" "teacher"
	 	 Then I should see "There are no corrections"
	 	 
	Scenario: Pending correction in the list
	 	Given course "2012-1" exists 
		  And Teacher "teacher" exists with password "teacher"	
	 	  And Student "martin" exists with password "martin"
	 	  And student "martin" exists in course "2012-1"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And exist delivery of "TP Intro" from student "martin" whit dalivery date "2012-11-01"
	 	  And Teacher "teacher" is the corrector of student "martin"
	 	 When I log in as "teacher" "teacher"
	 	 Then I should see "Pending"   
	 	 
	Scenario: Correction correction in the list
	 	Given course "2012-1" exists 
		  And Teacher "teacher" exists with password "teacher"	
	 	  And Student "martin" exists with password "martin"
	 	  And student "martin" exists in course "2012-1"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And exist delivery of "TP Intro" from student "martin" whit dalivery date "2012-11-01"
	 	  And Teacher "teacher" is the corrector of student "martin"
	 	  And exist correction of delivery of "martin" for "TP Intro" with "Coment1" "Coment2" "4.0" and corrector "teacher"
	 	 When I log in as "teacher" "teacher"
	 	 Then I should see "Corrected"   
