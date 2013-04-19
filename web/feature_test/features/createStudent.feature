Feature: As a teacher I want to create a student
    
    Scenario: Create Student
        Given Teacher "teacher" exists with password "teacher"
          And there are no students      
          And course "2012-1" exists
          And a shift with name "tarde" and description "horario" in the course "2012-1"
          And I log in as "teacher" "teacher"
         When I am in the page of student list of shift "tarde" of course "2012-1"
          And I click the button "newstudent"
          And I fill the newstudent form with default data for shift "tarde"
	  	  And I submit the form
	     Then I should see "dummy"
	      And I should see "Dummy Student"
		  And I should see "dummy@foo.foo"
