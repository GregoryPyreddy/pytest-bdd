import pytest
import configparser
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Get the directory of the current file (conftest.py)
current_dir = os.path.dirname(os.path.realpath(__file__))
# Navigate to the root directory
root_dir = os.path.abspath(os.path.join(current_dir, "../.."))
# Path to the config.ini file
config_file = os.path.join(root_dir, "config.ini")

def pytest_addoption(parser):
    config = configparser.ConfigParser()
    config.read("config.ini")
    browser_default = config.get("pytest", "browser", fallback="chrome")
    test_case_default = config.get("pytest", "test_case", fallback="login_test")
    time_out_default = config.get("pytest", "time_out", fallback="10")

    parser.addoption("--browser", action="store", default=browser_default, help="Specify the browser")
    parser.addoption("--test-case", action="store", default=test_case_default, help="Specify the test case")
    parser.addoption("--time-out", action="store", default=time_out_default, help="Specify the timeout in seconds")

@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    return browser

@pytest.fixture
def test_case(request):
    test_case = request.config.getoption("--test-case")
    return test_case

@pytest.fixture(scope="session")
def browser(request):
    browser_choice = request.config.getoption("--browser")
    time_out = request.config.getoption("--time-out")
    if browser_choice == "chrome":
        driver = webdriver.Chrome()
    elif browser_choice == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"Browser '{browser_choice}' is not supported")
    wait = WebDriverWait(driver, time_out)
    yield TestContext(driver, wait)

    # Teardown: Close the browser after all tests
    driver.quit()

class TestContext:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait