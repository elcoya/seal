Feature: As a student I cannot access administration pages

	 Scenario: Student cannot see courses in which they do not exist
	  	Given student "test" exists with password "test"
	 	  And course "2012-1" exists
	 	  And course "2012-2" exists
	 	  And a shift with name "tarde" and description "horario" in the course "2012-1"
	 	  And a shift with name "tarde" and description "horario" in the course "2012-2"
	 	  And student "test" exists in course "2012-1" and in shift "tarde"
	 	  And student "test" does not exist in course "2012-2" and in shift "tarde"	
	 	 When I log in as "test" "test"
		 Then I should see "2012-1-tarde"
		  
