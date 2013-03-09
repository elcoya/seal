Feature: As a Administrator I want to create and modify a teacher
    
    Scenario: Create Teacher
         When I log in as "seal" "seal"
          And I click in the "Add and Modify Teacher" link
          And I click in the "New Teacher" link
	  	  And I fill the teacher form with default data
	  	  And I submit the form
	     Then I should see "teacher"
	      And I should see "First Teacher"
		  And I should see "Last Teacher"

    Scenario: Create Modify Teacher
    	Given Teacher "teacher" exists with password "teacher"
         When I log in as "seal" "seal"
          And I click in the "Add and Modify Teacher" link
          And I click in the "teacher" link
	  	  And I change "teacher" for "first_name" in element whith id "id_first_name"
	  	  And I change "teacher" for "last_name" in element whith id "id_last_name"
	  	  And I submit the form
	     Then I should see "first_name"
		  And I should see "last_name"
