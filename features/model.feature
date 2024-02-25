Feature:My Model
    Scenario:Successful Logged In User 
    Given I load the website
    When I enter my username "Gaurav" and account ID "vault" and password "Gaurav@123"
    Then I click the login button
    Then I should be redirected to the dashboard page
    Then I take a screenshot of the dashboard

    Scenario:Access the My Model page
    Given User is Logged In
    When User on the Dashboard page
    When User click on the Model dropdown
    Then Select the My Models option
    Then User should be redirected to the My Models page
    Then User should take an screenshot

    Scenario:Search a model with specific id
    Given User is on my models page
    When Search for "OCC-3453" model
    Then Right Click on the Model in a Table
    Then Click on the View Details button
    Then User take a screenshot