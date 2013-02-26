Feature: As a Teacher I should be able to browse the files of the deliveries done by the students

    Scenario: Access the delivery explorer as a teacher
        Given Teacher "teacher" exists with password "teacher"
          And course "2013-1" exists
          And practice "TP Intro" exists in course "2013-1" with deadline "2013-04-01"
    	  And Student "student" exists with password "student"
          And a delivery exists for practice "TP Intro" and course "2013-1" from Student "student" with id "1"
          And I log in as "teacher" "teacher"
         When I am in the list page of delivery from "TP Intro"
         Then I should see a link to "/teacher/delivery/explore/1"

    Scenario: Browse a certain delivery
        Given Teacher "teacher" exists with password "teacher"
          And course "2013-1" exists
          And practice "TP Intro" exists in course "2013-1" with deadline "2013-04-01"
    	  And Student "student" exists with password "student"
          And a delivery exists for practice "TP Intro" and course "2013-1" from Student "student" with id "1"
          And I log in as "teacher" "teacher"
         When I am at the explore delivery page for delivery "1"
         Then I should see a link to "/teacher/delivery/browse/1/prueba.txt"
          And I should see "prueba.txt"
	
	Scenario: Browse a certain delivery
        Given Teacher "teacher" exists with password "teacher"
          And course "2013-1" exists
          And practice "TP Intro" exists in course "2013-1" with deadline "2013-04-01"
    	  And Student "student" exists with password "student"
          And a delivery exists for practice "TP Intro" and course "2013-1" from Student "student" with id "1"
          And I log in as "teacher" "teacher"
         When I am at the browse delivery page for delivery "1" browsing "prueba.txt"
         Then I should see a link to "/teacher/delivery/browse/1/prueba.txt"
          And I should see "prueba.txt"
          And I should see "lalala"
	
	