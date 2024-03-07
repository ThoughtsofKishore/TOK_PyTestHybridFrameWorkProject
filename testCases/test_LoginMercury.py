import pytest
from pageObjects.LoginPageMercury import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_LoginMercury:

    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    loggerObj = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.loggerObj.info("*********  Test_001_LoginMercury  *************************")
        self.loggerObj.info("*********  Verifying HomePage Title of Mercury Tours  *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == 'Welcome: Mercury Tours':
            self.driver.close()
            self.loggerObj.info("************  HomePageTitle Test is Passed  ********************")
            assert True
        else:
            self.driver.save_screenshot('./Screenshots/homePageTitleError.png')
            self.driver.close()
            self.loggerObj.error("***********  HomePageTitle Test is Failed  ********************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginMercury(self, setup):
        self.loggerObj.info("***************  Verifying Mercury Tours Login ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lpObj = LoginPage(self.driver)
        self.lpObj.set_username(self.username)
        self.lpObj.set_password(self.password)
        self.lpObj.click_submit_button()
        act_title = self.driver.title

        if act_title == 'Login: Mercury Tours':
            self.driver.close()
            self.loggerObj.info("*************************  Mercury Tours Login Test is Passed  ********************")
            assert True
        else:
            self.driver.save_screenshot('./Screenshots/loginMercuryError.png')
            self.driver.close()
            self.loggerObj.error("************************* Mercury Tours Login Test is Failed  ********************")
            assert False


