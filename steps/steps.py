#!/usr/bin/env python3
################################################################################
# Project:   2BIT ITS, Project                                                 #
#            Faculty of Information Technolgy                                  #
#            Brno University of Technology                                     #
# File:      steps.py                                                          #
# Date:      25.4.2019                                                         #
# Author:    Peter Kruty, <xkruty00@stud.fit.vutbr.cz>                         #
################################################################################
import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# behave --no-capture -f plain

# product_search.feature
@given('home page is loaded')
def step_impl(context):
    context.browser.get(context.open_cart_home_page)

@when('user clicks on category tab {category}')
def step_impl(context, category):
    if category == '"Tablets"':
        context.browser.find_element_by_xpath("//a[contains(text(),'Tablets')]").click()
    elif category == '"Software"':
        context.browser.find_element_by_xpath("//a[contains(text(),'Software')]").click()
    elif category == '"Desktops"':
        context.browser.find_element_by_xpath("//a[contains(text(),'Desktops')]").click()
    elif category == '"Laptops & Notebooks"':
        context.browser.find_element_by_xpath("//a[contains(text(),'Laptops & Notebooks')]").click()

@then('{category} drop-down list with following informations appears')
def step_impl(context, category):
    if category == '"Desktops"':
        subcategory1 = context.browser.find_element_by_xpath("//li[@class='dropdown open']//li[1]//a").text[:2]
        subcategory2 = context.browser.find_element_by_xpath("//li[@class='dropdown open']//li[2]//a").text[:3]
        for row in context.table:
            if row['category'] == "Desktops":
                assert(row['subcategory1'] == subcategory1)
                assert(row['subcategory2'] == subcategory2)

    elif category == '"Laptops & Notebooks"':
        subcategory1 = context.browser.find_element_by_xpath("//li[@class='dropdown open']//li[1]//a").text[:4]
        subcategory2 = context.browser.find_element_by_xpath("//li[@class='dropdown open']//li[2]//a").text[:7]
        for row in context.table:
            if row['category'] == "Laptops & Notebooks":
                assert(row['subcategory1'] == subcategory1)
                assert(row['subcategory2'] == subcategory2)

@then('{category} category page appears')
def step_impl(context, category):
    if category == '"Tablets"':
        page_title = context.browser.find_element_by_xpath("//div/h2[contains(text(),'Tablets')]").text
        assert(u"Tablets" == page_title)
    elif category == '"Software"':
        page_title = context.browser.find_element_by_xpath("//div/h2[contains(text(),'Software')]").text
        assert(u"Software" == page_title)

@given('{category} category page is loaded')
def step_impl(context, category):
    if category == '"Tablets"':
        context.browser.get("http://mys01.fit.vutbr.cz:8038/index.php?route=product/category&path=57")
    elif category == '"Cameras"':
        context.browser.get("http://mys01.fit.vutbr.cz:8038/index.php?route=product/category&path=33")

@when('user clicks on product {product}')
def step_impl(context, product):
    if product == '"Canon EOS 5D"':
        context.browser.find_element_by_xpath("//div/a/img[@title='Canon EOS 5D']").click()
    elif product == '"Samsung Galaxy Tab 10.1"':
        context.browser.find_element_by_xpath("//div/a/img[@title='Samsung Galaxy Tab 10.1']").click()

@then('{product} product page appears')
def step_impl(context, product):
    if product == '"Canon EOS 5D"':
        product_title = context.browser.find_element_by_xpath("//div[@class]//h1[contains(text(),'Canon EOS 5D')]").text
        assert(product_title == u"Canon EOS 5D")
    elif product == '"Samsung Galaxy Tab 10.1"':
        product_title = context.browser.find_element_by_xpath("//div[@class]//h1[contains(text(),'Samsung Galaxy Tab 10.1')]").text
        assert(product_title == u"Samsung Galaxy Tab 10.1")

# page_visit.feature
@when('user clicks on link {page}')
def step_impl(context, page):
    if page == '"Delivery Information"':
        context.browser.find_element_by_xpath("//footer/div/div/div/ul/li/a[contains(text(),'Delivery Information')]").click()
    elif page == '"Returns"':
        context.browser.find_element_by_xpath("//footer/div/div/div/ul/li/a[contains(text(),'Returns')]").click()

