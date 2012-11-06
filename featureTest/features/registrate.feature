Feature: As a student I can register myself into seal

	 Scenario: Index page link
		Given I am not logged in
	 	  And I am in the index page
		 Then I should see "Registrate"
	 
	 Scenario: Register as new Student
	 	Given I am not logged in
	 	  And user "test" is not registered
	 	  And I am in the index page
		 When I click in the "Registrate" link
		  And I fill in the registration form with user "test"
		  And I submit the form
		 Then I should see "Registration completed successfully"

	 @dev	 
	 Scenario: User already registered
	  	Given I am not logged in
	 	  And user "test" is registered
	 	  And I am in the index page
		 When I click in the "Registrate" link
		  And I fill in the registration form with user "test"
		  And I submit the form
		 Then I should see "User 'test' is not available"
	 