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
   
    Scenario: Upload a new delivery leaving it pending
        Given course "2012-1" exists
          And Student "student" exists with password "student"
          And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
          And there are no deliveries
         When I create a new delivery for practice "TP Intro" and course "2012-1" from Student "student"
         Then delivery for practice "TP Intro" and course "2012-1" from Student "student" should have status "pending"
   
    Scenario: Run the Autocheck for the deliveries
        Given course "2012-1" exists
          And Student "student" exists with password "student"
          And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
          And script "successfull_test_script.sh" is set for practice "TP Intro" for course "2012-1"
          And there are no deliveries
         When I create a new delivery for practice "TP Intro" and course "2012-1" from Student "student"
          And I run the Autocheck process
         Then delivery for practice "TP Intro" and course "2012-1" from Student "student" should have status "successfull"
         
    Scenario: As a teacher browse the results of an automatic check
    	Given Teacher "teacher" exists with password "teacher"
    	  And Student "student" exists with password "student"
    	  And course "2012-1" exists
    	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
          And script "successfull_test_script.sh" is set for practice "TP Intro" for course "2012-1"
          And a delivery exists for practice "TP Intro" and course "2012-1" from Student "student"
          And autocheck process is run
          And I log in as "teacher" "teacher"
         When I create a new delivery for practice "TP Intro" and course "2012-1" from Student "student"
          And I run the Autocheck process
          And I am in the list page of delivery from "TP Intro"
          And I click in the "successfull" link
         Then I should see "this is the successfull bash script."
          And I should see "Automatic check result: successfull"
