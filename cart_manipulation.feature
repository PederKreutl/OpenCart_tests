################################################################################
# Project:   2BIT ITS, Project                                                 #
#            Faculty of Information Technolgy                                  #
#            Brno University of Technology                                     #
# File:      cart_manipulation.feature                                         #
# Date:      11.04.2019                                                        #
# Author:    Peter Kruty, <xkruty00@stud.fit.vutbr.cz>                         #
################################################################################

Feature: Cart manipulation on OpenCart platform
  This feature verifies the correct implementation of cart manipulation
  on OpenCart platform.

################################################################################
  Scenario Outline: Add product to cart
    Given "<product>" product page is loaded
    When user insert "<product>" product options
      And user insert product quantity "2"
      And user clicks on button "Add to cart"
    Then "<product>" product quantity in cart is set to "2"

    Examples: Product pages
      | product                 |
      | Samsung Galaxy Tab 10.1 |
      | Canon EOS 5D            |

################################################################################
  Scenario: Show cart drop-down list
    Given home page is loaded
      And product "iPhone" is in cart
    When user clicks on button "Cart"
    Then cart drop-down list with product "iPhone" appears

################################################################################
  Scenario: Go to cart
    Given home page is loaded
      And product "iPhone" is in cart
    When user clicks on button "Cart"
      And user clicks on button "View Cart"
    Then cart page with product "iPhone" is loaded

################################################################################
  Scenario Outline: Change Currency
    Given cart page is loaded
    When user clicks on button "Currency"
      And user clicks on button "<currency>"
    Then currency "<currency>" is set as actual currency

    Examples: Currency
      | currency       |
      | Euro           |
      | Pound Sterling |
      | US Dollar      |

################################################################################
  Scenario: Remove product from cart
    Given cart page is loaded
      And product "iPhone" is in cart
    When in product cell "iPhone" user clicks on button "Remove"
    Then product "iPhone" is not in cart

################################################################################
  Scenario: Change product quantity in cart
    Given cart page is loaded
      And product "iPhone" is in cart
    When in product cell "iPhone" user change quantity to "2"
      And in product cell "iPhone" user clicks on button "Update"
    Then "iPhone" product quantity in cart is set to "2"

################################################################################
  Scenario: Use Coupon code
    Given cart page is loaded
      And product "iPhone" is in cart
    When user clicks on button "Use Coupon Code"
      And user insert valid coupon code "1111"
        | Coupon code | Sale |
        | 5555        | 20%  |
        | 1111        | 10%  |
      And user clicks on button "Apply Coupon"
    Then total price drops down according to coupon code "1111"
      | Coupon code | Sale |
      | 5555        | 20%  |
      | 1111        | 10%  |
