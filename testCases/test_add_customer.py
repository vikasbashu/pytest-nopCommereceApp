import pytest

from pageObjects.AddCustomerPage import Addcustomer
from pageObjects.LoginPage import Login

class Test_002_add_customer:

    username = "admin@yourstore.com"
    password = "admin"

    @pytest.mark.smoke
    def test_add_customer_feature(self, setup):
        self.driver = setup
        # login into application
        self.loginPage = Login(self.driver)
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        assert self.driver.title == "Dashboard / nopCommerce administration", self.driver.save_screenshot(
            str('Screenshots/{}.png'.format(self.driver.title)))
        # select customer category
        self.addCustomerPage = Addcustomer(self.driver)
        self.addCustomerPage.selectSubCategory('Customer')
        self.addCustomerPage.clickAddNewButton()
        assert self.driver.title == "Add a new customer / nopCommerce administration", self.driver.save_screenshot(
            str('Screenshots/{}.png'.format(self.driver.title)))
        self.driver.close()


