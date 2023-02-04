import pytest
import allure
from pageObjects.AddCustomerPage import Addcustomer
from pageObjects.SearchCustomer import SearchCustomer
from pageObjects.LoginPage import Login


@allure.severity(allure.severity_level.NORMAL)
class Test_003_Search_Customer:

    username = "admin@yourstore.com"
    password = "admin"

    @pytest.mark.xdist_group(name="Suit2")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.parametrize("username, password", [
        ("admin@yourstore.com", "admin")
    ])
    def test_search_customer_by_email(self, setup, username, password):
        self.driver = setup
        search_value = "brenda_lindgren@nopCommerce.com"
        # login into application
        self.loginPage = Login(self.driver)
        self.loginPage.setUserName(username)
        self.loginPage.setPassword(password)
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
            self.customerPage.commonMethods.addAllureScreenShot(search_value)
            assert "No data available in table" == self.result
            assert False

        self.driver.close()

    @pytest.mark.xdist_group(name="Suit2")
    @allure.severity(allure.severity_level.MINOR)
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
            self.customerPage.commonMethods.addAllureScreenShot(search_value)
            assert "No data available in table" == self.result
            assert False

        self.driver.close()

    @pytest.mark.xdist_group(name="Suit2")
    @pytest.mark.skip("Implement this later")
    def test_search_customer_by_lastName(self):
        pass


