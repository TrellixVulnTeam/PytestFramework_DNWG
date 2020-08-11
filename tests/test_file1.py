from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from tasks.CheckElementPresent import is_element_present
from tasks.DemoListButtons import clickDemoBtn
import pytest


@pytest.mark.usefixtures("driver_init")
class Test1:

    def test_check_title(self):
        assert "Selenium Easy" in self.driver.title
        # raise NotImplementedError

    def test_side_nav_present(self):
        assert is_element_present(self.driver, By.XPATH, "//div[@class='panel panel-default']") is True
        # raise NotImplementedError

    def test_board_present(self):
        assert is_element_present(self.driver, By.XPATH, "//div[@class='row']//div[@class='board']") is True
        # raise NotImplementedError

    def test_all_demo_btn_present(self):
        demo_btn_list = ["Simple Form Demo", "Check Box Demo", "Radio Buttons Demo", "Select Dropdown List",
                         "Javascript Alerts", "Window Popup Modal", "Bootstrap Alerts", "Bootstrap Modals"]

        clickDemoBtn(self.driver)
        for item in demo_btn_list:
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_link_text(item)).perform()
            assert is_element_present(self.driver, By.PARTIAL_LINK_TEXT, item) is True

    def test_get_input(self):
        clickDemoBtn(self.driver)
        self.driver.find_element_by_link_text("Simple Form Demo").click()
        message = "Hello there"
        self.driver.find_element_by_xpath("//*[@id='get-input']//input").send_keys(message)
        self.driver.find_element_by_xpath("//*[@id='get-input']//*[@class='btn btn-default']").click()
        get_text = self.driver.find_element_by_xpath("//*[@id='user-message']//span").text
        assert message == get_text

    def test_get_input_total(self):
        num1, num2 = 15, 23
        self.driver.find_element_by_xpath("//*[@id='sum1']").send_keys(num1)
        self.driver.find_element_by_xpath("//*[@id='sum2']").send_keys(num2)
        self.driver.find_element_by_xpath("//*[@id='gettotal']//*[@class='btn btn-default']").click()
        get_text = self.driver.find_element_by_xpath("//*[@id='displayvalue']").text
        assert str(num1+num2) == get_text



