from utilities.CommonMethods import CommonFunctions

class SearchCustomer:

    input_email_id = "SearchEmail"
    input_firstName_id = "SearchFirstName"
    input_lastName_id = "SearchLastName"
    button_search_id = "search-customers"
    table_output_index = {
        'noData': '1',
        'email': "2",
        'name': "3",
        'roles': "4",
        'company': "5",
        'active': "6",
        'edit': "7"
    }
    search_criteria = 'noData'
    search_value = ''
    search_result_xpath = "(//*[@id='customers-grid']/tbody/tr[{}]/td)[{}]"


    def __init__(self , driver):
        self.driver = driver
        self.commonMethods = CommonFunctions(self.driver)

    def fillEmailField(self, email):
        self.commonMethods.fillLocatorById(self.input_email_id, email)
        self.search_criteria = "email"
        self.search_value = email

    def fillFirstNameField(self, firstName):
        self.commonMethods.fillLocatorById(self.input_firstName_id, firstName)
        self.search_criteria = "name"
        self.search_value = firstName

    def fillLastNameField(self, lastName):
        self.commonMethods.fillLocatorById(self.input_lastName_id, lastName)
        self.search_criteria = "name"
        self.search_value = lastName

    def searchRecords(self):
        self.commonMethods.clickLocatorById(self.button_search_id)

    def getOutputResult(self):
        self.commonMethods.wait(5)
        return self.commonMethods.getTextFromLocator(self.search_result_xpath.format(1, self.table_output_index[self.search_criteria]))



