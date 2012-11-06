Feature: As a user I want to see the student list
    
    Scenario: No student in course 2012-1
        Given course "2012-1" exists
          And there are no student in "2012-1"
          And I am in the index page
         When I click in the "2012-1" link
         Then I should see "There are yet no Students"
    
	Scenario: Student in course 2012-1 order by name
        Given course "2012-1" exists
          And user "Martin" is registered
          And user "Anibal" is registered
          And student "Martin" exists in course "2012-1"
          And student "Anibal" exists in course "2012-1"
         when I am in the modifier page of course "2012-1"
         Then I should see "Anibal" before "Martin" 