#!/usr/bin/env python3
################################################################################
# Project:   2BIT ITS, Project                                                 #
#            Faculty of Information Technolgy                                  #
#            Brno University of Technology                                     #
# File:      environment.py                                                    #
# Date:      25.4.2019                                                         #
# Author:    Peter Kruty, <xkruty00@stud.fit.vutbr.cz>                         #
################################################################################

from behave import *
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def before_all(context):
    dp = {'browserName': 'firefox', 'marionette': 'true','javascriptEnabled': 'true'}
    context.open_cart_home_page = "http://mys01.fit.vutbr.cz:8038/"
    context.browser = webdriver.Remote(
                command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub',
                desired_capabilities=dp)
    context.browser.implicitly_wait(15)

def after_all(context):
    context.browser.quit()
