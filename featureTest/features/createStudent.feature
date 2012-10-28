Feature: As a teacher I want to create a student
    
    Scenario: Create Student
        Given there are no students
          And I am at the new student form
         When I fill the newstudent form with default data
          And I submit the form
         Then I should see "New student saved successfully"

