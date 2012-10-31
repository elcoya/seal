Feature: As a teacher I want to create a practice

	 Scenario: Create Practice
	 	Given there are no practices
          And I am at the new practice form
         When I fill the practice form with default data
          And I submit the form
         Then I should see "The list with a new practice"
         
	Scenario: Create Practice with equal id in diferent course
		 Given course "2012-1" exists
		   And course "2012-2" exists
		   And practice "1" in "2012-1"
		  when I am at the new practice form
		   And I fill the practice form with id "1" and default data
		  Then I shoul see "The list with a new practice"