@then('page {page} appears')
def step_impl(context, page):
    if page == '"Delivery Information"':
        context.browser.find_element_by_xpath("//body/div/div/div/h1[contains(text(),'Delivery Information')]")
    elif page == '"Returns"':
        context.browser.find_element_by_xpath("//body/div/div/div/h1[contains(text(),'Product Returns')]")

# cart_manipulation.feature
@given('{product} product page is loaded')
def step_impl(context, product):
    if product == '"Samsung Galaxy Tab 10.1"':
        context.browser.get("http://mys01.fit.vutbr.cz:8038/index.php?route=product/product&path=57&product_id=49")
    elif product == '"Canon EOS 5D"':
        context.browser.get("http://mys01.fit.vutbr.cz:8038/index.php?route=product/product&path=33&product_id=30")

@given('product {product} is in cart')
def step_impl(context, product):
    current_url = context.browser.current_url
    if product == '"iPhone"':
        context.browser.get("http://mys01.fit.vutbr.cz:8038/index.php?route=product/product&path=24&product_id=40")
        context.browser.find_element_by_id("button-cart").click()

    context.browser.get(current_url)

@given('cart page is loaded')
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8038/index.php?route=checkout/cart")

@when('user insert {product} product options')
def step_impl(context, product):
    if product == '"Samsung Galaxy Tab 10.1"':
        pass
    elif product == '"Canon EOS 5D"':
        context.browser.find_element_by_xpath('//*[@id="input-option226"]').click()
        context.browser.find_element_by_xpath("//body/div/div/div/div/div/div/div/select/option[contains(text(),'Red')]").click()
        context.browser.find_element_by_id("input-quantity").send_keys("3")

@when('user insert product quantity {quantity}')
def step_impl(context, quantity):
        quantity = quantity[1:-1]
        context.browser.find_element_by_id("input-quantity").clear()
        context.browser.find_element_by_id("input-quantity").send_keys(quantity)

@when('user clicks on button {button}')
def step_impl(context, button):
    if button == '"Checkout"':
        context.browser.find_element_by_xpath("//div/a[contains(text(),'Checkout')]").click()
    elif button == '"Add to cart"':
        context.browser.find_element_by_id("button-cart").click()
    elif button == '"Cart"':
        context.browser.find_element_by_id("cart").click()
    elif button == '"View Cart"':
        context.browser.find_element_by_xpath("//header/div/div/div/div/ul/li/div/p/a[@href='http://mys01.fit.vutbr.cz:8038/index.php?route=checkout/cart']").click()
    elif button == '"Currency"':
        context.browser.find_element_by_id("form-currency").click()
    elif button == '"Euro"':
        context.browser.find_element_by_xpath("//form/div/ul/li/button[@name='EUR']").click()
    elif button == '"Pound Sterling"':
        context.browser.find_element_by_xpath("//form/div/ul/li/button[@name='GBP']").click()
    elif button == '"US Dollar"':
        context.browser.find_element_by_xpath("//form/div/ul/li/button[@name='USD']").click()
    elif button == "Use Coupon Code":
        context.browser.find_element_by_xpath("/html/body/div/div/div/div/div/div/h4/a[contains(text(),'Use Coupon Code')]").click()

@when('in product cell {product} user clicks on button {button}')
def step_impl(context, button, product):
    if button == '"Remove"':
        context.browser.find_element_by_xpath("//table/tbody/tr/td/div/span/button[@class='btn btn-danger']").click()
    elif button == '"Update"':
        context.browser.find_element_by_xpath("//table/tbody/tr/td/div/span/button[@class='btn btn-primary']").click()

@when('in product cell {product} user change quantity to {quantity}')
def step_impl(context, product, quantity):
    quantity = quantity[1:-1]
    context.browser.find_element_by_xpath("//table/tbody/tr/td/div/input").clear()
    context.browser.find_element_by_xpath("//table/tbody/tr/td/div/input").send_keys(quantity)

@when('user insert valid coupon code {code}')
def step_impl(context, code):
    pass # Cannot implement (Unsupported structure of webpage)

