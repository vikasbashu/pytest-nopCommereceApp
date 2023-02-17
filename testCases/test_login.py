import pytest
import allure
from pageObjects.LoginPage import Login
from datetime import datetime
from utilities.customLogger import LogGen


class Test_001_Login:


    username = "admin@yourstore.com"
    password = "admin"


    # username = ReadConfig.getUserEmail()
    # password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()
    @allure.severity(allure.severity_level.TRIVIAL)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginPageTitle(self, setup):
        """loginPageTitle"""
        self.logger.info("*************** test_loginPageTitle Start**************")
        self.driver = setup
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.logger.info("*************** test_loginPageTitle Passed**************")
        else:
            self.driver.save_screenshot(str('Screenshots/{}.png'.format(self.test_loginPageTitle.__doc__ + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))))
            self.logger.error("*************** test_loginPageTitle Failed**************")
            assert False
        self.driver.close()
        self.logger.info("*************** test_loginPageTitle End**************")

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.regression
    def test_login(self, setup):
         """login test"""
         self.driver = setup
         self.loginPage = Login(self.driver)
         self.loginPage.setUserName(self.username)
         self.loginPage.setPassword(self.password)
         self.loginPage.clickLogin()
         assert self.driver.title == "Dashboard / nopCommerce administration", self.driver.save_screenshot(str('Screenshots/{}.png'.format(self.driver.title)))
         self.driver.close()