################################################################################
# Project:   2BIT ITS, Project                                                 #
#            Faculty of Information Technolgy                                  #
#            Brno University of Technology                                     #
# File:      page_visit.feature                                                #
# Date:      11.04.2019                                                        #
# Author:    Peter Kruty, <xkruty00@stud.fit.vutbr.cz>                         #
################################################################################

Feature: Check page availibility on Opencart platform
  This feature verifies the correct implementation of page visit
  on OpenCart platform.

################################################################################
  Scenario Outline: Visit page
    Given home page is loaded
    When user clicks on link "<page>"
    Then page "<page>" appears

    Examples:
      | page                 |
      | Delivery Information |
      | Returns              |
