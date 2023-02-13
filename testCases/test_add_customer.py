import pytest
import re
from pageObjects.AddCustomerPage import Addcustomer
from pageObjects.LoginPage import Login


class Test_002_add_customer:

    @pytest.mark.xdist_group(name="Suit2")
    @pytest.mark.smoke
    @pytest.mark.repeat(1)
    @pytest.mark.parametrize("username, password", [
        ("admin@yourstore.com", "admin")
    ])
    def test_add_customer_feature(self, setup, username, password):
        self.driver = setup
        # login into application
        self.loginPage = Login(self.driver)
        self.loginPage.setUserName(username)
        self.loginPage.setPassword(password)
        self.loginPage.clickLogin()
        assert self.driver.title == "Dashboard / nopCommerce administration", \
            self.loginPage.commonMethods.addAllureScreenShot(self.driver.title)
        # select customer category
        self.addCustomerPage = Addcustomer(self.driver)
        self.addCustomerPage.selectSubCategory('Customer')
        self.addCustomerPage.clickAddNewButton()
        assert self.driver.title == "Add a new customer / nopCommerce administration", \
            self.addCustomerPage.commonMethods.addAllureScreenShot(self.driver.title)
        self.addCustomerPage.validatePageTitle('Add a new customer')
        self.addCustomerPage.fillUserDetails()
        assert re.search("The new customer has been added successfully.", self.addCustomerPage.getAlertText()), \
            self.addCustomerPage.commonMethods.addAllureScreenShot(self.addCustomerPage.getAlertText())
        self.driver.close()
