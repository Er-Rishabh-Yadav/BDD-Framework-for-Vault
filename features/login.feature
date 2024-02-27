Feature: User Login
  As a registered user
  I want to be able to log in to my account
  So that I can access my profile
  
  @login 
  Scenario: Successful login with valid credentials
    Given I load the website
    When I enter my username "Gaurav" and account ID "vault" and password "Gaurav@123"
    Then I click the login button
    Then I should be redirected to the dashboard page
    Then I take a screenshot of the dashboard
    # Then Stop the driver
  

  Scenario:Logout Successfully
    Given User should loggedin
    When User clicks on logout button
    Then User should be logged out successfully
    Then Take a screenshot of the landing page

  Scenario: Login with incorrect credentials
    Given I load the website
    When I enter invalid username "user" and account ID "vault" and password "User@123"
    Then I click the login button
    Then I should see an error massage "Username does not exist."
    Then I take a screenshot of the error massage
    # Then Stop the driver