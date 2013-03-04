Feature: As a student I want to aplicate to a course

	Scenario: See the link to aplicate in de homte page of student
	   Given student "martin" exists with password "martin"
		 And I log in as "martin" "martin"
		then I should see link to "Suscription" in the list
	
	Scenario: No course for suscribe
	   Given student "martin" exists with password "martin"
	     And there are no courses
		 And I log in as "martin" "martin"
	    When I click in the "Suscription" link
        Then I should see "There are yet no Course to suscribe"  	 
	
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

	Scenario: Make a suscription
	   Given student "martin" exists with password "martin"
	     And course "2012-1" exists
		 And I log in as "martin" "martin"
	     And there are no suscription	
	    When I click in the "Suscription" link
         And I click in the "Suscribe" link 
        Then I should see "Pending"  	
		
	Scenario: See the list of old suscription order by suscription date
	   Given student "martin" exists with password "martin"
		 And I log in as "martin" "martin"
		 And course "2012-1" exists
		 And there are no suscription
		 And existe suscrition of student "martin" for course "2012-1" with suscription date "2012-11-01" and state "Pending"
		 And existe suscrition of student "martin" for course "2012-1" with suscription date "2012-11-02" and state "Pending"
	    When I click in the "Suscription" link
        Then I should see "Nov. 1, 2012" before "Nov. 2, 2012" 
        
    Scenario: See the list of accept suscription
	   Given student "martin" exists with password "martin"
		 And I log in as "martin" "martin"
		 And course "2012-1" exists
		 And there are no suscription
		 And existe suscrition of student "martin" for course "2012-1" with suscription date "2012-11-01" and state "Accept"
		When I click in the "Suscription" link
        Then I should see "Accept"     
        
    Scenario: See the list of reject suscription  
       Given student "martin" exists with password "martin"
		 And I log in as "martin" "martin"
		 And course "2012-1" exists
		 And there are no suscription
		 And existe suscrition of student "martin" for course "2012-1" with suscription date "2012-11-01" and state "Reject"
		When I click in the "Suscription" link
        Then I should see "Reject"
        
    Scenario: Suscribe and desapear de course, unique suscribe pending for course
       Given student "martin" exists with password "martin"
		 And there are no courses
		 And I log in as "martin" "martin"
		 And course "2012-1" exists
		 And there are no suscription
		 And existe suscrition of student "martin" for course "2012-1" with suscription date "2012-11-01" and state "Pending"
		When I click in the "Suscription" link
		Then I should see "There are yet no Course to suscribe"     
    
    Scenario: Student enroled in the only course, no courses to sucribe  
       Given student "martin" exists with password "martin"
		 And there are no courses
		 And course "2012-1" exists
		 And student "martin" exists in course "2012-1"
		 And I log in as "martin" "martin" 
		When I click in the "Home" link
		 And I click in the "Suscription" link
		Then I should see "There are yet no Course to suscribe" 