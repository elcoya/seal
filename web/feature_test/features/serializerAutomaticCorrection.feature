Feature: As a user I want to see a Automatic Correction Pending list serializer

	 Scenario: See a automatic correction serializer from administrator index page
	 	Given Student "martin" exists with email "martin@foo.foo"
	 	  And course "2012-1" exists
	 	  And student "martin" exists in course "2012-1"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And a delivery exists for practice "TP Intro" and course "2012-1" from Student "martin"
	 	 when I log in as "seal" "seal"
	 	  And I click in the "Automatic Correction Serializer" link
	 	 Then I should see "delivery"
	 	 