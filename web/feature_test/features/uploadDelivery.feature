Feature: As a student I want to upload a delivery

	 Scenario: Upload Delivery
	 	Given course "2012-1" exists 
	 	  And a inning with name "tarde" and description "horario" in the course "2012-1"
	 	  And Student "martin" exists with password "martin"
	 	  And student "martin" exists in course "2012-1" and in inning "tarde"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And I log in as "martin" "martin"
         When I am in the upload page of practice "TP Intro"
          And I fill the delivery form with default data
          And I submit the form
		 Then I should see the delivery in the list
