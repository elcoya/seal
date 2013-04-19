Feature: As a teacher I want to see the list of the student without delivery successfull

	Scenario: No student without delivery pending
	 	Given Teacher "teacher" exists with password "teacher"
          And course "2012-1" exists
          And I log in as "teacher" "teacher" 
         When I am in the page of delivery pending of course "2012-1"
		 Then I should see "There are no student with pending delivery"
	
	Scenario: List Student without delivery
		Given Student "martin" exists with email "martin@foo.foo"
		  And Teacher "teacher" exists with password "teacher"
	 	  And course "2012-1" exists
	 	  And a shift with name "tarde" and description "horario" in the course "2012-1"
	 	  And student "martin" exists in course "2012-1" and in shift "tarde"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And I log in as "teacher" "teacher"
 		 When I am in the page of delivery pending of course "2012-1"
	 	 Then I should see "martin"	 
	
	Scenario: List Student with delivery and automatic correction state failed 
		Given Student "martin" exists with email "martin@foo.foo"
		  And Teacher "teacher" exists with password "teacher"
	 	  And course "2012-1" exists
	 	  And a shift with name "tarde" and description "horario" in the course "2012-1"
	 	  And student "martin" exists in course "2012-1" and in shift "tarde"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And a delivery exists for practice "TP Intro" and course "2012-1" from Student "martin" with id "1"
	 	  And the automatic correction of delivery with id "1" is "failed"
	 	  And I log in as "teacher" "teacher" 
	 	 When I am in the page of delivery pending of course "2012-1"
	 	 Then I should see "martin"
    
    Scenario: No List Student with delivery and automatic correction statsu successfull 
		Given Student "martin" exists with email "martin@foo.foo"
		  And Teacher "teacher" exists with password "teacher"
	 	  And course "2012-1" exists
	 	  And a shift with name "tarde" and description "horario" in the course "2012-1"
	 	  And student "martin" exists in course "2012-1" and in shift "tarde"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And a delivery exists for practice "TP Intro" and course "2012-1" from Student "martin" with id "1"
	 	  And the automatic correction of delivery with id "1" is "successfull"
	 	  And I log in as "teacher" "teacher" 
	 	 When I am in the page of delivery pending of course "2012-1"
	 	 Then I should see "There are no student with pending delivery"

    Scenario: List Student with delivery and automatic correction status fail and not list a student with automtaci correction status successfull 
		Given Student "martin" exists with email "martin@foo.foo"
		  And Student "anibal" exists with email "anibal@foo.foo"
		  And Teacher "teacher" exists with password "teacher"
	 	  And course "2012-1" exists
	 	  And a shift with name "tarde" and description "horario" in the course "2012-1"
	 	  And student "martin" exists in course "2012-1" and in shift "tarde"
	 	  And student "anibal" exists in course "2012-1" and in shift "tarde"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And a delivery exists for practice "TP Intro" and course "2012-1" from Student "martin" with id "1"
	 	  And the automatic correction of delivery with id "1" is "successfull"
	 	  And a delivery exists for practice "TP Intro" and course "2012-1" from Student "anibal" with id "2"
	 	  And the automatic correction of delivery with id "2" is "failed"
	 	  And I log in as "teacher" "teacher" 
	 	 When I am in the page of delivery pending of course "2012-1"
	     Then I should see "anibal"
	 	  And I should not see "martin"
	 	   
	  