Feature: As a student I want to aplicate to a course

	Scenario: See the link to aplicate in de homte page of student
	   Given student "martin" exists with password "martin"
		 And I log in as "martin" "martin"
		then I should see link to "Suscription" in the list
	
	Scenario: See the list of course to suscribe
	   Given student "martin" exists with password "martin"
	     And course "2012-1" exists
		 And I log in as "martin" "martin"
	    When I click in the "Suscription" link
        Then I should see "2012-1"  	 
	
	Scenario: See the list of old suscription empty
	   Given student "martin" exists with password "martin"
		 And I log in as "martin" "martin"
		 And course "2012-1" exists
		 And there are no suscription
		When I click in the "Suscription" link
        Then I should see "There are no old suscription"  

	Scenario: See the list of old suscription order by suscription date
	   Given student "martin" exists with password "martin"
		 And I log in as "martin" "martin"
		 And course "2012-1" exists
		 And existe suscrition of student "martin" for course "2012-1" with suscription date "2012-11-01"
		 And existe suscrition of student "martin" for course "2012-1" with suscription date "2012-11-02" 
	    When I click in the "Suscription" link
        Then I should see "Nov. 1, 2012" before "Nov. 2, 2012"  