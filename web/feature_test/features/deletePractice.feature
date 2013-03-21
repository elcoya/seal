Feature: As a teacher I would like to eliminate a practice if delivery is not associated

	 Scenario: Delete Practice whitout deliveries
	 	Given Teacher "teacher" exists with password "teacher"
          And course "2012-1" exists
          And practice "TP Intro" exists in course "2012-1" with deadline "2013-04-01"
    	  And there are no deliveries
          And I log in as "teacher" "teacher"
         When I am in the detail page of course "2012-1"
          And I click the button "deleteTP Intro"
         Then I should not see "TP Intro" 
	
	Scenario: No button Delete in the practices with delivery
	 	Given Teacher "teacher" exists with password "teacher"
          And Student "martin" exists with password "martin"
          And course "2012-1" exists
          And a shift with name "tarde" and description "horario" in the course "2012-1"
          And student "martin" exists in course "2012-1" and in shift "tarde"
          And practice "TP Intro" exists in course "2012-1" with deadline "2013-04-01"
    	  And exist delivery of "TP Intro" from student "martin" whit dalivery date "2012-11-01"
    	  And I log in as "teacher" "teacher"
         When I am in the detail page of course "2012-1"
         Then I should not see the button "deleteTP Intro"
	
	