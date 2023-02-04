import pytest

from pageObjects.AddCustomerPage import Addcustomer
from pageObjects.LoginPage import Login

class Test_002_add_customer:

    @pytest.mark.xdist_group(name="Suit2")
    @pytest.mark.smoke
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
        assert self.driver.title == "Dashboard / nopCommerce administration", self.driver.save_screenshot(
            str('Screenshots/{}.png'.format(self.driver.title)))
        # select customer category
        self.addCustomerPage = Addcustomer(self.driver)
        self.addCustomerPage.selectSubCategory('Customer')
        self.addCustomerPage.clickAddNewButton()
        assert self.driver.title == "Add a new customer / nopCommerce administration", \
            self.addCustomerPage.commonMethods.addAllureScreenShot(self.driver.title)
        self.driver.close()


