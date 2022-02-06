class LoginPage:
    link_login_xpath = "//*[@id='/html/body/a[1]/button']"

def __init__(self,driver):
    self.driver = driver

def clickOnLogin(self):
    self.driver.find_element_by_xpath(self.link_login_xpath).click()