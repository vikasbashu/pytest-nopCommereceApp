from utilities.CommonMethods import CommonFunctions
from utilities import GenericFunctions as gf

class AddVendors:

    id_name = 'Name'
    xpath_description = "(//*[@data-id='Description'])[1]"
    xpath_iframe_description = "(//iframe[@id='Description_ifr'])[1]"
    id_email = 'Email'
    id_status = 'Active'

    def __init__(self, driver):
        self.driver = driver
        self.commonMethods = CommonFunctions(driver)

    def fillVendorDetails(self):
        self.commonMethods.fillLocatorById(self.id_name, gf.get_test_username())
        self.commonMethods.switchToIframe(self.xpath_iframe_description)
        self.commonMethods.fillLocatorByXpath(self.xpath_description, gf.getProducts()[0])
        self.commonMethods.switchToParent()
        self.commonMethods.fillLocatorById(self.id_email, gf.get_test_email())
