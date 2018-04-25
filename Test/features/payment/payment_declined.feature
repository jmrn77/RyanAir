Feature: Payment Declined
  As a client
  I want to book a flight but the payment is declined
  so that I will receive an error message

  Background: The page is successfully loaded
    Given I navigate to "HomePage"


  @TC-1 @US-100
  @payment @declined
  Scenario: Payment is declined by an invalid credit card
    Given I make a booking from "Dublin" to "Liverpool" for tomorrow
    When  I pay for booking with data of "user_testing" and credit card "invalid"
    Then  I should get "payment declined" message
