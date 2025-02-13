import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_open():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.driver.set_window_size(1700, 1280)
    yield
    browser.quit()