Feature: As a teacher I want to create and modifier innings

	 Scenario: Create Inning
	 	Given Teacher "teacher" exists with password "teacher"
          And course "2012-1" exists
          And I log in as "teacher" "teacher" 
         When I click in the "2012-1" link
          And I click in the "New Inning" link
          And I fill the inning form with name "tarde" and description "horario"
          And I submit the form
		 Then I should see "tarde"

	 Scenario: Modifier Inning
	 	Given Teacher "teacher" exists with password "teacher"
          And course "2012-1" exists
          And a inning with name "tarde" and description "horario" in the course "2012-1"
          And I log in as "teacher" "teacher" 
         When I click in the "2012-1" link
          And I click in the "tarde" link
          And I change "horario" for "description" in element whith id "id_description"
          And I submit the form
		 Then I should see "description"
