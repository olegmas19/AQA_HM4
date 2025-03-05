import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.driver.set_window_size(1700, 1280)
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "125.0",
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }

    options.capabilities.update(selenoid_capabilities)
    browser.config.driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options,
    )
    yield browser
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()


def removing_banner():
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")


#  browser.config.driver = driver


#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": "100.0",
#         "selenoid:options": {"enableVideo": True, "enableVNC": True},
#     }
#     options.capabilities.update(selenoid_capabilities)
#     driver = webdriver.Remote(
#         command_executor="https://selenoid.autotests.cloud/wd/hub", options=options
#     )
#     browser = Browser(Config(driver=driver))
#     browser.config.base_url = 'https://demoqa.com/automation-practice-form'
#     yield browser
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#     attach.add_html(browser)
#     attach.add_video(browser)
#     browser.quit()


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
#
