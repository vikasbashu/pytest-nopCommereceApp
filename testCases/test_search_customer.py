import pytest

from pageObjects.AddCustomerPage import Addcustomer
from pageObjects.SearchCustomer import SearchCustomer
from pageObjects.LoginPage import Login

class Test_003_Search_Customer:

    username = "admin@yourstore.com"
    password = "admin"

    @pytest.mark.smoke
    def test_search_customer_by_email(self, setup):
        self.driver = setup
        search_value = "brenda_lindgren@nopCommerce.com"
        # login into application
        self.loginPage = Login(self.driver)
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        assert self.driver.title == "Dashboard / nopCommerce administration", self.driver.save_screenshot(
            str('Screenshots/{}.png'.format(self.driver.title)))

        # Navigate to customer page

        self.addCustomerPage = Addcustomer(self.driver)
        self.addCustomerPage.selectSubCategory('Customer')

        # search customer

        self.customerPage = SearchCustomer(self.driver)
        self.customerPage.fillEmailField(search_value)
        self.customerPage.searchRecords()
        self.result = self.customerPage.getOutputResult()

        if search_value in self.result:
            assert True
        else:
            self.driver.save_screenshot('Screenshots/{}.png'.format(search_value))
            assert "No data available in table" == self.result
            assert False

        self.driver.close()

    @pytest.mark.smoke
    def test_search_customer_by_name(self, setup):
        self.driver = setup
        search_value = "Brenda"
        # login into application
        self.loginPage = Login(self.driver)
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        assert self.driver.title == "Dashboard / nopCommerce administration", self.driver.save_screenshot(
            str('Screenshots/{}.png'.format(self.driver.title)))

        # Navigate to customer page

        self.addCustomerPage = Addcustomer(self.driver)
        self.addCustomerPage.selectSubCategory('Customer')

        # search customer

        self.customerPage = SearchCustomer(self.driver)
        self.customerPage.fillFirstNameField(search_value)
        self.customerPage.searchRecords()
        self.result = self.customerPage.getOutputResult()

        if search_value in self.result:
            assert True
        else:
            self.driver.save_screenshot('Screenshots/{}.png'.format(search_value))
            assert "No data available in table" == self.result
            assert False

        self.driver.close()

