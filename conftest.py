import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from fixtures.pages.app_shop import ShopApplication
from tests.test_search import shop_logger


@pytest.fixture()
def shop_application(request):
    # url
    url = request.config.getoption("--shop_url")
    headless = request.config.getoption("--headless_option")

    # Опции драйвера
    chrome_options = Options()
    chrome_options.headless = headless

    # Драйвер
    driver = webdriver.Chrome(ChromeDriverManager().install())
    shop_logger.info(f'Open browser with URL {url}')

    shop = ShopApplication(driver, url)
    yield shop
    shop.quit()
    shop_logger.info(f'End session. Close browser')


def pytest_addoption(parser):
    parser.addoption("--shop_url", action="store",
                     default="https://berpress.github.io/online-grocery-store/", help="site url"),
    parser.addoption("--headless_option", action="store",
                     default="false", help="headless status")
