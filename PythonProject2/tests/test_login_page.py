import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver")
class TestLogin:
    correct_username = "snrt000723"
    correct_password = "Snrt@000723"
    incorrect_username = "Someuser1"
    incorrect_password = "123Pass"

    # ## test the title of the website :: TESTED 6/11
    def test_title(self, driver):
        login_page = LoginPage(driver)
        assert login_page.verify_title()

##TESTED :: 6/11
    # ## input all valid credentials and click log in ::
    def test_login_success(self,driver):
        login_page = LoginPage(driver)
        login_page.enter_username(self.correct_username)
        login_page.enter_password(self.correct_password)
        login_page.enter_captcha("01042025")
        login_page.click_login()
        assert "Welcome" in driver.page_source

##::TESTED :: 6/11
    # ## leave the username field blank and log in
    def test_login_missing_username(self,driver):
        login_page = LoginPage(driver)
        login_page.enter_password(self.correct_password)
        login_page.enter_captcha("01042025")
        login_page.click_login()
        try:
            error_message = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Username is required')]"))
            )
            assert error_message.is_displayed(), "Expected error message for missing username not displayed"
        except:
            pytest.fail("Missing username error not found after clicking login")
        #assert "Username is required" in driver.page_source

##tested :: 6/11
    ## leave the password field blank and log in
    def test_login_missing_password(self,driver):
        login_page = LoginPage(driver)
        login_page.enter_username(self.correct_username)
        login_page.enter_captcha("01042025")
        login_page.click_login()
        try:
            error_message = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Password is required')]"))
            )
            assert error_message.is_displayed(), "Expected error message for missing password not displayed"
        except:
            pytest.fail("Missing password error not found after login attempt")
        #assert "Password is required" in driver.page_source

##TESTED :: 6/11
    # ## leave the captcha blank and log in
    def test_login_missing_captcha(self,driver):
        login_page = LoginPage(driver)
        login_page.enter_username(self.correct_username)
        login_page.enter_password(self.correct_password)
        login_page.click_login()
        try:
            error_message = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Captcha is Required')]"))
            )
            assert error_message.is_displayed(), "Expected error message for missing captcha not displayed"
        except:
            pytest.fail("Captcha validation error not shown after login attempt")
        #assert "Captcha is Required" in driver.page_source

##TESTED :: 6/11
    #validate the password typed is masked
    def test_password_should_be_masked(self,driver):
        login_page = LoginPage(driver)
        assert login_page.is_password_masked()

        # login_page.enter_password("SomeSecret123")  # optional, just to confirm value doesn't affect type
        # password_input = driver.find_element(*login_page.password_input)
        # input_type = password_input.get_attribute("type")
        #
        # assert input_type == "password", f"Expected password input to be masked, but got type='{input_type}'"


##TESTED :: 6/11
    #validate that on toggle of eye icon the password is visible
    def test_password_visibility_toggle(self,driver):
        login_page = LoginPage(driver)
        login_page.toggle_password_visibility()
        assert login_page.is_password_visible()


##TESTED :: 6/11
      # enter all invalid credentials in the input fields and correct captcha
    def test_login_invalid_credential(self,driver):
        login_page = LoginPage(driver)
        login_page.enter_username(self.incorrect_username)
        login_page.enter_password(self.incorrect_password)
        login_page.enter_captcha("01042025")
        login_page.click_login()
        # --- WAIT FOR 5 SEC TO FIND THE TOASTER MSG --
        # wait = WebDriverWait(driver, 2)
        # toast = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid credentials')]")))
        # assert "Invalid credentials" in toast.text

        # Step 3: Wait for error toast to appear
        try:
            toast = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid credentials')]"))
            )
            assert "Invalid credentials" in toast.text, "Expected 'Invalid credentials' message not found"
        except:
            pytest.fail("Login error toast not shown for invalid credentials")


## TESTED :: 6/11
    ##enter only incorrect username - shows Invalid credentials
    def test_login_invalid_username(self,driver):
        login_page = LoginPage(driver)
        login_page.enter_username(self.incorrect_username)
        login_page.enter_password(self.correct_password)
        login_page.enter_captcha("01042025")
        login_page.click_login()
        # --- WAIT FOR 5 SEC TO FIND THE TOASTER MSG --
        # wait = WebDriverWait(driver, 2)
        # toast = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid credentials')]")))
        # assert "Invalid credentials" in toast.text

        try:
            toast = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid credentials')]"))
            )
            assert "Invalid credentials" in toast.text, "Expected 'Invalid credentials' message not displayed"
        except:
            pytest.fail("Toast message for invalid username not shown")

# if a password less than or equal to 5 charc
    ## enter only incorrect password
    # def test_login_short_password(self,driver):
    #     login_page = LoginPage(driver)
    #     login_page.enter_username("sida000347")
    #     login_page.enter_password("123")
    #     login_page.enter_captcha("876")
    #     login_page.click_login()
    #     assert "Invalid password" in driver.page_source

    # --- if the password is greater than 5 charc  but is incorrect
    # def test_login_invalid_password(self,driver):
    #     login_page = LoginPage(driver)
    #     login_page.enter_username("sida000347")
    #     login_page.enter_password("1234567")
    #     login_page.enter_captcha("876")
    #     login_page.click_login()
    #
    #     #--- WAIT FOR 10 SEC TO FIND THE TOASTER MSG --
    #     wait = WebDriverWait(driver, 10)
    #     toast = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Invalid credentials')]")))
    #     assert "Invalid credentials" in toast


##tested :: 6/11
# ## enter only invalid captcha
    def test_login_invalid_captcha(self,driver):
        login_page = LoginPage(driver)
        login_page.enter_username(self.correct_username)
        login_page.enter_password(self.correct_password)
        login_page.enter_captcha("1233")
        login_page.click_login()
        # --- WAIT FOR 5 SEC TO FIND THE TOASTER MSG --
        # wait = WebDriverWait(driver, 2)
        # toast = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid Captcha')]")))
        # assert "Invalid Captcha" in toast.text

        try:
            toast = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid Captcha')]"))
            )
            assert "Invalid Captcha" in toast.text, "Expected 'Invalid Captcha' error message not displayed"
        except:
            pytest.fail("No toast message displayed for invalid captcha input")



#TESTED :: 6/11
    def test_login_all_field_blank(self,driver):
        login_page = LoginPage(driver)
        login_page.click_login()
        page_current = driver.page_source
        assert "Username is required" in page_current, "Expected validation for missing username not found"
        assert "Password is required" in page_current, "Expected validation for missing password not found"
        assert "Captcha is Required" in page_current, "Expected validation for missing captcha not found"
