Feature: As a user I can change lenguaje

	 Scenario: Index page whith options for change lenguaje
		Given I am not logged in
	 	  And I am in the index page
		 Then I should see "Change Lenguaje"
	
	 Scenario: Index page change lenguaje English to Spanish and Spanish to English
		Given I am not logged in
	 	  And I am in the index page
	 	 When I click in the "Click Here" link
	 	  And I select lenguaje "Español"
	 	  And I submit the form
	 	  And I click in the "Click Aqui" link
	 	  And I select lenguaje "English"
	 	  And I submit the form
	 	 Then I should see "Login" 	 

	
