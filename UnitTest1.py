from selenium import webdriver
import unittest2
import HtmlTestRunner


class LoginHRM(unittest2.TestCase):

    # because of decorator @classmethod and setupclass cls is decaled instead self
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="//Users//darshanirayajiwala//Documents//PycharmProjects//UnitTestHTMLReport//Drivers//chromedriver")
        cls.driver.maximize_window()


    def test_title(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.assertEqual("OrangeHRM", self.driver.title, "Not Matching")


    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title == "OrangeHRM"


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest2.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="//Users//darshanirayajiwala//Documents//PycharmProjects//UnitTestHTMLReport1//Reports"))
