Feature: As a user I want to see the practice list
    
    Scenario: No practice
        Given Teacher "teacher" exists with password "teacher"
          And there are no practices
    	  And course "2012-1" exists
          And I log in as "teacher" "teacher"
         Then I should see "There are no practices"
         
    Scenario: Practices in course 2012-1 order by Dead Line
        Given Teacher "teacher" exists with password "teacher"
    	  And course "2012-1" exists
          And practice "TP 1" exists in course "2012-1" with deadline "2012-12-02"
          And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
          And I log in as "teacher" "teacher"
         Then I should see "TP Intro"
          And I should see "TP 1"
         
    Scenario: List Delivery of Practices from home student
        Given Student "martin" exists with password "martin"
    	  And course "2012-1" exists
    	  And a shift with name "tarde" and description "horario" in the course "2012-1"
    	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
          And I log in as "martin" "martin"
    	  And student "martin" exists in course "2012-1" and in shift "tarde"
    	 when I am in the delivery page of practice "TP Intro"
    	 Then I should see "There are yet no deliveries from this practice"
