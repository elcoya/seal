Feature: As a teacher I want to manage several practice files

	 Scenario: No file upload
	 	Given course "2012-1" exists 
	 	  And there are no practices
	 	  And Teacher "teacher" exists with password "teacher"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And I log in as "teacher" "teacher"
	 	 When I click in the "2012-1" link
	 	  And I click in the "Upload Files" link
	 	 Then I should see "There are yet no Files in this Practice"

	 Scenario: Upload file
		Given course "2012-1" exists 
	 	  And there are no practices
	 	  And Teacher "teacher" exists with password "teacher"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And I log in as "teacher" "teacher"
	 	 When I click in the "2012-1" link
	 	  And I click in the "Upload Files" link
	 	  And I fill the upload file form with name "enunciado"
	 	  And I submit the form
	 	 Then I should see "enunciado"
	 
	 Scenario: Delete file
		Given course "2012-1" exists 
	 	  And there are no practices
	 	  And Teacher "teacher" exists with password "teacher"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And I log in as "teacher" "teacher"
	 	 When I click in the "2012-1" link
	 	  And I click in the "Upload Files" link
	 	  And I fill the upload file form with name "enunciado"
	 	  And I submit the form
	 	  And I click in the "Delete" link
	 	 Then I should see "There are yet no Files in this Practice"
	
	Scenario: See the option edit when i upload a text file
		Given course "2012-1" exists 
	 	  And there are no practices
	 	  And Teacher "teacher" exists with password "teacher"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And text file is bound to practice "TP Intro" with id "1"
	 	  And I log in as "teacher" "teacher"
	 	 When I click in the "2012-1" link
	 	  And I click in the "Upload Files" link
	 	 Then I should see "Edit"

	Scenario: Not see the option edit when i upload a not text file
		Given course "2012-1" exists 
	 	  And there are no practices
	 	  And Teacher "teacher" exists with password "teacher"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And not text file is bound to practice "TP Intro" with id "1"
	 	  And I log in as "teacher" "teacher"
	 	 When I click in the "2012-1" link
	 	  And I click in the "Upload Files" link
	 	 Then I should not see "Edit"
	 	  And I should see "Non-editable"

