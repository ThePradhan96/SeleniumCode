from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ForgotPage:

    def __init__(self, driver):
        self.driver = driver

    # --- Tabs ---
    reset_password_tab = (By.XPATH, "//button[normalize-space()='Reset Password']")
    find_username_tab = (By.XPATH, "//button[normalize-space()='Find Username']")

    # --- Reset Password Fields ---
    #username_input = (By.XPATH, "//span[text()='Username']")

    #username_input =  (By.XPATH, "//span[text()='Username']/ancestor::fieldset/preceding-sibling::input")
    username_input = (By.XPATH, "//legend/span[text()='Username']/ancestor::fieldset/preceding-sibling::input")

    captcha_input  = (By.XPATH, "//input[@placeholder='Type the CAPTCHA above']")
    Send_otp_btn  = (By.XPATH, "//button[normalize-space()='Send OTP']")
    otp_input = (By.XPATH, "//input[@placeholder='Enter the OTP sent to your mobile']")
    verify_otp_btn = (By.XPATH, "//button[normalize-space()='verify OTP']'")
    cancel_btn  = (By.XPATH, "//button[normalize-space()='Cancel']")

    # --- Find Username Fields ---
    mobile_input    = (By.XPATH, "//input[@placeholder='Enter 10-digit mobile number']")
    user_captcha_input   = (By.XPATH, "//input[@placeholder='Type the CAPTCHA above']")
    user_submit_btn   = (By.XPATH, "//button[normalize-space()='Submit']")
    find_success_msg = (By.XPATH, "//div[contains(text(),'If your mobile number is registered,"
                                  " a message with your username has been sent to your registered mobile number']")
    user_cancel_btn   = (By.XPATH, "//button[normalize-space()='Cancel']")

    # --- Reset Password Actions ---

    def reset_password_send_otp(self):
        self.driver.find_element(*self.Send_otp_btn).click()


    def reset_password_username(self, username):
        #self.driver.find_element(*self.username_input).send_keys(username)
        #self.driver.find_element(*self.Send_otp_btn).click()
        elem = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.username_input)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)
        elem.clear()
        elem.send_keys(username)

    def reset_password_captcha(self,captcha):
        self.driver.find_element(*self.captcha_input).send_keys(captcha)
        #self.driver.find_element(*self.Send_otp_btn).click()

    def enter_otp(self, otp):
        self.driver.find_element(*self.otp_input).send_keys(otp)

    def click_verify_otp(self):
        self.driver.find_element(*self.Send_otp_btn).click()

    def verify_otp(self):
        self.driver.find_element(*self.verify_otp_btn).click()


    def cancel_reset_password(self):
        self.driver.find_element(*self.cancel_btn).click()

    # --- Find Username Actions ---
    def switch_to_find_username_tab(self):
        self.driver.find_element(*self.find_username_tab).click()

    def find_username_mobile(self, mobile):
        self.driver.find_element(*self.mobile_input).send_keys(mobile)
        #self.driver.find_element(*self.user_submit_btn).click()

    def find_username_captcha(self, captcha):
        self.driver.find_element(*self.captcha_input).send_keys(captcha)
        #self.driver.find_element(*self.user_submit_btn).click()


    def reset_username_user_submit_btn(self):
        self.driver.find_element(*self.user_submit_btn).click()

    def get_find_username_success_message(self):
        return self.driver.find_element(*self.find_success_msg).text

    def cancel_find_username(self):
        self.driver.find_element(*self.user_cancel_btn).click()
