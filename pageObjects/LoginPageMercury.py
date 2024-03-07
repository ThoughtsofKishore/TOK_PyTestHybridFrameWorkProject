from selenium.webdriver.common.by import By

class LoginPage:
    txt_username_name = 'userName'
    txt_password_name = 'password'
    button_submit_name = 'submit'
    lnk_sign_off_lnkText = 'SIGN-OFF'

    def __init__(self, driver):
        self.driver = driver


    def set_username(self, username):
        self.driver.find_element(By.NAME, self.txt_username_name).clear()
        self.driver.find_element(By.NAME,self.txt_username_name).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.NAME, self.txt_password_name).clear()
        self.driver.find_element(By.NAME,self.txt_password_name).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(By.NAME,self.button_submit_name).click()

    def click_signoff_link(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_sign_off_lnkText).click()


