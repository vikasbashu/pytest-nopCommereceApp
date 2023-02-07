from utilities.CommonMethods import CommonFunctions


class Addcustomer:

    text_sideNavBar_customers_xpath = "(//p[contains(text(), 'Customers')])[1]"
    text_subCategory_xpath = "(//p[contains(text(), 'Customers')])[2]"
    button_AddNew_xpath = "//a[@class='btn btn-primary']"
    min_wait, max_wait = 10, 30


    def __init__(self, driver):
        self.driver = driver
        self.commonMethods = CommonFunctions(self.driver)


    def selectSubCategory(self, category):
        self.commonMethods.waitForVisible(self.text_sideNavBar_customers_xpath, self.min_wait)
        self.commonMethods.acceptAlerts()
        self.commonMethods.clickElement(self.text_sideNavBar_customers_xpath)
        self.commonMethods.waitForVisible(self.text_subCategory_xpath, self.min_wait)
        self.commonMethods.clickElement(self.text_subCategory_xpath)


    def clickAddNewButton(self):
        self.commonMethods.waitForVisible(self.button_AddNew_xpath, self.min_wait)
        self.commonMethods.clickElement(self.button_AddNew_xpath)












