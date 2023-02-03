from selenium.webdriver.common.by import By
from utilities import CommonMethods

class Login:

    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "(//button[@type='submit'])[1]"
    link_logout_linkText = "Logout"
    heading_dashboard_xpath = "(//h1[contains(text(),'Dashboard')])[1]"
    title_loginPage_xpath = "(//*[contains(text(),'Welcome, please sign in')])[1]"
    text_errorMessage_xpath = "(//div[contains(@class, 'message-error')])[1]"


    def __init__(self, driver):
        self.driver = driver
        #super(driver)


    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)


    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linkText).click()

    def checkFailedLoginErrorMessage(self):
        print("*******",self.driver.find_element(By.XPATH, self.text_errorMessage_xpath).text)
        assert self.driver.find_element(By.XPATH, self.text_errorMessage_xpath).text == "Login was unsuccessful. Please correct the errors and try again."


