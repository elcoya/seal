Feature: As a teacher I would like to eliminate a shift if student is not associated

	 Scenario: Delete Shift whitout students
	 	Given Teacher "teacher" exists with password "teacher"
          And course "2012-1" exists
          And a shift with name "tarde" and description "horario" in the course "2012-1"
    	  And there are no students
          And I log in as "teacher" "teacher"
         When I am in the detail page of course "2012-1"
          And I click the button "deletetarde"
         Then I should not see "tarde"
         
         
    Scenario: No button Delete in the shift whit student
	 	Given Teacher "teacher" exists with password "teacher"
          And Student "martin" exists with password "martin"
          And course "2012-1" exists
          And a shift with name "tarde" and description "horario" in the course "2012-1"
          And student "martin" exists in course "2012-1" and in shift "tarde"
          And I log in as "teacher" "teacher"
         When I am in the detail page of course "2012-1"
         Then I should not see the button "deletetarde"

	
	