Feature: As a student I want to see the practice file list

	Scenario: No file practice
		 Given Student "martin" exists with password "martin"
    	  And course "2012-1" exists
    	  And a shift with name "tarde" and description "horario" in the course "2012-1"
    	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
          And student "martin" exists in course "2012-1" and in shift "tarde"
          And I log in as "martin" "martin"
    	 When I click in the "Download" link
    	 Then I should see "There are no files bounded to this practice"
    	 
   	Scenario: List file
   		Given Student "martin" exists with password "martin"
    	  And course "2012-1" exists
    	  And a shift with name "tarde" and description "horario" in the course "2012-1"
    	  And practice "TP Intro" exists in course "2012-1" with deadline "2012-12-01"
          And student "martin" exists in course "2012-1" and in shift "tarde"
          And file "enunciado" existe in the practice "TP Intro" and course "2012-1"
          And file "tp1" existe in the practice "TP Intro" and course "2012-1" 
          And I log in as "martin" "martin"
    	 When I click in the "Download" link
    	 Then I should see "enunciado"
    	  And I should see "tp1"
    	