Feature: As a student I want to aplicate to a course

	Scenario: See the link to aplicate in de homte page of student
	   Given student "martin" exists with password "martin"
		 And I log in as "martin" "martin"
		then I should see link to "Subscription" in the list
	
	Scenario: No course for suscribe
	   Given student "martin" exists with password "martin"
	     And there are no courses
	     And there are no shifts
		 And I log in as "martin" "martin"
	    When I am in the student suscription page
        Then I should see "There are yet no Shifts to suscribe"  	 
	
	Scenario: See the list of course to suscribe
	   Given student "martin" exists with password "martin"
	     And there are no courses
	     And there are no shifts
	     And course "2012-1" exists
		 And a shift with name "tarde" and description "horario" in the course "2012-1"
		 And I log in as "martin" "martin"
	    When I am in the student suscription page
        Then I should see "2012-1-tarde"  	 
	
	Scenario: See the list of old suscription empty
	   Given student "martin" exists with password "martin"
		 And there are no suscription
		 And I log in as "martin" "martin"
		When I am in the student suscription page
        Then I should see "There are no old suscription"  

	Scenario: Make a suscription
	   Given student "martin" exists with password "martin"
	     And there are no courses
	     And there are no shifts
	     And course "2012-1" exists
		 And a shift with name "tarde" and description "horario" in the course "2012-1"
	     And there are no suscription	
	     And I log in as "martin" "martin"
	    When I am in the student suscription page
         And I click in the "Suscribe" link 
        Then I should see "Pending"  	
		
	Scenario: See the list of old suscription order by suscription date
	   Given student "martin" exists with password "martin"
		 And there are no courses
	     And there are no shifts
		 And course "2012-1" exists
		 And course "2013-1" exists
		 And a shift with name "tarde" and description "horario" in the course "2012-1"
		 And a shift with name "noche" and description "horario" in the course "2013-1"
		 And there are no suscription
		 And existe suscrition of student "martin" for course "2012-1" shift "tarde" with suscription date "2012-11-01" and state "Pending"
		 And existe suscrition of student "martin" for course "2013-1" shift "noche" with suscription date "2013-11-02" and state "Pending"
	     And I log in as "martin" "martin"
	    When I am in the student suscription page
        Then I should see "Nov. 1, 2012" before "Nov. 2, 2013" 
        
    Scenario: See the list of accept suscription
	   Given student "martin" exists with password "martin"
		 And there are no courses
	     And there are no shifts
		 And course "2012-1" exists
		 And a shift with name "tarde" and description "horario" in the course "2012-1"
		 And there are no suscription
		 And existe suscrition of student "martin" for course "2012-1" shift "tarde" with suscription date "2012-11-01" and state "Accept"
		 And I log in as "martin" "martin"
		When I am in the student suscription page
        Then I should see "Accept"     
        
    Scenario: See the list of reject suscription  
       Given student "martin" exists with password "martin"
		 And there are no courses
	     And there are no shifts
		 And course "2012-1" exists
		 And a shift with name "tarde" and description "horario" in the course "2012-1"
		 And there are no suscription
		 And existe suscrition of student "martin" for course "2012-1" shift "tarde" with suscription date "2012-11-01" and state "Reject"
		 And I log in as "martin" "martin"
		When I am in the student suscription page
        Then I should see "Reject"
        
    Scenario: Suscribe and desapear de course and shift, unique suscribe pending for course
       Given student "martin" exists with password "martin"
		 And there are no courses
		 And there are no shifts
		 And course "2012-1" exists
		 And a shift with name "tarde" and description "horario" in the course "2012-1"
		 And a shift with name "noche" and description "horario" in the course "2012-1"
		 And there are no suscription
		 And existe suscrition of student "martin" for course "2012-1" shift "tarde" with suscription date "2012-11-01" and state "Pending"
		 And I log in as "martin" "martin"
		When I am in the student suscription page
		Then I should see "There are yet no Shifts to suscribe"     
    
    Scenario: Student enroled in the only course, no courses to sucribe  
       Given student "martin" exists with password "martin"
		 And there are no courses
		 And there are no shifts
		 And course "2012-1" exists
		 And a shift with name "tarde" and description "horario" in the course "2012-1"
		 And student "martin" exists in course "2012-1" and in shift "tarde"
		 And I log in as "martin" "martin" 
		When I am in the student suscription page
		Then I should see "There are yet no Shifts to suscribe" 
