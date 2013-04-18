Feature: As a Teacher I should be able to download a file containing a summary of the deliveries made by the students

    Scenario: As a teacher I should see the link to the Export Data page
        Given Teacher "teacher" exists with password "teacher"
          And course "2013-1" exists
         When I log in as "teacher" "teacher"
         Then I should see a link to "/teacher/export/"

    Scenario: As a teacher I should be able to access the Export Data page given there are no courses
        Given Teacher "teacher" exists with password "teacher"
          And there are no courses
         When I log in as "teacher" "teacher"
         Then I should not see a link to "/teacher/export/"

    Scenario: As a teacher I should be able to access the Export Data page given there is a course
        Given Teacher "teacher" exists with password "teacher"
          And course "2013-1" with pk "1" exists
         When I log in as "teacher" "teacher"
          And I click the link to "/teacher/export/"
         Then I should see a link to "/teacher/export/download/1"

