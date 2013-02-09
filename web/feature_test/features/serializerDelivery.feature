Feature: As a user I want to see a delivery list serializer

	 Scenario: See a delivery serializer from administrator index page
	 	Given Student "martin" exists with email "martin@foo.foo"
	 	  And course "2012-1" exists
	 	  And student "Martin" exists in course "2012-1"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And exist delivery of "TP Intro" from student "Martin" whit dalivery date "2012-11-01"
	 	 when I log in as "seal" "seal"
	 	  And I click in the "Delivery Serializer" link
	 	 Then I should see "2012-11-01"
	 	  And I am in the index page
	 	  And I logout