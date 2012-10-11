Feature: Login promt

  Scenario: Login to site
     Given we have opened the browser for "http://localhost:8000/admin"
      When we input login data "seal|seal"
      Then we enter in the page with this title "Site administration | Django site admin"
      And we logout
      And we close de browser


