Feature: As a user I want to see the student list
    
    Scenario: No student in course 2012-1
        Given Teacher "teacher" exists with password "teacher"
          And course "2012-1" exists
          And there are no student in "2012-1"
          And I log in as "teacher" "teacher"
         When I click in the "2012-1" link
         Then I should see "There are yet no Students"
    
	Scenario: Student in course 2012-1 order by name
        Given Teacher "teacher" exists with password "teacher"
          And I log in as "teacher" "teacher"
          And course "2012-1" exists
          And Student "martin" exists with password "martin"
          And Student "anibal" exists with password "anibal"
          And student "martin" exists in course "2012-1"
          And student "anibal" exists in course "2012-1"
         when I am in the modifier page of course "2012-1"
         Then I should see "anibal" before "martin" 