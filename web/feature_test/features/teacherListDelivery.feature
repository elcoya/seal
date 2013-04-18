Feature: As a teacher I want to see the delivery lists of one practice

	Scenario: No delivery from one practice
	    Given Teacher "teacher" exists with password "teacher"
	      And course "2012-1" exists
          And I log in as "teacher" "teacher"
          And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-02"
          And there are no deliveries
         When I am in the list page of delivery from "TP Intro" of course "2012-1"
         Then I should see "There are yet no deliveries"   
         
    Scenario: Delivery list order by date of the delivery
    	Given Teacher "teacher" exists with password "teacher"
    	  And course "2012-1" exists
          And I log in as "teacher" "teacher"
    	  And a shift with name "tarde" and description "horario" in the course "2012-1"
          And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-02"
          And Student "martin" exists with password "martin"	
          And student "martin" exists in course "2012-1" and in shift "tarde"
          And exist delivery of "TP Intro" from student "martin" whit dalivery date "2012-11-01"
		  And exist delivery of "TP Intro" from student "martin" whit dalivery date "2012-11-02"		
		 When I am in the list page of delivery from "TP Intro" of course "2012-1"
         Then I should see "Nov. 1, 2012" before "Nov. 2, 2012"  