from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, shop):
        self.BP_app = shop

    def find_element_method(self, locator_name, wait_time=10):
        my_element = WebDriverWait(self.BP_app.MyDriver, wait_time).until(
            EC.presence_of_element_located(locator_name),
            message=f"Can't find element by locator {locator_name}"
        )
        return my_element

    def click_method(self, locator_name, wait_time=10):
        my_element = WebDriverWait(self.BP_app.MyDriver, wait_time).until(
            EC.presence_of_element_located(locator_name),
            message=f"Can't find element by locator {locator_name}"
        )
        my_element.click(self)

    def input_data_method(self, locator_name, wait_time=10):
        pass
