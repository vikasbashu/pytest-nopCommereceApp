import pytest
from pageObjects.LoginPage import Login
from datetime import datetime
#from Configurations.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_001_Login_ddt:


    # username = ReadConfig.getUserEmail()
    # password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()

    @pytest.mark.quickTest
    @pytest.mark.regression
    def test_login(self, setup):
         """homePageTitle"""
         self.driver = setup
         actual_status = []
         expected_status = []
         rows = XLUtils.get_row_count('TestData/LoginData.xlsx', 'Sheet1')
         self.logger.info('**** DDT test started')
         for i in range(2, rows+1):
             self.loginPage = Login(self.driver)
             self.loginPage.setUserName(XLUtils.read_data('TestData/LoginData.xlsx', 'Sheet1', i, 1))
             self.loginPage.setPassword(XLUtils.read_data('TestData/LoginData.xlsx', 'Sheet1', i, 2))
             expected_status.append(XLUtils.read_data('TestData/LoginData.xlsx', 'Sheet1', i, 3))
             self.loginPage.clickLogin()
             if self.driver.title == "Dashboard / nopCommerce administration":
                 assert True
                 self.logger.info("**** DDT test passed")
                 actual_status.append("pass")
                 self.loginPage.clickLogout()
                 time.sleep(5)
             else:
                 self.driver.save_screenshot(str('Screenshots/LoginWith{}.png'.format(XLUtils.read_data('TestData/LoginData.xlsx', 'Sheet1', i, 1))))
                 #self.loginPage.checkFailedLoginErrorMessage()
                 self.driver.refresh()
                 actual_status.append("fail")
                 self.logger.error("**** DDT Test Case Failed")
                 #assert False
         self.driver.close()
         assert actual_status == expected_status
