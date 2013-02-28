Feature: As a Teacher I should be able to edit text the files uploaded, bounded to a practice

    Scenario: As a teacher I must see a link to edit files uploaded to the practice when are text files
        Given Teacher "teacher" exists with password "teacher"
          And course "2013-1" exists
          And practice "TP Intro" exists in course "2013-1" with deadline "2013-04-01"
          And text file is bound to practice "TP Intro" with id "1"
          And I log in as "teacher" "teacher"
         When I am at the list files page for practice "TP Intro"
         Then I should see a link to "/teacher/practices/editfile/1"

    Scenario: As a teacher I must be able to edit any text file bound to a delivery
        Given Teacher "teacher" exists with password "teacher"
          And course "2013-1" exists
          And practice "TP Intro" exists in course "2013-1" with deadline "2013-04-01"
          And text file is bound to practice "TP Intro" with id "1"
          And I log in as "teacher" "teacher"
         When I am at the edit text file page for practice "TP Intro"
         Then I should see "first line"
          And I should see "second line"
          And I should see "third line"
          And I should see "fourth line"
          And I should see "fifth line"

    Scenario: 
        Given Teacher "teacher" exists with password "teacher"
          And course "2013-1" exists
          And practice "TP Intro" exists in course "2013-1" with deadline "2013-04-01"
          And text file is bound to practice "TP Intro" with id "1"
          And I log in as "teacher" "teacher"
         When I am at the edit text file page for practice "TP Intro"
          And I edit the practice text file in the form
          And I submit the form
         Then I should see "Edited successfully"
          And I should see "only line"

