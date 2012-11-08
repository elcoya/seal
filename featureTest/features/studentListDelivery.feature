Feature: As a student I want to see my deliveries
   
    Scenario: List Delivery of Practices from home student when there are not delivery
    	Given Student "martin" exists with password "martin"
          And I log in as "martin" "martin"
    	  And course "2012-1" exists
    	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
    	  And student "martin" exists in course "2012-1"
    	 when I am in the delivery page of practice "TP INTRO"
    	 Then I should see "There are yet no Delivery from this practice"
    	 
  	Scenario: List Delivery of Practices order by delivery date
  		Given Student "martin" exists with password "martin"
          And I log in as "martin" "martin"
    	  And course "2012-1" exists
  		  And student "martin" exists in course "2012-1"
    	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
    	  And exist delivery of "TP Intro" from student "martin" whit dalivery date "2012-11-01"
		  And exist delivery of "TP Intro" from student "martin" whit dalivery date "2012-11-02"
		 when I am in the delivery page of practice "TP INTRO"
    	 Then I should see "Nov. 1, 2012" before "Nov. 2, 2012" 