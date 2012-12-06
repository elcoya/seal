Feature: As a student I can regenerate de password

	 Scenario: Index page link
		Given I am not logged in
	 	  And I am in the index page
		 Then I should see "Recovery"
	 
	 Scenario: Recovery succesfull
	 	Given I am not logged in
	 	  And Student "martin" exists with email "martin@foo.foo"
	 	  And I am in the index page
		 When I click in the "Recovery" link
		  And I fill the recovery form with user "martin" and email "martin@foo.foo"
		  And I submit the form
		 Then I should see "Recovery completed successfully!"
		 
	 Scenario: Recovery Fail because diferent email
	 	Given I am not logged in
	 	  And Student "martin" exists with email "martin@foo.foo"
	 	  And I am in the index page
		 When I click in the "Recovery" link
		  And I fill the recovery form with user "martin" and email "mauro@foo.foo"
		  And I submit the form
		 Then I should see "E-mail or Username didn't match, please try again."
	
	Scenario: Recovery Fail because diferent username
	 	Given I am not logged in
	 	  And Student "martin" exists with email "martin@foo.foo"
	 	  And I am in the index page
		 When I click in the "Recovery" link
		  And I fill the recovery form with user "mauro" and email "martin@foo.foo"
		  And I submit the form
		 Then I should see "E-mail or Username didn't match, please try again."
	
	Scenario: Recovery Fail because not existe user
	 	Given I am not logged in
	 	  And there are no students
	 	  And I am in the index page
		 When I click in the "Recovery" link
		  And I fill the recovery form with user "martin" and email "martin@foo.foo"
		  And I submit the form
		 Then I should see "E-mail or Username didn't match, please try again."
					