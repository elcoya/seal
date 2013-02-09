Feature: As a user I want to see a script list serializer

	 Scenario: See a script serializer from administrator index page
	 	Given course "2012-1" exists
    	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
          And script "successfull_test_script.sh" is set for practice "TP Intro" for course "2012-1"
         when I log in as "seal" "seal"
	 	  And I click in the "Script Serializer" link
	 	 Then I should see "successfull_test_script.sh"
	 	  And I am in the index page
	 	  And I logout