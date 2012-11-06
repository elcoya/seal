Feature: As a student I want to see my deliveries
   
    Scenario: List Delivery of Practices from home student when there are not delivery
    	Given course "2012-1" exists
    	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
    	  And student "Martin" exists in course "2012-1"
    	 when I am in the delivery page of student "Martin" and practice "TP INTRO"
    	 Then I should see "There are yet no Delivery from this practice"
    	 
  	Scenario: List Delivery of Practices order by delivery date
  		Given course "2012-1" exists
  		  And student "Martin" exists in course "2012-1"
    	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
    	  And exist delivery of "TP Intro" from student "Martin" whit dalivery date "2012-11-01"
		  And exist delivery of "TP Intro" from student "Martin" whit dalivery date "2012-11-02"
		 when I am in the delivery page of student "Martin" and practice "TP INTRO"
    	 Then I should see "Nov. 1, 2012" before "Nov. 2, 2012" 