Feature: As a user I want to see a serializer of the list of practice

	 Scenario: See a practice serializer from administrator index page
	 	Given course "2012-1" exists 
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	 when I log in as "seal" "seal"
	 	  And I click in the "Practice Serializer" link
	 	 Then I should see "TP Intro"
	 	  And I am in the index page
	 	  And I logout