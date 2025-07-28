
from datetime import datetime, time
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FIRST_NAMES = ["Amit", "Priyanshi", "Rohan", "SnehaK", "Vikas", "Neha"]
MIDDLE_NAMES = ["Kumar", "Raj", "Singh", "Devi", "Das", ""]
LAST_NAMES = ["Sharma", "Verma", "Mehta", "Kapoor", "Chopra", "Reddy"]

class AddNewEmployeePage:
    ## iska driver hoga ua login_succ hoga dekhna
    def __init__(self, driver):
        self.driver = driver

    # Navigation elements from dashboard to employee _management to add new emp tab
    employee_management_tab = (By.XPATH, "//span[text()='Employee Management']")
    add_new_emp_tab = (By.XPATH, "//span[text()='Add New Employee']")
    dashboard = (By.XPATH, "//span[text()='Dashboard']")

    # Add new employee fields
    ##-- personal information
    service_class_dd = (By.ID, "mui-component-select-serviceClassificationId")
    select_office_dd = (By.ID, "mui-component-select-officeId")
    title_dd = (By.ID, "mui-component-select-initial")
    first_name_input = (By.NAME, "firstName")
    middle_name_input = (By.NAME, "middleName")
    last_name_input = (By.NAME,"lastName")
    father_name_input = (By.NAME, "fatherName")
    mother_name_input = (By.NAME, "motherName")
    male_radio = (By.XPATH, "//input[@name='gender' and @value='M']")
    female_radio = (By.XPATH, "//input[@name='gender' and @value='F']")
    other_radio = (By.XPATH, "//input[@name='gender' and @value='O']")
    DOB = (By.NAME, "dateOfBirth")
    DOB_icon_btn = (By.XPATH, "//input[@name='dateOfBirth']/following-sibling::div//button[@aria-label='Choose date']")

    #### ------- employement details --------
    recruitment_mode_dd = (By.ID, "mui-component-select-recruitmentModeId")
    app_order_date = (By.NAME, "appointmentOrderDate")
    app_order_date_calender = (By.XPATH,
        "//input[@name='appointmentOrderDate']"
        "/following-sibling::div//button[@aria-label='Choose date']")
    employement_status_dd = (By.ID, "mui-component-select-employmentStatusId")
    app_order_no_input = (By.NAME, "appointmentOrderNo")
    DOJ = (By.NAME, "dateOfJoining")
    DOJ_icon = (By.XPATH, "//input[@name='dateOfJoining']/following-sibling::div//button[@aria-label='Choose date']")
    pancard_input = (By.NAME, "panCard")
    #select_qualification_dd = (By.XPATH, "//span[text()='Select the Qualification']")
    select_qual = (By.CSS_SELECTOR,"input[role='combobox'][aria-autocomplete='list']")

    mobile_no_input = (By.NAME, "mobileNumber")
    email_input = (By.NAME, "emailAddress")
    whatsapp_same_checkbox = (By.NAME, "useWhatsappAsMobile")
    whatsapp_num_input = (By.NAME, "whatsappNumber")
    create_draft_btn = (By.XPATH, "//button[text()='Create Draft']")



    # Methods
    #navigating to the add new employee page ( should I add url of the page ??? check url ?)
    def navigate_to_add_employee(self):
        self.driver.find_element(*self.employee_management_tab).click()
        self.driver.find_element(*self.add_new_emp_tab).click()


    ### Select any random option from the list, if only one option is available - choose that
    def select_random_option(self, dropdown_locator, options_xpath):
        # Step 1: Open the dropdown
        self.driver.find_element(*dropdown_locator).click()
        # Step 2: Wait for options to appear
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, options_xpath))
        )
        # Step 3: Collect options
        options = self.driver.find_elements(By.XPATH, options_xpath)
        if not options:
            raise Exception(f"No options found in dropdown: {dropdown_locator}")
        # Step 4: Choose randomly or select the only available one
        if len(options) > 1:
            selected_option = random.choice(options[1:] if len(options) > 1 else options)
        else:
            selected_option = options[0]
        selected_text = selected_option.text
        selected_option.click()
        print(f"Selected option: {selected_text}")

    ##service_class_dd = (By.ID, "mui-component-select-serviceClassificationId")
    def select_random_service_class(self):
        #self.select_random_option(self.service_class_dd) -USED THIS BEFORE
        dropdown_locator = (By.ID, "mui-component-select-serviceClassificationId")
        options_xpath = "//ul[@role='listbox']/li"
        self.select_random_option(dropdown_locator, options_xpath)

    #select_office_dd = (By.ID, "mui-component-select-officeId")
    def select_random_office(self):
        dropdown_locator = (By.ID, "mui-component-select-officeId")
        options_xpath = "//ul[@role='listbox']/li"
        self.select_random_option(dropdown_locator, options_xpath)
        #self.select_random_option(self.select_office_dd)

    # title_dd = (By.ID, "mui-component-select-initial")
    def select_random_title(self):
        dropdown_locator =  (By.ID, "mui-component-select-initial")
        options_xpath = "//ul[@role='listbox']/li"
        self.select_random_option(dropdown_locator, options_xpath)
        #self.select_random_option(self.title_dd)

    #first_name_input = (By.NAME, "firstName")
    def enter_first_name(self,firstname):
        field = self.driver.find_element(*self.first_name_input)
        field.clear()
        field.send_keys(firstname)

    def enter_random_first_name(self):
        name = random.choice(FIRST_NAMES)
        field = self.driver.find_element(*self.first_name_input)
        field.clear()
        field.send_keys(name)
        return name

    #middle_name_input = (By.NAME, "middleName")

    def enter_middle_name(self,middlename):
        field = self.driver.find_element(*self.middle_name_input)
        field.clear()
        field.send_keys(middlename)

    def enter_random_middle_name(self):
        name = random.choice(MIDDLE_NAMES)
        field = self.driver.find_element(*self.middle_name_input)
        field.clear()
        field.send_keys(name)
        return name

    #last_name_input = (By.NAME,"lastName")
    def enter_last_name(self,lastname):
        field = self.driver.find_element(*self.last_name_input)
        field.clear()
        field.send_keys(lastname)

    def enter_random_last_name(self):
        name = random.choice(LAST_NAMES)
        field = self.driver.find_element(*self.last_name_input)
        field.clear()
        field.send_keys(name)
        return name


    # def enter_first_name(self, name):
    #     self.driver.find_element(*self.first_name_input).send_keys(name)
    #
    # def enter_middle_name(self, name):
    #     self.driver.find_element(*self.middle_name_input).send_keys(name)
    #
    # def enter_last_name(self, name):
    #     self.driver.find_element(*self.last_name_input).send_keys(name)

    #father_name_input = (By.NAME, "fatherName")
    def enter_father_name(self, name):
        self.driver.find_element(*self.father_name_input).send_keys(name)

    #mother_name_input = (By.NAME, "motherName")
    def enter_mother_name(self, name):
        self.driver.find_element(*self.mother_name_input).send_keys(name)

    ## gender --- check
    def select_random_gender(self):
        gender_options = {
            "male": self.male_radio,
            "female": self.female_radio,
            "other": self.other_radio
        }
        gender_choice = random.choice(list(gender_options.values()))
        self.driver.find_element(*gender_choice).click()


    #DOB = (By.NAME, "dateOfBirth")
    def pick_dob(self, year="2006", month="Mar", day="20"):
        wait = WebDriverWait(self.driver, 10)

        # Open calendar
        btn = self.driver.find_element(*self.DOB_icon_btn)
        self.driver.execute_script("arguments[0].click();", btn)
        #Click header once to switch to month picker
        header = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'MuiPickersCalendarHeader-label')]")))
        header.click()
        ##Click header again to switch to year picker
        time.sleep(1)
        header = self.driver.find_element(By.XPATH, "//div[contains(@class,'MuiPickersCalendarHeader-label')]")
        self.driver.execute_script("arguments[0].click();", header)

        year_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//button[@role='radio' and normalize-space(text())='{year}']")))
        self.driver.execute_script("arguments[0].click();", year_btn)

        month_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//button[@role='radio' and starts-with(@aria-label, '{month}')]")))
        self.driver.execute_script("arguments[0].click();", month_btn)

        day_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//button[@role='gridcell' and normalize-space(text())='{day}']")))
        day_btn.click()



    # def enter_date_of_birth(self, date_str="22-12-1990"):
    #     dob_input = self.driver.find_element(*self.DOB)
    #     # Remove readonly if present, set value directly
    #     script = """
    #         arguments[0].removeAttribute('readonly');
    #         arguments[0].value = arguments[1];
    #         arguments[0].dispatchEvent(new Event('change'));
    #     """
    #     self.driver.execute_script(script, dob_input, date_str)

    #### ------- methods employement details --------
    # recruitment_mode_dd = (By.ID, "mui-component-select-recruitmentModeId")
    def select_random_recruitment_mode(self):
        dropdown_locator = (By.ID, "mui-component-select-recruitmentModeId")
        options_xpath = "//ul[@role='listbox']/li"
        self.select_random_option(dropdown_locator, options_xpath)
        ##self.select_random_option(self.recruitment_mode_dd)

   #### appointment order date
    app_select_date = (By.XPATH, "//button[@role='gridcell' and normalize-space(text())='1' "
                                 "and contains(@class,'MuiButtonBase-root')]")

    def pick_app_order_date(self):
        # 1. Click icon to open calendar
        icon = self.driver.find_element(*self.app_order_date_calender)
        self.driver.execute_script("arguments[0].click();", icon)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.app_select_date))
        self.driver.find_element(*self.app_select_date).click()


    # def enter_appointment_order_date(self, order_date_str= "06-12-2025"):
    #     app_order_date_input = self.driver.find_element(*self.app_order_date)
    #     # Remove readonly if present, set value directly
    #     script = """
    #         arguments[0].removeAttribute('readonly');
    #         arguments[0].value = arguments[1];
    #         arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
    #         arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
    #         arguments[0].blur();
    #     """
    #     self.driver.execute_script(script, app_order_date_input, order_date_str)


    # employement_status_dd = (By.ID, "mui-component-select-employmentStatusId")
    def select_random_employment_status(self):
        dropdown_locator = (By.ID, "mui-component-select-employmentStatusId")
        options_xpath = "//ul[@role='listbox']/li"
        self.select_random_option(dropdown_locator, options_xpath)
        #self.select_random_option(self.employement_status_dd)

    # app_order_no_input = (By.NAME, "appointmentOrderNo")
    def enter_app_order_no(self, order_no="ORDER123"):
        self.driver.find_element(*self.app_order_no_input).send_keys(order_no)

    # DOJ = (By.NAME, "dateOfJoining") -- old
    doj_select_date = (By.XPATH, "//button[@role='gridcell' and normalize-space(text())='1' "
                                 "and contains(@class,'MuiButtonBase-root')]")

    def pick_joining_date(self):
        icon = self.driver.find_element(*self.DOJ_icon)
        self.driver.execute_script("arguments[0].click();", icon)
        time.sleep(2)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.doj_select_date))
        time.sleep(1)
        self.driver.find_element(*self.doj_select_date).click()


    # pancard_input = (By.NAME, "panCard")
    # PAN_OPTIONS = ["ABCDE1234F", "XYZAB6789K", "PQRLM5678X"]
    PAN_OPTIONS = ["AFSPD4687D"]

    def enter_pancard(self):
        pancard_field = self.driver.find_element(*self.pancard_input)
        pancard_field.send_keys(random.choice(self.PAN_OPTIONS))

    def enter_invalid_pancard(self,pan = "1212121212"):
        field = self.driver.find_element(*self.pancard_input)
        field.clear()
        field.send_keys(pan)

    # select_qualification_dd = (By.XPATH, "//span[text()='Select the Qualification']")
    def select_random_qualification(self):
        dropdown_locator = (By.CSS_SELECTOR,"input[role='combobox'][aria-autocomplete='list']")
        options_xpath= "//ul[@role='listbox']//li[normalize-space()]"
        self.select_random_option(dropdown_locator, options_xpath)



    #mobile_no_input = (By.NAME, "mobileNumber")
    def enter_random_mobile_number(self):
        number = "9" + "".join(random.choices("0123456789", k=9))
        self.driver.find_element(*self.mobile_no_input).send_keys(number)
        return number

    #email_input = (By.NAME, "emailAddress")
    def enter_random_email(self):
        email = f"user{random.randint(1000, 9999)}@example.com"
        self.driver.find_element(*self.email_input).send_keys(email)
        return email

    #whatsapp_same_checkbox = (By.NAME, "useWhatsappAsMobile")
    def check_whatsapp_same(self):
        checkbox = self.driver.find_element(*self.whatsapp_same_checkbox)
        if not checkbox.is_selected():
            checkbox.click()

    #whatsapp_num_input = (By.NAME, "whatsappNumber")
    def enter_whatsapp_number(self):
        number = "8" + "".join(random.choices("0123456789", k=9))
        self.driver.find_element(*self.whatsapp_num_input).send_keys(number)
        return number

    #create_draft_btn = (By.XPATH, "//span[text()='Create Draft']")
    def click_create_draft(self):
        self.driver.find_element(*self.create_draft_btn).click()

    def navigate_to_dashboard(self):
        self.driver.find_element(*self.dashboard).click()



    #





