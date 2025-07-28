# # Pytest setup/teardown

import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait


Base_url = "https://staging.trsc.nic.in/finance/ehrmis/"

# If one doesn't want to hard code the url, one can write it in command line
# pytest tests/ --browser=chrome --base-url=https://your-url

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")

@pytest.fixture(scope="session")  # change this to session or module from function
def driver(request):
    browser = request.config.getoption("--browser")
    driver = get_driver(browser)
    driver.get(Base_url)
    driver.implicitly_wait(20)
    yield driver
    driver.quit()

### use this for all other pages apart from login - meaning after the login is successful
@pytest.fixture(scope="session")
def login_successfully(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("baro000066")
    login_page.enter_password("Test@123")
    login_page.enter_captcha("01042025")
    login_page.click_login()
    assert "Welcome" in driver.page_source
    return driver
    ## check whether its dashboard or something else

    # WebDriverWait(driver, 10).until(lambda d: "Welcome" in d.current_url)
    # return driver

## both fixture needs to be in either - function or session  -
# for login page - use functions and for all other pages use session
## NOTE : both fixture needs to be in either - function or session for the test cases to execute.
# for login page - use functions and for all other pages use session for testing the test cases (each method)

### driver fixture (session scope): Initializes the WebDriver for the selected browser,
# opens the base URL, sets implicit waits, and ensures cleanup after the session.
# This is the shared driver used across all test cases, so that you can directly use it in your test cases
