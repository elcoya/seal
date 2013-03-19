Feature: As a user I want to see a serializer of the list of mail pending to send

	 Scenario: Correct the delivery and see the page of serializer of mail pending to send from the correction
	 	Given Student "martin" exists with password "martin"
    	  And Teacher "teacher" exists with password "teacher"
    	  And I log in as "teacher" "teacher"
    	  And course "2012-1" exists
	 	  And a shift with name "tarde" and description "horario" in the course "2012-1"
	 	  And student "martin" exists in course "2012-1" and in shift "tarde"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And exist delivery of "TP Intro" from student "martin" whit dalivery date "2012-11-01"
	 	  And there are no corrections
	 	 when I am in the correction delivery page of student "martin" and practice "TP Intro"
	 	  And I fill the form with "Coment1" "Coment2" "4.0"
	 	  And I submit the form
	 	  And I logout
	 	  And I log in as "seal" "seal"
	 	  And I click in the "Mails to send Serializer" link
	 	 Then I should see "Tienes una correccion para ver en SEAL"
	 	  And I am in the index page
	 	  And I logout
	 	  
     Scenario: Recovery password and see the page of serializer of mail pending to send from the recovery
		Given Student "martin" exists with email "martin@foo.foo"
	 	  And I am in the index page
		 When I click in the "Recovery" link
		  And I fill the recovery form with user "martin" and email "martin@foo.foo"
		  And I submit the form
		  And I am in the index page
  	      And I log in as "seal" "seal"
	 	  And I click in the "Mails to send Serializer" link
	 	 Then I should see "Recupero de password de SEAL"
	 	  And I am in the index page
	 	  And I logout
	 
	 Scenario: Change password and see the page of serializer of mail pending to send from the change
		Given Student "martin" exists with password "martin"
	 	  And I log in as "martin" "martin"
		 When I click in the "Change Password" link	
		  And I fill the change password form with user "martin", oldpass "martin", newpass "mauro", newpassagin "mauro"
		  And I submit the form
		  And I am in the index page
		  And I logout
  	      And I log in as "seal" "seal"
	 	  And I click in the "Mails to send Serializer" link
	 	 Then I should see "Cambio de password en SEAL"
	 	  And I am in the index page
	 	  And I logout