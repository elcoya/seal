Feature: As a teacher I want to see the suscription pending list with link in navigator bar

	Scenario: No suscription pending
	 	Given Teacher "teacher" exists with password "teacher"
          And I log in as "teacher" "teacher" 
         When I click in the "Pending Subscriptions" link
		 Then I should see "There are no suscription pending"

	Scenario: List Suscription pending
	   Given Teacher "teacher" exists with password "teacher"
         And student "martin" exists with password "martin"
         And course "2012-1" exists
		 And a shift with name "tarde" and description "horario" in the course "2012-1"
		 And there are no suscription
		 And existe suscrition of student "martin" for course "2012-1" shift "tarde" with suscription date "2012-11-01" and state "Pending"
		 And I log in as "teacher" "teacher"
	    When I click in the "Pending Subscriptions" link
		Then I should see "Nov. 1, 2012"
        
	Scenario: Resolve Suscription and desapear in the list		
	   Given Teacher "teacher" exists with password "teacher"
         And student "martin" exists with password "martin"
         And course "2012-1" exists
		 And a shift with name "tarde" and description "horario" in the course "2012-1"
		 And there are no suscription
		 And existe suscrition of student "martin" for course "2012-1" shift "tarde" with suscription date "2012-11-01" and state "Pending"
		 And I log in as "teacher" "teacher"
	    When I click in the "Pending Subscriptions" link
		 And I click in the "Resolve" link
		 And I check the suscription of student "martin" for course "2012-1" shift "tarde"
		 And I click the button "Accept"
		 And I click in the "Pending Subscriptions" link
		Then I should see "There are no suscription pending"
        