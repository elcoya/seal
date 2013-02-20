Feature: As a student I want to see my corrections


	Scenario: No correction yet
		Given course "2012-1" exists 
	 	  And Student "martin" exists with password "martin"
	 	  And student "martin" exists in course "2012-1"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And exist delivery of "TP Intro" from student "martin" whit dalivery date "2012-11-01"
	 	  And there are no corrections
	 	  And I log in as "martin" "martin"
	 	 When I am in the correction consult page of delivery from student "martin" and practice "TP Intro"
	 	 Then I should see "There is yet no Correction"
	 	 

	Scenario: Student only see a public coment and grade of correction
		Given course "2012-1" exists 
	 	  And Student "martin" exists with password "martin"
	 	  And student "martin" exists in course "2012-1"
	 	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
	 	  And exist delivery of "TP Intro" from student "martin" whit dalivery date "2012-11-01"
	 	  And exist correction of delivery of "martin" for "TP Intro" with "Public Coment" "Private Coment" "4.0"
	 	  And I log in as "martin" "martin"
	 	 When I am in the correction consult page of delivery from student "martin" and practice "TP Intro"
	 	 Then I should see "Public Coment" and "4.0"
	 	  And I should not see "Private Coment"
	