Feature: As a teacher I want to see a detail of one student

	Scenario: See de detail of a student
		Given course "2012-1" exists 
		  And a shift with name "tarde" and description "horario" in the course "2012-1"
		  And Teacher "teacher" exists with password "teacher"
		  And Student "martin" exists with email "martin@gmail.com"
	 	  And student "martin" exists in course "2012-1" and in shift "tarde"
	 	  And I log in as "teacher" "teacher"
	 	 When I am in the detail page of course "2012-1"
	 	  And I click the button "studentlisttarde"
		  And I click the button "detailmartin"
		 Then I should see "martin"
		  And I should see "martin@gmail.com"
