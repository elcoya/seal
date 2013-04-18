Feature: As a teacher I want to make a correction of a delivery

	 Scenario: Corretion of a delivery fist time
    	Given Student "martin" exists with password "martin"
    	  And Teacher "teacher" exists with password "teacher"
    	  And course "2012-1" exists
    	  And a shift with name "tarde" and description "horario" in the course "2012-1"
	 	  And student "martin" exists in course "2012-1" and in shift "tarde"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And a delivery exists for practice "TP Intro" and course "2012-1" from Student "martin" with id "1"
	 	  And there are no corrections
	 	  And I log in as "teacher" "teacher"
	 	 when I am in the correction delivery page of student "martin" and practice "TP Intro"
	 	  And I fill the form with "Coment1" "Coment2" "4.0"
	 	  And I submit the form
		  And I am in the correction delivery page of student "martin" and practice "TP Intro"
		 Then I should have the edit form for correction with "Coment1" "Coment2" "4.0" data in it	
		 
		 
      Scenario: Modify corretion of a delivery
		Given Student "martin" exists with password "martin"
    	  And Teacher "teacher" exists with password "teacher"
    	  And course "2012-1" exists
    	  And a shift with name "tarde" and description "horario" in the course "2012-1"
	 	  And student "martin" exists in course "2012-1" and in shift "tarde"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And a delivery exists for practice "TP Intro" and course "2012-1" from Student "martin" with id "1"
	 	  And exist correction of delivery of "martin" for "TP Intro" with "Coment1" "Coment2" "4.0" and corrector "teacher"
	 	  And I log in as "teacher" "teacher"
	 	 When I am in the correction delivery page of student "martin" and practice "TP Intro"
	 	  And I change "Coment1" for "New coment 1" in element whith id "id_publicComent"
	 	  And I submit the form
	 	  And I am in the correction delivery page of student "martin" and practice "TP Intro"
	 	 Then I should have the edit form for correction with "New coment 1" "Coment2" "4.0" data in it	
		 