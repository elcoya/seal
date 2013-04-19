Feature: As a teacher I want to create and modify shifts

	 Scenario: Create Shift
	 	Given Teacher "teacher" exists with password "teacher"
          And course "2012-1" exists
          And I log in as "teacher" "teacher" 
         When I am in the page of new shift of course "2012-1"
          And I fill the shift form with name "tarde" and description "horario"
          And I submit the form
		 Then I should see "tarde"

	 Scenario: Modify Shift
	 	Given Teacher "teacher" exists with password "teacher"
          And course "2012-1" exists
          And a shift with name "tarde" and description "horario" in the course "2012-1"
          And I log in as "teacher" "teacher" 
         When I am in the page of edit shift "tarde" of course "2012-1"
          And I change "tarde" for "noche" in element whith id "id_name"
          And I submit the form
		 Then I should see "noche"
