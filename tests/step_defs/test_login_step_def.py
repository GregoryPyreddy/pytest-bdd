
import time 
from pytest_bdd import given, scenario, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@scenario('../features/login.feature', 'Login with valid credentials')
def test_login():
    pass

@given('I am on the login page')
def step_given(browser):
    browser.driver.get('<url>')

@when('I enter my username and password')
def step_when(browser):
    browser.wait.until(EC.element_to_be_clickable((By.ID, 'username')))
    browser.driver.find_element(By.ID, 'username').send_keys('######')
    browser.driver.find_element(By.ID, 'login-pwd').send_keys('########')
    time.sleep(10)

@when(parsers.parse('I click the "{element}" button'))
def step_when(browser, element):
    button_locator = (By.ID, element)
    browser.driver.find_element(*button_locator).click()
