Feature: As a teacher I want to modify a student

 	Scenario: Index page follow link to edit course, edit student and modify the name of the student
        Given Teacher "teacher" exists with password "teacher"
          And there are no practices
	  	  And Student "martin" exists with password "martin"
    	  And course "2012-1" exists
    	  And a inning with name "tarde" and description "horario" in the course "2012-1"
          And student "martin" exists in course "2012-1" and in inning "tarde"
          And I log in as "teacher" "teacher"
         When I click in the "2012-1" link
          And I click in the "List" link 
          And I click in the "martin" link 
          And I change "martin" for "Martin Mauro" in element whith id "id_last_name"
          And I submit the form
         Then I should see "Martin Mauro"