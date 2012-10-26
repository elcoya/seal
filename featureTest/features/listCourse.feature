Feature: As a professor I want to see the course list

    Scenario: Courses ordered by newest first
       Given course "2012-1" exists
         And course "2011-1" exists
         And I am in the course list page
        Then I should see "2012-1" before "2011-1" 
    
    Scenario: No courses
        Given there are no courses
          And I am in the course list page
         Then I should see "0 courses"
