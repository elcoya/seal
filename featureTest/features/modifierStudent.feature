Feature: As a teacher I want to modifier a student

 	Scenario: Index page follow link to edit course, edit student and modifier the name of the student
        Given Teacher "teacher" exists with password "teacher"
          And there are no practices
	  	  And user "Martin" is registered
    	  And course "2012-1" exists
          And student "Martin" exists in course "2012-1"
          And I log in as "teacher" "teacher"
         When I click in the "2012-1" link
          And I click in the "Martin" link 
          And I change "Martin" for "Martin Mauro" in element whith id "id_name"
          And I submit the form
         Then I should see "Martin Mauro"