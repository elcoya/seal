Feature: As a Teacher I should be able to see de automatic correction result

    Scenario: Upload a script for a practice
        Given Teacher "teacher" exists with password "teacher"
          And I log in as "teacher" "teacher"
          And course "2012-1" exists
          And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
          And I am at the upload script form for practice "TP Intro" and course "2012-1"
         When I fill in the upload script form with the file "successfull_test_script.sh"
          And I submit the form
          And I click the button "uploadsriptTP Intro"
         Then I should see pattern "successfull_test_script(_[0-9]+)?.sh"
   
    Scenario: As a teacher browse the results of an automatic check
    	Given Teacher "teacher" exists with password "teacher"
    	  And Student "student" exists with password "student"
    	  And course "2012-1" exists
    	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
          And script "successfull_test_script.sh" is set for practice "TP Intro" for course "2012-1"
          And a delivery exists for practice "TP Intro" and course "2012-1" from Student "student" with id "1"
          And automatic_correction for all deliveries has status "successfull"
          And automatic_correction for all deliveries has stdout "this is the successfull bash script"
          And automatic_correction for all deliveries has exit_value "0"
          And I log in as "teacher" "teacher"
         When I am in the list page of delivery from "TP Intro"
          And I click the button "autocorrection1"
         Then I should see "this is the successfull bash script"
          And I should see "Automatic check result: successfull"

    Scenario: As a student browse the results of an automatic check
    	Given Teacher "teacher" exists with password "teacher"
    	  And Student "student" exists with password "student"
    	  And course "2012-1" exists
    	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
          And script "successfull_test_script.sh" is set for practice "TP Intro" for course "2012-1"
          And a delivery exists for practice "TP Intro" and course "2012-1" from Student "student"
          And automatic_correction for all deliveries has status "successfull"
          And automatic_correction for all deliveries has stdout "this is the successfull bash script"
          And automatic_correction for all deliveries has exit_value "0"
          And I log in as "student" "student"
         When I am in the delivery page of practice "TP Intro"
          And I click in the "successfull" link
         Then I should see "this is the successfull bash script"
          And I should see "Automatic check result: successfull"
