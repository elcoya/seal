Feature: As a teacher I want to create a student
    
    Scenario: Create Student
        Given Teacher "teacher" exists with password "teacher"
          And I log in as "teacher" "teacher"
          And there are no students      
          And course "2012-1" exists
          And a shift with name "tarde" and description "horario" in the course "2012-1"
         When I am in the modify page of course "2012-1"
          And I click in the "List" link
          And I click in the "New Student" link
          And I fill the newstudent form with default data for shift "tarde"
	  	  And I submit the form
	     Then I should see "dummy"
	      And I should see "Dummy Student"
		  And I should see "dummy@foo.foo"