@then('{product} product quantity in cart is set to {quantity}')
def step_impl(context, product, quantity):
    quantity = quantity[1:-1]
    product = product[1:-1]
    context.browser.find_element_by_xpath("/html/body/header/div/div/div/div/button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']").click()
    context.browser.find_element_by_xpath("//body/header//p[@class='text-right']/a").click()
    context.browser.find_element_by_xpath("//table/tbody/tr/td/a[contains(text(),'%s')]" % product)
    context.browser.find_element_by_xpath("//table/tbody/tr/td/div/input[@value=%s]" % quantity)
    context.browser.find_element_by_xpath("//table/tbody/tr/td/div/span/button[@class='btn btn-danger']").click()

@then('cart drop-down list with product {product} appears')
def step_impl(context, product):
    product = product[1:-1]
    context.browser.find_element_by_xpath("//table/tbody/tr/td/a[contains(text(),'%s')]" % product)
    context.browser.find_element_by_xpath("//table/tbody/tr/td/button[@class='btn btn-danger btn-xs']").click()

@then('cart page with product {product} is loaded')
def step_impl(context, product):
    cart_title = context.browser.find_element_by_xpath("/html/body/div/div/div/h1").text
    cart_title = cart_title[:13]
    assert(cart_title == u"Shopping Cart")
    product = product[1:-1]
    context.browser.find_element_by_xpath("//table/tbody/tr/td/a[contains(text(),'%s')]" % product)

@then('currency {currency} is set as actual currency')
def step_impl(context, currency):
    currency_act = context.browser.find_element_by_xpath("//html/body/nav/div/div/form/div/button/strong").text
    if currency == '"Euro"':
        assert(currency_act == u"€")
    elif currency == '"Pound Sterling"':
        assert(currency_act == u"£")
    elif currency == '"US Dollar"':
        assert(currency_act == u"$")

@then('product {product} is not in cart')
def step_impl(context, product):
    empty = context.browser.find_element_by_xpath("//html/body/div/div/div/p").text
    assert(empty == u"Your shopping cart is empty!")


@then('total price drops down according to coupon code {code}')
def step_impl(context, code):
    pass # Cannot implement (Unsupported structure of webpage)

# checkout_process.feature
@then('checkout page (Step 1) is loaded')
def step_impl(context):
    step_expanded = context.browser.find_element_by_xpath("/html/body/div/div/div/div/div/div/h4/a[@aria-expanded='true']").text
    assert(step_expanded == u"Step 1: Checkout Options")

@given('checkout page (Step 1) is loaded')
def step_impl(context):
    pass # Cannot implement (Unsupported structure of webpage)

@given('checkout page (Step 2) is loaded')
def step_impl(context):
    pass # Cannot implement (Unsupported structure of webpage)

@given('checkout page (Step 4) is loaded')
def step_impl(context):
    pass # Cannot implement (Unsupported structure of webpage)

@given('checkout page (Step 5) is loaded')
def step_impl(context):
    pass # Cannot implement (Unsupported structure of webpage)

@given('checkout page (Step 6) is loaded')
def step_impl(context):
    pass # Cannot implement (Unsupported structure of webpage)

@when('user marks Guest Checkout')
def step_impl(context):
    pass # Cannot implement (Unsupported structure of webpage)

@when('user fill required fields')
def step_impl(context):
    pass # Cannot implement (Unsupported structure of webpage)

@when('user mark Delivery and Billing addresses are the same')
def step_impl(context):
    pass # Cannot implement (Unsupported structure of webpage)

@when('user marks Agreement with Terms & Conditions')
def step_impl(context):
    pass # Cannot implement (Unsupported structure of webpage)

@then('checkout page (Step 2) is loaded')
def step_impl(context):
    pass # Cannot implement (Unsupported structure of webpage)

@then('checkout page (Step 4) is loaded')
def step_impl(context):
    pass # Cannot implement (Unsupported structure of webpage)

@then('checkout page (Step 5) is loaded')
def step_impl(context):
    pass # Cannot implement (Unsupported structure of webpage)

@then('checkout page (Step 6) is loaded')
def step_impl(context):
    pass # Cannot implement (Unsupported structure of webpage)

@then('order has been successfully processed')
def step_impl(context):
    pass # Cannot implement (Unsupported structure of webpage)
