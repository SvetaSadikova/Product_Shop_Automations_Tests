from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from fixtures.pages.base_page import BasePage


class SearchProduct(BasePage):

    def __search_input(self) -> WebElement:
        return self.find_element_method(locator_name=(By.ID, 'email_inline'), wait_time=3)

    def __search_button(self) -> WebElement:
        return self.find_element_method(locator_name=(By.CLASS_NAME, 'search-btn'))

    def search_product(self, product_name):
        """
        Функция поиска
        """
        self.__search_input().send_keys(product_name)
        self.__search_button().click()
