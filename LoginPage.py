class LoginPage:
    # Login Page
    textbox_email_xpath = "/html/body/div/div/form/div[1]/input"
    textbox_password_xpath = "/html/body/div/div/form/div[2]/input"
    button_login_xpath = "/html/body/div/div/form/div[3]/button"
   
    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, email):
        self.driver.find_element_by_xpath(self.textbox_email_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
