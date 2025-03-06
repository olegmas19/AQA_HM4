import pytest
from requests import options
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config


#
#
# @pytest.fixture(scope="function", autouse=True)
# def browser_open():
#     driver_options = webdriver.ChromeOptions()
#     driver_options.page_load_strategy = 'eager'
#     browser.config.driver_options = driver_options
#     browser.config.base_url = 'https://demoqa.com/automation-practice-form'
#     browser.driver.set_window_size(1700, 1280)
#
#     yield
#     browser.quit()
#
#
# def removing_banner():
#     browser.driver.execute_script("$('#fixedban').remove()")
#     browser.driver.execute_script("$('footer').remove()")


@pytest.fixture(scope="function")
def setup_open():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "125.0",
        "selenoid:options": {"enableVideo": True, "enabledVNC": True},
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options,
    )

    browser = Browser(Config(driver))
    yield browser
    browser.quit()
