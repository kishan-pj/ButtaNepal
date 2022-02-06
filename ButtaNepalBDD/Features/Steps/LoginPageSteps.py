from ButtaNepalBDD.Utilites.readproperty import ReadConfig
from ButtaNepalBDD.Utilites.customLogger import LogGen
from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

baseURL = ReadConfig.getURL()
myLogger = LogGen.loggen()

@given('Launch the browser')
def stepl_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install)
    myLogger.info("****Driver Installed****")
    context.driver.get(baseURL)

@then('verify the page title')
def step_imp(context):
    actual_title = context.driver.title
    expected_title = "ButtaNepal"

    if actual_title == expected_title:
        assert True
        myLogger.info("****Title Matched*****")
    else:
        myLogger.info("****Title not Match****")
        assert False

@then('close the browser')
def step_imple(context):
    context.driver.close()
    myLogger.info('Browser closed')