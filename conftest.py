import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from selene.support.shared import browser
from utils import attach

DEFAULT_BROWSER_VERSION = "100.0"


@pytest.fixture(scope='function')
def browser_managemento():
    print('Starting browser')
    browser.config.wait_for_no_overlap_found_by_js = True

    browser.config.browser_name = 'chrome'
    browser.config.hold_browser_open = False
    browser.config.timeout = 3
    browser.config.window_width = 1700
    browser.config.window_height = 1200


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        # command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    # browser = Browser(Config(driver))
    browser.config.driver = driver

    yield browser
    # даже если тест упадет закрепы будут в отсчете
    attach.add_html(browser)
    attach.add_screenshoot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()




"""
@pytest.fixture()
def open_auto_practice_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.should(have.title('ToolsQA'))
    browser.element('[class="main-header"]').should(have.text('Practice Form'))


@pytest.fixture()
def open_webtables_page():
	browser.open('https://demoqa.com/webtables')
	browser.should(have.title('ToolsQA'))
	browser.element('[class="main-header"]').should(have.text('Web Tables'))
"""