from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import Addcustomer
from pageObjects.AddVendors import AddVendors
import pytest, re, allure


class Test_004_Add_Vendor_Feature():


    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.order(1)
    @pytest.mark.repeat(1)
    @pytest.mark.sanity
    @pytest.hookimpl(tryfirst=True)
    @pytest.mark.xdist_group(name='Suit4')
    @pytest.mark.parametrize("username, password", [
        ("admin@yourstore.com", "admin")
    ])
    def test_add_single_vendor(self, setup, username, password):
        self.driver = setup
        self.loginPage = Login(self.driver)
        self.loginPage.setUserName(username)
        self.loginPage.setPassword(password)
        self.loginPage.clickLogin()
        assert self.driver.title == "Dashboard / nopCommerce administration", \
            self.loginPage.commonMethods.addAllureScreenShot(self.driver.title)
        self.addCustomerPage = Addcustomer(self.driver)
        self.addCustomerPage.selectSubCategory('Vendors')
        self.addCustomerPage.validatePageTitle('Vendors')
        self.addCustomerPage.clickAddNewButton()
        self.addCustomerPage.validatePageTitle('Add a new vendor')
        assert self.driver.title == "Add a new vendor / nopCommerce administration", \
            self.addCustomerPage.commonMethods.addAllureScreenShot(self.driver.title)
        self.addVendorPage = AddVendors(self.driver)
        self.addVendorPage.fillVendorDetails()
        self.addVendorPage.commonMethods.pressButton('save')
        assert re.search("For security purposes, the feature you have requested is not available on the demo site.",
                         self.addCustomerPage.getAlertText()), self.addVendorPage.commonMethods.addAllureScreenShot(
            self.addCustomerPage.getAlertText()
        )
        self.driver.close()