Feature: As a teacher I want to modifier a name course

 	Scenario: Index page follow link to edit course and modifier the course
        Given course "2012-1" exists
          And I am in the index page
         When I click in the "2012-1" link
          And I change "2012-1" for "2013-1" in element whith id "id_name"
          And I submit the form
          Then I should see link to "2013-1" in the list