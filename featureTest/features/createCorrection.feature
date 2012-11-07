Feature: As a teacher I want to make a correction of a delivery

	 Scenario: Corretion of a delivery fist time
	 	Given course "2012-1" exists 
	 	  And user "Martin" is registered
	 	  And student "Martin" exists in course "2012-1"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And exist delivery of "TP Intro" from student "Martin" whit dalivery date "2012-11-01"
	 	 when I am in the correction delivery page of student "Martin" and practice "TP Intro"
	 	  And I fill the form with "Coment1" "Coment2" "4.0"
	 	  And I submit the form
		  And I click in the "Correction" link
		 Then I should have the edit form for correction with "Coment1" "Coment2" "4.0" data in it	
		 
		 
      Scenario: Modifier corretion of a delivery
		Given course "2012-1" exists 
	 	  And user "Martin" is registered
	 	  And student "Martin" exists in course "2012-1"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And exist delivery of "TP Intro" from student "Martin" whit dalivery date "2012-11-01"
	 	  And exist correction of delivery of "Martin" for "TP Intro" with "Coment1" "Coment2" "4.0"
	 	 When I am in the correction delivery page of student "Martin" and practice "TP Intro"
	 	  And I change "Coment1" for "New coment 1" in element whith id "id_publicComent"
	 	  And I submit the form
	 	  And I click in the "Correction" link	
	 	 Then I should have the edit form for correction with "New coment 1" "Coment2" "4.0" data in it	
		 