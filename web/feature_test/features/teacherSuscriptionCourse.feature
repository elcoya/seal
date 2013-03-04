Feature: As a teacher I want to administrate de suscription

	Scenario: See the link to list de suscrption in de edit course page
	   Given Teacher "teacher" exists with password "teacher"
	     And I log in as "teacher" "teacher"
    	 And course "2012-1" exists
    	When I am in the modifier page of course "2012-1"
    	Then I should see link to "Suscription" in the list
	
	Scenario: See the list of suscription empty
	   Given Teacher "teacher" exists with password "teacher"
         And I log in as "teacher" "teacher"
    	 And course "2012-1" exists
    	 And there are no suscription
		When I am in the suscription list page of course "2012-1"
        Then I should see "There are yet no suscriptions for this course"
         And I should see "There are yet no suscriptions solve for this course"  

	Scenario: See the list of old suscription order by suscription date
	   Given Teacher "teacher" exists with password "teacher"
         And student "martin" exists with password "martin"
         And I log in as "teacher" "teacher"
    	 And course "2012-1" exists
		 And there are no suscription
		 And existe suscrition of student "martin" for course "2012-1" with suscription date "2012-11-01" and state "Pending"
		 And existe suscrition of student "martin" for course "2012-1" with suscription date "2012-11-02" and state "Pending"
	    When I am in the suscription list page of course "2012-1"
        Then I should see "Nov. 1, 2012" before "Nov. 2, 2012" 
        
    Scenario: Accept suscription
	   Given Teacher "teacher" exists with password "teacher"
         And student "martin" exists with password "martin"
         And I log in as "teacher" "teacher"
         And course "2012-1" exists
		 And there are no suscription
		 And existe suscrition of student "martin" for course "2012-1" with suscription date "2012-11-01" and state "Pending"
		When I am in the suscription list page of course "2012-1"
		 And I check the suscription of student "martin" for course "2012-1"
		 And I click the button "Accept"
        Then I should see "Accept"     
        
    Scenario: Reject suscription  
       Given Teacher "teacher" exists with password "teacher"
         And student "martin" exists with password "martin"
         And I log in as "teacher" "teacher"
         And course "2012-1" exists
		 And there are no suscription
		 And existe suscrition of student "martin" for course "2012-1" with suscription date "2012-11-01" and state "Pending"
		When I am in the suscription list page of course "2012-1"
 		 And I check the suscription of student "martin" for course "2012-1"
		 And I click the button "Reject"
        Then I should see "Reject"     

	Scenario: Accept Suscription and see a course in de home page of student
	   Given Teacher "teacher" exists with password "teacher"
         And student "martin" exists with password "martin"
         And I log in as "teacher" "teacher"
         And course "2012-1" exists
		 And there are no suscription
		 And existe suscrition of student "martin" for course "2012-1" with suscription date "2012-11-01" and state "Pending"
		When I am in the suscription list page of course "2012-1"
		 And I check the suscription of student "martin" for course "2012-1"
		 And I click the button "Accept"
		 And I click in the "logout" link
         And I log in as "martin" "martin"
        Then I should see "There are yet no Practices"