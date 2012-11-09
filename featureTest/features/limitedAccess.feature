Feature: As a student I cannot access administration pages

	 Scenario: Student cannot see courses in which they do not exist
	  	Given student "test" exists with password "test"
	 	  And course "2012-1" exists
	 	  And course "2012-2" exists
	 	  And student "test" exists in course "2012-1"
	 	  And student "test" does not exist in course "2012-2"
		 When I log in as "test" "test"
		 Then I should see "2012-1"
		  And I should not see "2012-2"
