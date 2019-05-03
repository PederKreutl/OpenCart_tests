################################################################################
# Project:   2BIT ITS, Project                                                 #
#            Faculty of Information Technolgy                                  #
#            Brno University of Technology                                     #
# File:      checkout_process.feature                                          #
# Date:      11.04.2019                                                        #
# Author:    Peter Kruty, <xkruty00@stud.fit.vutbr.cz>                         #
################################################################################

Feature: Checkout process on OpenCart platform
  This feature verifies the correct implementation of checkout process
  on OpenCart platform.

################################################################################
  Background:
    Given product "iPhone" is in cart

################################################################################
  Scenario: Start checkout
    Given cart page is loaded
      When user clicks on button "Checkout"
      Then checkout page (Step 1) is loaded

################################################################################
  Scenario: Insert checkout data (Step 1, Checkout options)
    Given checkout page (Step 1) is loaded
    When user marks Guest Checkout
      And user clicks on button "Continue"
    Then checkout page (Step 2) is loaded

################################################################################
  Scenario: Insert checkout data (Step 2, Billing details)
    Given checkout page (Step 2) is loaded
    When user fill required fields
      And user mark Delivery and Billing addresses are the same
      And user clicks on button "Continue"
    Then checkout page (Step 4) is loaded

################################################################################
  Scenario: Insert checkout data (Step 4, Delivery method)
    Given checkout page (Step 4) is loaded
    When user clicks on button "Continue"
    Then checkout page (Step 5) is loaded

################################################################################
  Scenario: Insert checkout data (Step 5, Payment method)
    Given checkout page (Step 5) is loaded
    When user marks Agreement with Terms & Conditions
      And user clicks on button "Continue"
    Then checkout page (Step 6) is loaded

################################################################################
  Scenario: Insert checkout data (Step 6, Confirm order)
    Given checkout page (Step 6) is loaded
    When user clicks on button "Confirm Order"
    Then order has been successfully processed

# EOF
