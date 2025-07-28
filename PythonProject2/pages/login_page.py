from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

## selectors for the login page
    page_title = "NextGen eHRMIS"
    username_input = (By.NAME , "loginId")
    password_input = (By.NAME, "password")
    eye_icon = (By.XPATH, "//button[@aria-label='toggle password visibility']")
    captcha_input = (By.NAME, "captcha")
    login_btn = (By.CSS_SELECTOR, "button[type='submit']")
    forget_cred = (By.XPATH, "//span[text()='Forgot Password/Username?']")




    def verify_title(self):
        return self.driver.title == self.page_title

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

      ## check this input_type
    def is_password_masked(self):
        input_type = self.driver.find_element(*self.password_input).get_attribute("type")
        return input_type == "password"

    def toggle_password_visibility(self):
        self.driver.find_element(*self.eye_icon).click()

    def is_password_visible(self):
        input_type = self.driver.find_element(*self.password_input).get_attribute("type")
        return input_type == "text"

    def enter_captcha(self, captcha_value):
        self.driver.find_element(*self.captcha_input).send_keys(captcha_value)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()

    def click_forget(self):
        self.driver.find_element(*self.forget_cred).click()


