import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.loginPage_locators = self.pageLocators('GooglePage')

    def isAt(self):
        header_login = self.getElementList(*self.locator(self.loginPage_locators, 'header_login'))
        if len(header_login) > 0:
            return True
        return False

    def login(self, searchtext):
        self.sendKeys(searchtext, *self.locator(self.loginPage_locators, 'search_box'))
        self.elementClick(*self.locator(self.loginPage_locators, 'search_button'))
