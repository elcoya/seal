Feature: As a student I can register myself into seal

	 Scenario: Register with a captcha error
	 	Given I am not logged in
	 	  And user "test" is not registered
	 	  And I am in the index page
		 When I am in the registration page
		  And I fill in the registration form with user "test"
		  And I submit the form
		 Then I should see "You Must Be a Robot"