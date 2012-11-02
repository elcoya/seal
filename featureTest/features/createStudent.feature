Feature: As a teacher I want to create a student
    
    Scenario: Create Student
        Given there are no students      
          And course "2012-1" exists
         When I am in the modifier page of course "2012-1"
          And I click in the "New Student" link
          And I fill the newstudent form with default data
	  	  And I submit the form
	     Then I should see "Dummy Student" 

