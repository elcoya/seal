Feature: As a Student I should be able to upload my deliveries and trigger the automatic correction

    Scenario: Upload a new delivery leaving it pending
        Given course "2012-1" exists
          And Student "student" exists with password "student"
          And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
          And there are no deliveries
         When I create a new delivery for practice "TP Intro" and course "2012-1" from Student "student"
         Then delivery for practice "TP Intro" and course "2012-1" from Student "student" should have status "pending"
   
    Scenario: Run the AutomaticCorrection for the deliveries
        Given course "2012-1" exists
          And Student "student" exists with password "student"
          And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
          And script "successfull_test_script.sh" is set for practice "TP Intro" for course "2012-1"
          And there are no deliveries
         When I create a new delivery for practice "TP Intro" and course "2012-1" from Student "student"
          And I run the AutomaticCorrection process
         Then delivery for practice "TP Intro" and course "2012-1" from Student "student" should have status "successfull"
