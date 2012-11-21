Feature: As a Student I should be able to upload my deliveries and trigger the automatic correction

	Scenario: Upload a script for a practice
    	Given Teacher "teacher" exists with password "teacher"
    	  And I log in as "teacher" "teacher"
    	  And course "2012-1" exists
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And I am at the upload script form for practice "TP Intro" and course "2012-1"
	 	 When I fill in the upload script form with the file "successfull_test_script.sh"
	 	  And I submit the form
	 	 Then I should see pattern "successfull_test_script(_[0-9]+)?.sh"
	
