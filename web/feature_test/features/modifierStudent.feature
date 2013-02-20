Feature: As a teacher I want to modifier a student

 	Scenario: Index page follow link to edit course, edit student and modifier the name of the student
        Given Teacher "teacher" exists with password "teacher"
          And there are no practices
	  	  And Student "martin" exists with password "martin"
    	  And course "2012-1" exists
          And student "martin" exists in course "2012-1"
          And I log in as "teacher" "teacher"
         When I click in the "2012-1" link
          And I click in the "martin" link 
          And I change "martin" for "Martin Mauro" in element whith id "id_name"
          And I submit the form
         Then I should see "Martin Mauro"