Feature: As a professor I want to see the course list

    Scenario: No courses
        Given I am in the course list page
          And there are no courses 
         Then I should see "0 courses"
