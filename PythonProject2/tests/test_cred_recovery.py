import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.cred_recovery import ForgotPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
class TestForgot:

##TESTED :: 6/11

    def test_navigate_to_forgot_page(self, driver):
        login = LoginPage(driver)
        login.click_forget()
        forgot = ForgotPage(driver)
        assert driver.find_element(*forgot.reset_password_tab).is_displayed(), "Reset Password tab not visible"



    # --- fill in the captcha and leave the username blank
    # ## now shows only captcha is required , though username is blank -- check msg
##tested :: 6/16
    def test_reset_password_missing_username(self, driver):
        login = LoginPage(driver)
        login.click_forget()
        forgot = ForgotPage(driver)
        forgot.reset_password_captcha("01042025")
        forgot.click_verify_otp()
        try:
            toast = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid credentials')]"))
            )
            assert "Invalid credentials" in toast.text, "Expected 'Invalid credentials' error not shown"
        except:
            pytest.fail("No error message shown when resetting password with missing username")
        #wait = WebDriverWait(driver, 2)
        #toast = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid credentials')]")))
        # assert "Invalid credentials"


    # -- fill in the username and leave the captcha blank
    def test_reset_password_missing_captcha(self, driver):
        login = LoginPage(driver)
        login.click_forget()
        forgot = ForgotPage(driver)
        forgot.reset_password_username("PPPOO")
        forgot.click_verify_otp()
        assert "Captcha is required" in driver.page_source  ## update it later

# tested
    # -- leave both username and captcha blank and submit
    def test_reset_password_missing_fields(self, driver):
        login = LoginPage(driver)
        login.click_forget()
        forgot = ForgotPage(driver)
        forgot.reset_password_send_otp()
        assert "Captcha is required" in driver.page_source
    ###   assert "Username is required" in driver.page_source ##- not implemented yet

    # # ---entire positive flow of the username recovery
    def test_reset_password_otp_verification(self, driver):
        login = LoginPage(driver)
        login.click_forget()
        forgot = ForgotPage(driver)
        forgot.reset_password_username("valid_username")
        forgot.reset_password_captcha("")
        forgot.reset_password_send_otp()
        forgot.enter_otp("")
        forgot.verify_otp()
    #     assert "verified SOMETHING" in driver.page_source  # CHANGE THIS
    #

    ## -- enter invalid username --- NOT implemented yet
    def test_reset_password_invalid_username(self, driver):
        login = LoginPage(driver)
        login.click_forget()
        forgot = ForgotPage(driver)
        forgot.reset_password_username("invalid_username")
        forgot.reset_password_captcha("")
        forgot.reset_password_send_otp()
        assert "Invalid Username" in driver.page_source


    ##--- click on send otp button and without filling the OTP, click on verify otp button
    def test_reset_password_otp_blank(self, driver):
        login = LoginPage(driver)
        login.click_forget()
        forgot = ForgotPage(driver)
        forgot.reset_password_username("valid_username")
        forgot.reset_password_captcha("")
        forgot.reset_password_send_otp()
        forgot.verify_otp()
        assert "OTP is required" in driver.page_source
#
# # tested
    def test_reset_password_cancel_returns_to_login(self, driver):
        login = LoginPage(driver)
        login.click_forget()
        forgot = ForgotPage(driver)
        forgot.cancel_reset_password()
        assert login.verify_title(), " Did not return to login page"

# --------------------------------------- #

    def test_find_username_positive(self, driver):
        login = LoginPage(driver)
        login.click_forget()
        forgot = ForgotPage(driver)
        forgot.switch_to_find_username_tab()
        forgot.find_username_mobile("9876543210")
        forgot.find_username_captcha("")
        forgot.reset_username_user_submit_btn()
        message = forgot.get_find_username_success_message()
        assert "Success!" in message
        ##---assert "username" in driver.page_source.lower()  # change this


##TESTED :: 6/16
    def test_no_mobile_captcha(self,driver):
        login = LoginPage(driver)
        login.click_forget()
        forgot = ForgotPage(driver)
        forgot.switch_to_find_username_tab()
        forgot.reset_username_user_submit_btn()
        assert "Invalid Request" in driver.page_source




    def test_find_username_missing_mobile(self, driver):

        login = LoginPage(driver)
        login.click_forget()
        forgot = ForgotPage(driver)
        forgot.switch_to_find_username_tab()
        forgot.find_username_captcha("")
        forgot.reset_username_user_submit_btn()
        assert "required" in driver.page_source ##shows invalid request for now

    def test_find_username_missing_captcha(self, driver):
        login = LoginPage(driver)
        login.click_forget()
        forgot = ForgotPage(driver)
        forgot.switch_to_find_username_tab()
        forgot.find_username_mobile("")
        forgot.reset_username_user_submit_btn()
        assert "required" in driver.page_source

## Input less than 10 digits in the mobile number field
    def test_find_username_invalid_mobile(self, driver):
        login = LoginPage(driver)
        login.click_forget()
        forgot = ForgotPage(driver)
        forgot.switch_to_find_username_tab()
        forgot.find_username_mobile("123456")
        forgot.reset_username_user_submit_btn()
        assert "required" in driver.page_source

## input charc in mobile number
    def test_find_username_invalid_mobile_char(self, driver):
        login = LoginPage(driver)
        login.click_forget()
        forgot = ForgotPage(driver)
        forgot.switch_to_find_username_tab()
        forgot.find_username_mobile("qwerty")
        forgot.reset_username_user_submit_btn()
        assert "required" in driver.page_source

    def test_find_username_missing_fields(self, driver):
        login = LoginPage(driver)
        login.click_forget()
        forgot = ForgotPage(driver)
        forgot.switch_to_find_username_tab()
        #forgot.reset_username_missing_field()
        assert "Invalid Request" in driver.page_source

# tested
    def test_find_username_cancel_returns_to_login(self, driver):
        login = LoginPage(driver)
        login.click_forget()
        forgot = ForgotPage(driver)
        forgot.switch_to_find_username_tab()
        forgot.cancel_find_username()
        assert login.verify_title(), "Did not return to login page"

