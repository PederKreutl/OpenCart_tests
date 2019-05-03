################################################################################
# Project:   2BIT ITS, Project                                                 #
#            Faculty of Information Technolgy                                  #
#            Brno University of Technology                                     #
# File:      product_search.feature                                            #
# Date:      11.04.2019                                                        #
# Author:    Peter Kruty, <xkruty00@stud.fit.vutbr.cz>                         #
################################################################################

Feature: Product search on OpenCart platform
  This feature verifies the correct implementation of product search
  on OpenCart platform.

################################################################################
  Scenario Outline: Show products category drop-down list
    Given home page is loaded
    When user clicks on category tab "<category>"
    Then "<category>" drop-down list with following informations appears
      | category            | subcategory1 | subcategory2 |
      | Desktops            | PC           | Mac          |
      | Laptops & Notebooks | Macs         | Windows      |

    Examples: Categories
      | category            |
      | Desktops            |
      | Laptops & Notebooks |

################################################################################
  Scenario Outline: Show products category
    Given home page is loaded
    When user clicks on category tab "<category>"
    Then "<category>" category page appears

    Examples: Categories
      | category |
      | Tablets  |
      | Software |

################################################################################
  Scenario Outline: Show product
    Given "<category>" category page is loaded
    When user clicks on product "<product>"
    Then "<product>" product page appears

    Examples: Products in category
      | category | product                 |
      | Tablets  | Samsung Galaxy Tab 10.1 |
      | Cameras  | Canon EOS 5D            |
