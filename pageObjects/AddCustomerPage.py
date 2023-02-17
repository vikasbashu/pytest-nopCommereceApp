from utilities.CommonMethods import CommonFunctions
from utilities import GenericFunctions as gf

class Addcustomer:

    text_sideNavBar_customers_xpath = "(//p[contains(text(), 'Customers')])[1]"
    text_subCategory_xpath = "(//p[contains(text(), 'Customers')])[2]"
    button_AddNew_xpath = "//a[@class='btn btn-primary']"
    min_wait, max_wait = 10, 30
    #page_title = lambda title='Add a new customer': "(//h1[contains(text(), '{}')])[1]".format(title)
    def page_title(self, title):
        return "(//h1[contains(text(), '{}')])[1]".format(title)

    def sub_category_xpath(self, sub_category, index):
        return "(//p[contains(text(), '{}')])[{}]".format(sub_category, str(index))

    def select_gender(self, label):
        if label.lower() == "m":
            return "Gender_Male"
        else:
            return "Gender_Female"

    def __init__(self, driver):
        self.driver = driver
        self.commonMethods = CommonFunctions(self.driver)


    def selectSubCategory(self, category):
        index = 1
        if category.lower() == 'customer':
            index = 2
        self.commonMethods.waitForVisible(self.text_sideNavBar_customers_xpath, self.min_wait)
        self.commonMethods.acceptAlerts()
        self.commonMethods.clickElement(self.text_sideNavBar_customers_xpath)
        self.commonMethods.waitForVisible(self.sub_category_xpath(category, index), self.min_wait)
        self.commonMethods.clickElement(self.sub_category_xpath(category, index))


    def clickAddNewButton(self):
        self.commonMethods.waitForVisible(self.button_AddNew_xpath, self.min_wait)
        self.commonMethods.clickElement(self.button_AddNew_xpath)

    def validatePageTitle(self, title):
        self.commonMethods.waitForVisible(self.page_title(title), self.min_wait)

    def fillUserDetails(self):
        self.commonMethods.fillLocatorById("Email", gf.get_test_email())
        self.commonMethods.fillLocatorById("Password", gf.get_test_password())
        self.commonMethods.fillLocatorById("FirstName", gf.get_test_username().split(' ')[0])
        self.commonMethods.fillLocatorById("LastName", gf.get_test_username().split(' ')[1])
        self.commonMethods.clickLocatorById(self.select_gender(gf.get_random_gender()))
        self.commonMethods.fillLocatorById("DateOfBirth", '11/10/1981')
        self.commonMethods.fillLocatorById("Company", gf.get_test_username())
        self.commonMethods.fillLocatorById("AdminComment", gf.get_random_status())
        self.commonMethods.pressButton("save")

    def getAlertText(self):
        return self.commonMethods.getTextFromLocator("(//div[contains(@class,'alert')])[1]").strip()











