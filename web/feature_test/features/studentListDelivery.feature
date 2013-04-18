Feature: As a student I want to see my deliveries
   
    Scenario: List Delivery of Practices from home student when there are not delivery
    	Given Student "martin" exists with password "martin"
          And course "2012-1" exists
          And a shift with name "tarde" and description "horario" in the course "2012-1"
    	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
    	  And student "martin" exists in course "2012-1" and in shift "tarde"
    	  And I log in as "martin" "martin"	
    	 when I am in the delivery page of practice "TP Intro"
    	 Then I should see "There are yet no deliveries from this practice"
    	 
  	Scenario: List Delivery of Practices order by delivery date
  		Given Student "martin" exists with password "martin"
          And course "2012-1" exists
          And a shift with name "tarde" and description "horario" in the course "2012-1"
    	  And student "martin" exists in course "2012-1" and in shift "tarde"
    	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
    	  And exist delivery of "TP Intro" from student "martin" whit dalivery date "2012-11-01"
		  And exist delivery of "TP Intro" from student "martin" whit dalivery date "2012-11-02"
		  And I log in as "martin" "martin"	
		 when I am in the delivery page of practice "TP Intro"
    	 Then I should see "Nov. 2, 2012" before "Nov. 1, 2012" 