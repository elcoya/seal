Feature: As a User I can change de password

	 Scenario: Change password succesfull
		Given Student "martin" exists with password "martin"
	 	  And I log in as "martin" "martin"
		 When I click the button "changepassword"
		  And I fill the change password form with user "martin", oldpass "martin", newpass "mauro", newpassagin "mauro"
		  And I submit the form
		 Then I should see "Change password successfully!"
		 
	Scenario: Change password error user and old password
		Given Student "martin" exists with password "martin"
	 	  And I log in as "martin" "martin"
		 When I click the button "changepassword"
		  And I fill the change password form with user "martin", oldpass "error", newpass "mauro", newpassagin "mauro"
		  And I submit the form
		 Then I should see "User or password not exist"
		 
	Scenario: Change password error not match new password
		Given Student "martin" exists with password "martin"
	 	  And I log in as "martin" "martin"
		 When I click the button "changepassword"
		  And I fill the change password form with user "martin", oldpass "martin", newpass "not", newpassagin "match"
		  And I submit the form
		 Then I should see "Passwords does not match"
		 
