from behave import *
from selenium import webdriver


@given(u"Lunch Chrome Browser")
def lunchBrowser(context):
    context.driver = webdriver.Chrome()


@when(u"Open ButtaNepal Homepage")
def openHomePage(context):
    context.driver.get("http://localhost:8000/")


@then(u"Verify that the logo present on webpage")
def verifyLogo(context):
    status = context.driver.find_element_by_xpath(
        '''//*[@id="navbar"]/header/nav[2]/div/a/img'''
    ).is_displayed()
    assert status is True


@then(u"Close Browser")
def closeBrowser(context):
    context.driver.close()
