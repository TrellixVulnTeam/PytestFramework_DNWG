Feature: Home Page
  A site where u can practice automation testing

  Scenario: Go to Home Page
    Given Home Page Display
    And Check Menu List is present
    And Practice Board is present
    Then Check all the demo listed down in Basic section


  Scenario: Validate simple demo page
    When Validate if get input form is working
    Then Validate if get input total form is working


#  Scenario: Go to test Check Box Demo page
#    Given User is on Check demo page and verify check box is display and working
#    Then Verify multiple check box


#Feature:
#  Scenario: Go to test Check Box Demo page
#    Given User is on Check demo page and verify check box is display and working
#    Then Verify multiple check box




