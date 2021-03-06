Feature: As a teacher I want to modify a student

 	Scenario: Index page follow link to edit course, edit student and modify the name of the student
        Given Teacher "teacher" exists with password "teacher"
          And there are no practices
	  	  And Student "martin" exists with password "martin"
    	  And course "2012-1" exists
    	  And a shift with name "tarde" and description "horario" in the course "2012-1"
          And student "martin" exists in course "2012-1" and in shift "tarde"
          And I log in as "teacher" "teacher"
         When I click the button "detail2012-1"
          And I click the button "studentlisttarde" 
          And I click the button "editmartin"
          And I change "martin" for "Martin Mauro" in element whith id "id_last_name"
          And I submit the form
         Then I should see "Martin Mauro"