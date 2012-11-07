Feature: As a student I want to see my corrections


	Scenario: No correction yet
		Given course "2012-1" exists 
	 	  And user "Martin" is registered
	 	  And student "Martin" exists in course "2012-1"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And exist delivery of "TP Intro" from student "Martin" whit dalivery date "2012-11-01"
	 	  And there are no corrections
	 	 When I am in the correction consult page of delivery from student "Martin" and practice "TP Intro"
	 	 Then I should see "There is yet no Correction"
	 	 

	Scenario: Student only see a public coment and note of correction
		Given course "2012-1" exists 
	 	  And user "Martin" is registered
	 	  And student "Martin" exists in course "2012-1"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And exist delivery of "TP Intro" from student "Martin" whit dalivery date "2012-11-01"
	 	  And exist correction of delivery of "Martin" for "TP Intro" with "Public Coment" "Private Coment" "4.0"
	 	 When I am in the correction consult page of delivery from student "Martin" and practice "TP Intro"
	 	 Then I should see "Public Coment" and "4.0"
	