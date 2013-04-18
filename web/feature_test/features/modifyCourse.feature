Feature: As a teacher I want to modify a name course

 	Scenario: Index page follow link to edit course and modify the course
        Given Teacher "teacher" exists with password "teacher"
    	  And course "2012-1" exists
          And I log in as "teacher" "teacher"
         When I am in the edit page of course "2012-1"
          And I change "2012-1" for "2013-1" in element whith id "id_name"
          And I submit the form
         Then I should see "2013-1"