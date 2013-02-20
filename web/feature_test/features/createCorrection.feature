Feature: As a teacher I want to make a correction of a delivery

	 Scenario: Corretion of a delivery fist time
    	Given Student "martin" exists with password "martin"
    	  And Teacher "teacher" exists with password "teacher"
    	  And I log in as "teacher" "teacher"
    	  And course "2012-1" exists
	 	  And student "martin" exists in course "2012-1"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And exist delivery of "TP Intro" from student "martin" whit dalivery date "2012-11-01"
	 	  And there are no corrections
	 	 when I am in the correction delivery page of student "martin" and practice "TP Intro"
	 	  And I fill the form with "Coment1" "Coment2" "4.0"
	 	  And I submit the form
		  And I click in the "Correction" link
		 Then I should have the edit form for correction with "Coment1" "Coment2" "4.0" data in it	
		 
		 
      Scenario: Modify corretion of a delivery
		Given Student "martin" exists with password "martin"
    	  And Teacher "teacher" exists with password "teacher"
    	  And I log in as "teacher" "teacher"
    	  And course "2012-1" exists
	 	  And student "martin" exists in course "2012-1"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And exist delivery of "TP Intro" from student "martin" whit dalivery date "2012-11-01"
	 	  And exist correction of delivery of "martin" for "TP Intro" with "Coment1" "Coment2" "4.0"
	 	 When I am in the correction delivery page of student "martin" and practice "TP Intro"
	 	  And I change "Coment1" for "New coment 1" in element whith id "id_publicComent"
	 	  And I submit the form
	 	  And I click in the "Correction" link	
	 	 Then I should have the edit form for correction with "New coment 1" "Coment2" "4.0" data in it	
		 