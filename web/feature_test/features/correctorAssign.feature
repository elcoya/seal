Feature: As a teacher I want to assing a correction of another teacher

	Scenario: No assing correction
	 	Given course "2012-1" exists 
		  And a shift with name "tarde" and description "horario" in the course "2012-1"
		  And Teacher "teacher" exists with password "teacher"	
	 	  And Student "martin" exists with password "martin"
	 	  And student "martin" exists in course "2012-1" and in shift "tarde"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And exist delivery of "TP Intro" from student "martin" whit dalivery date "2012-11-01"
	 	 When I log in as "teacher" "teacher"
	 	 Then I should see "There are no corrections"
	 	 
	Scenario: Assing correction of delivery susccesfull
	 	Given course "2012-1" exists 
	 	  And a shift with name "tarde" and description "horario" in the course "2012-1"
		  And Teacher "teacher" exists with password "teacher"	
	 	  And Student "martin" exists with password "martin"
	 	  And student "martin" exists in course "2012-1" and in shift "tarde"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And a delivery exists for practice "TP Intro" and course "2012-1" from Student "martin" with id "1"
	 	  And the automatic correction of delivery with id "1" is "successfull"
	 	 When I log in as "teacher" "teacher"
		  And I am in the page of student list of shift "tarde" of course "2012-1"
		  And I click the button "editmartin"
		  And I select the corrector "teacher"
		  And I submit the form
		  And I am in the index page
		 Then I should see "Pending"

	Scenario: Assing correction of delivery susccesfull, delivery fail and pending
	 	Given course "2012-1" exists 
	 	  And a shift with name "tarde" and description "horario" in the course "2012-1"
		  And Teacher "teacher" exists with password "teacher"	
	 	  And Student "martin" exists with password "martin"
	 	  And student "martin" exists in course "2012-1" and in shift "tarde"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And a delivery exists for practice "TP Intro" and course "2012-1" from Student "martin" with id "1"
	 	  And a delivery exists for practice "TP Intro" and course "2012-1" from Student "martin" with id "2"
	 	  And a delivery exists for practice "TP Intro" and course "2012-1" from Student "martin" with id "3"
	 	  And the automatic correction of delivery with id "1" is "successfull"
	 	  And the automatic correction of delivery with id "2" is "failed"
	 	  And the automatic correction of delivery with id "3" is "pending"
	 	 When I log in as "teacher" "teacher"
		  And I am in the page of student list of shift "tarde" of course "2012-1"
		  And I click the button "editmartin"
		  And I select the corrector "teacher"
		  And I submit the form
		  And I am in the index page
		 Then I should see "successfull" 
		  And I should not see "failed"
		  And I should not see "pending"
