Feature: As a student I want to see de courses where i am enrolled and the practices of this courses 

 	Scenario: No Course Enrolled
 		Given Student "martin" exists with password "martin"
 		  And course "2012-1" exists
 		  And a shift with name "tarde" and description "horario" in the course "2012-1"
 		  And student "martin" exists without course
          And I log in as "martin" "martin"
          And I wait
 		 Then I should see "There are yet no Shifts to suscribe to"
 
	Scenario: Enrolled in two courses, order by newest course
		Given Student "martin" exists with password "martin"
    	  And course "2012-1" exists
		  And course "2011-2" exists
		  And a shift with name "tarde" and description "horario" in the course "2012-1"
		  And a shift with name "tarde" and description "horario" in the course "2011-2"
		  And student "martin" exists in course "2012-1" shift "tarde" and in course "2011-2" shift "tarde" 
          And I log in as "martin" "martin"
		 Then I should see "2012-1-tarde" before "2011-2-tarde" 
 		  
	Scenario: List practices of enrroles course without practice
		Given Student "martin" exists with password "martin"
    	  And course "2012-1" exists
		  And a shift with name "tarde" and description "horario" in the course "2012-1"
		  And student "martin" exists in course "2012-1" and in shift "tarde"
          And I log in as "martin" "martin"
		 Then I should see "There are yet no Practices" 
		 
	Scenario: List practices of enrroles course with 2 practices order by deadline 
		Given Student "martin" exists with password "martin"
    	  And course "2012-1" exists
    	  And a shift with name "tarde" and description "horario" in the course "2012-1"
		  And student "martin" exists in course "2012-1" and in shift "tarde"
          And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And practice "TP 1" exists in course "2012-1" with deadline "2012-12-02"
	 	  And I log in as "martin" "martin"
		 Then I should see "TP Intro" before "TP 1"	 

