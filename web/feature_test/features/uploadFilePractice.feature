Feature: As a teacher I want to manage several practice files

	 Scenario: No file upload
	 	Given course "2012-1" exists 
	 	  And there are no practices
	 	  And Teacher "teacher" exists with password "teacher"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And I log in as "teacher" "teacher"
	 	 When I click the button "uploadfileTP Intro"
	 	 Then I should see "There are yet no deliveries uploaded to this practice"

	 Scenario: Upload file
		Given course "2012-1" exists 
	 	  And there are no practices
	 	  And Teacher "teacher" exists with password "teacher"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And I log in as "teacher" "teacher"
	 	 When I click the button "uploadfileTP Intro"
	 	  And I fill the upload file form with name "enunciado"
	 	  And I submit the form
	 	 Then I should see "enunciado"
	 
	 Scenario: Delete file
		Given course "2012-1" exists 
	 	  And there are no practices
	 	  And Teacher "teacher" exists with password "teacher"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And I log in as "teacher" "teacher"
	 	 When I click the button "uploadfileTP Intro"
	 	  And I fill the upload file form with name "enunciado"
	 	  And I submit the form
	 	  And I click the button "deleteenunciado"
	 	 Then I should see "There are yet no deliveries uploaded to this practice"
	
	Scenario: See the option edit when i upload a text file
		Given course "2012-1" exists 
	 	  And there are no practices
	 	  And Teacher "teacher" exists with password "teacher"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And text file is bound to practice "TP Intro" with id "1"
	 	  And I log in as "teacher" "teacher"
	 	 When I click the button "uploadfileTP Intro"
	 	 Then I should see the link to edit file with id "1"

	Scenario: Not see the option edit when i upload a not text file
		Given course "2012-1" exists 
	 	  And there are no practices
	 	  And Teacher "teacher" exists with password "teacher"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And not text file is bound to practice "TP Intro" with id "1"
	 	  And I log in as "teacher" "teacher"
	 	 When I click the button "uploadfileTP Intro"
	 	 Then I should not see the link to edit file with id "1"

