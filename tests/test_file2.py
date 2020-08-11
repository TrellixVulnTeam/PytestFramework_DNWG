import pytest
import random
from tasks.DemoListButtons import clickDemoBtn


@pytest.mark.usefixtures("driver_init")
class Test2:

    def test_single_check_box(self):
        clickDemoBtn(self.driver)
        self.driver.find_element_by_link_text("Check Box Demo").click()
        ele_box = self.driver.find_element_by_xpath("//*[@id='isAgeSelected']")
        box_res = ele_box.is_selected()
        assert box_res is False
        ele_box.click()
        box_res = ele_box.is_selected()
        assert box_res is True
        assert "Success - Check box is checked" == self.driver.find_element_by_xpath("//*[@id='txtAge']").text

    def test_multiple_check_box(self):
        check_all_btn = self.driver.find_element_by_id("check1")
        check_all_btn.click()
        assert "Uncheck All" == check_all_btn.get_attribute('value')

        ran_num = random.randint(1, 4)
        option_xpath = "//div[@class='panel panel-default']//div[@class='panel-body']//div[@class='checkbox'][" +\
                      str(ran_num) + "]//input[@class='cb1-element'] "
        self.driver.find_element_by_xpath(option_xpath).click()
        assert "Check All" == self.driver.find_element_by_id("check1").get_attribute('value')





