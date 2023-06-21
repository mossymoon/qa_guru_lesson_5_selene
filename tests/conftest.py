import pytest
from selene.support.shared import browser
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function', autouse=True)
def browser_window():
    browser.config.base_url = 'https://demoqa.com/'
    driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless')
    browser.config.type_by_js = True
    browser.config.driver_options = driver_options
    browser.config.driver = webdriver.Chrome(
        service=ChromeService(executable_path=ChromeDriverManager().install()),
        options=driver_options)
    yield
    browser.quit()
