import pytest
from selenium.webdriver.common.by import By
import random
from conftest import login_successfully
from pages.login_page import LoginPage
from pages.EM_add_new_emp import AddNewEmployeePage
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
def to_timestamp_ms(day, month, year):
    dt = datetime(year, month, int(day))
    return int(time.mktime(dt.timetuple()) * 1000)
@pytest.mark.usefixtures("login_successfully")
class TestAddNewEmp:

    # test whether user logs in and navigates to add new employee page from navigate
## TESTED :: 6/12
    def test_add_employee_page_opens(self,login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)  # automatically navigates to the page
        add_emp_page.navigate_to_add_employee()
    #     # assert "Create Employee Draft" in ls.current_url

## TESTED :: 6/12
#     # ## check for mandatory fields for the personal information section
    def test_click_create_draft_no_personal(self, login_successfully):
        ls = login_successfully
        click_submit = AddNewEmployeePage(ls)
        click_submit.navigate_to_add_employee()
        click_submit.click_create_draft()
        assert "Service Classification is required" in ls.page_source
        assert "Office is required" in ls.page_source
        assert "Title is required" in ls.page_source
        assert "First Name is required" in ls.page_source
        assert "Last Name is required" in ls.page_source
        assert "Father's Name is required" in ls.page_source
        assert "Mother's Name is required" in ls.page_source
        assert "Gender is required" in ls.page_source
        assert "Date of Birth is required" in ls.page_source
#
# ## TESTED :: 6/12
#     ## check for the mandatory field for the Employment Details and Contact Information section
    def test_click_create_draft_no_emp(self, login_successfully):
        ls = login_successfully
        click_submit = AddNewEmployeePage(ls)
        click_submit.navigate_to_add_employee()
        click_submit.click_create_draft()
        assert "Recruitment Mode is required" in ls.page_source
        assert "Appointment Order Date is required" in ls.page_source
        assert "Employment Status is required" in ls.page_source
        assert "Appointment Order No is required" in ls.page_source
        assert "Date of Joining is required" in ls.page_source
        assert "PAN Card Number is required" in ls.page_source
        assert "Qualification is required" in ls.page_source
        assert "Mobile Number is required" in ls.page_source
        assert  "Email Address is required" in ls.page_source
# #
#
#TESTED :: 6/12
    def test_select_random_service_class(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.select_random_service_class()
        # Optional: Assert a value is selected
        selected_option = ls.find_element(*add_emp_page.service_class_dd).get_attribute("value")
        assert selected_option != "", "No option selected for Service Class"


## TESTED :: 6/12
    def test_select_random_office(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.select_random_office()
        selected_option = ls.find_element(*add_emp_page.select_office_dd).get_attribute("value")
        assert selected_option != "", "No option selected for Office"


## TESTED :: 6/12
    def test_select_random_title(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.select_random_title()
        selected_option = ls.find_element(*add_emp_page.title_dd).get_attribute("value")
        assert selected_option != "", "No option selected for Title"
# ###### check the value for the title and for other drop-down


# ############ FIRST NAME VALIDATIONS ###########

# # ## TESTED :: 6/12
# # #     ## no leading or trailing spaces in names
    def test_first_name_just_space(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.enter_first_name(" John ")
        add_emp_page.click_create_draft()   # Leading and trailing space
        assert "Name cannot start or end with spaces" in ls.page_source
# #
# # ## TESTED :: 6/12
# # #     ## no 2 consecutive spaces should be allowed
    def test_first_name_consecutive_spaces(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.enter_first_name("Michelle  ")  # Consecutive spaces
        add_emp_page.click_create_draft()
        assert "Consecutive spaces are not allowed" in ls.page_source
#
# # ## TESTED :: 6/12
# # #     ## first letter needs to be capital
    def test_first_name_upper(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.enter_first_name("rudy")
        add_emp_page.click_create_draft()
        assert "Name must start with a capital letter" in ls.page_source
# #
# #
# # ## TESTED :: 6/12
# # #     ## name less than two charc
    def test_first_name_less_than_2(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        add_emp_page.enter_first_name("k")
        add_emp_page.click_create_draft()
        assert "Name must be at least 2 characters long" in ls.page_source
#
# ## TESTED  :: 6/12
#     ## Input random name from the List
    def test_enter_random_first_name(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.enter_random_first_name()
#
#     ###########----MIDDLE NAME VALIDATIONS ---###########
# ### TESTED :: 6/12
    def test_middle_name_just_space(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.enter_middle_name(" Cena ")  # Leading and trailing space
        add_emp_page.click_create_draft()
        assert "Name cannot start or end with spaces" in ls.page_source
#
# ## TESTED :: 6/12
# #     ## no 2 consecutive spaces should be allowed
    def test_middle_name_consecutive_spaces(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.enter_middle_name("Obama  ")  # Consecutive spaces
        add_emp_page.click_create_draft()
        assert "Consecutive spaces are not allowed" in ls.page_source
# #
# #
# #  ## TESTED :: 6/12
# # #     ## first letter needs to be capital
    def test_middle_name_upper(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        add_emp_page.enter_middle_name("hilfiger")
        add_emp_page.click_create_draft()
        assert "Name must start with a capital letter" in ls.page_source
#
# # ##TESTED :: 6/12
# # #     ## name less than two charc
    def test_middle_name_less_than_2(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        add_emp_page.enter_middle_name("p")
        add_emp_page.click_create_draft()
        assert "Name must be at least 2 characters long" in ls.page_source
# #
#
# ## TESTED :: 6/12
#     ## enter name from random list
    def test_enter_random_middle_name(self,login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.enter_random_middle_name()
#
## TESTED :: NEED TO CHANGE ERROR MSG "LAST NAME" TO JUST NAME"
# # ############## last name
    def test_last_name_just_space(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.enter_last_name(" wwe ")  # Leading and trailing space
        add_emp_page.click_create_draft()
        #assert "Name cannot start or end with spaces" in ls.page_source

## TESTED :: 6/12
# #     ## no 2 consecutive spaces should be allowed
    def test_last_name_consecutive_spaces(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.enter_last_name("Michael  ")  # Consecutive spaces
        add_emp_page.click_create_draft()
        assert "Consecutive spaces are not allowed" in ls.page_source

## TESTED :: NEED TO CHANGE THE ERROR MSG " LAST NAME TO NAME
# #     ## first letter needs to be capital
    def test_last_name_upper(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        add_emp_page.enter_last_name("rudy")
        add_emp_page.click_create_draft()
        #assert "Name must start with a capital letter" in ls.page_source

## TESTED :: NEED TO CHANGE THE ERROR MSG TO NAME
#     ## name less than two charc
    def test_last_name_less_than_2(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        add_emp_page.enter_last_name("e")
        add_emp_page.click_create_draft()
        #assert "Name must be at least 2 characters long" in ls.page_source

## TESTED :: 6/12
    def test_enter_random_last_name(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.enter_random_last_name()

#
# ##############################
# ## fathers and mothers name ka check
#
# ############

## TESTED :: 6/12
#     ##choose any random gender
    def test_select_random_gender(self,login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        #add_emp_page.select_random_gender()
        selected_gender_locator = add_emp_page.select_random_gender()
        is_selected = ls.find_element(*selected_gender_locator).is_selected()

        assert is_selected, "Selected gender radio button is not marked as selected"

## TESTED :: 6/12
    def test_pick_full_dob(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        add_emp_page.pick_dob(year="2006", month="Mar", day="20")

        dob_value = ls.find_element(*add_emp_page.pick_dob()).get_attribute("value")
        assert "20-03-2006" in dob_value, f"Expected '20-03-2006', got '{dob_value}'"

#     ##---------- date picker for dob -----
#     def test_enter_dob(self, login_successfully):
#         ls = login_successfully
#         add_emp_page = AddNewEmployeePage(ls)
#         #add_emp_page.navigate_to_add_employee()
#         add_emp_page.enter_date_of_birth()
#         value = login_successfully.find_element(*add_emp_page.DOB).get_attribute("value")
#         assert value == "22-12-1990", "DOB value did not persist correctly"

#         ##@@@@@@@check if a age is entered and its less than 18 years -----@@@@@@@@@@@
#
    def test_enter_invalid_dob_under_18(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        add_emp_page.navigate_to_add_employee()
        # Enter a date that makes the user younger than 18
        #under_18_date = (datetime.today() - timedelta(days=17 * 365)).strftime("%d-%m-%Y")
        add_emp_page.enter_date_of_birth("22-12-2019")
        add_emp_page.click_create_draft()
        assert "Age Must be 18+ years" in ls.page_source
#
#TESTED :: 6/21
    ## Recruitment mode - select any rndom from the list
    def test_select_random_recruitment_mode(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.select_random_recruitment_mode()
        # check if any value is selected
        selected_value = ls.find_element(*add_emp_page.recruitment_mode_dd).text
        assert selected_value.strip() != "", "No recruitment mode selected"

## TESTED :: 6/12 --------need to check / change
    def test_enter_appointment_order_date(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.pick_app_order_date()
        value = ls.find_element(*add_emp_page.app_order_date).get_attribute("value")
        #assert "1" in value

## TESTED :: 6/12
    def test_select_random_employment_status(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.select_random_employment_status()
#         selected_value = ls.find_element(*add_emp_page.employement_status_dd).text
#         assert selected_value.strip() != "", "No employment status selected"

## TESTED :: 6/12
    def test_enter_appointment_order_number(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.enter_app_order_no()

        # value = ls.find_element(*add_emp_page.app_order_no_input).get_attribute("value")
        # assert "ORDER56789" in value

## TESTED :: 6/12
    def test_enter_date_of_joining(self,login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.enter_date_of_joining()
        value = ls.find_element(*add_emp_page.DOJ).get_attribute("value")
        assert value == "07-12-2025"

## TESTED :: 6/16
    def test_pick_joining_date(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        add_emp_page.navigate_to_add_employee()
        # Trigger the selection of day '1' as joining date
        add_emp_page.pick_joining_date()
        # Retrieve value after picking date
        doj_value = ls.find_element(*add_emp_page.DOJ).get_attribute("value")
        assert doj_value.startswith("01"), f"Expected DOJ date with day ‘01…’, but got '{doj_value}'"

    #
    # def test_doj_after_appointment_order_date_positive(self, login_successfully):
    #     ls = login_successfully
    #     add_emp_page = AddNewEmployeePage(ls)
    #     add_emp_page.navigate_to_add_employee()
    #     add_emp_page.enter_app_order_date("01-01-2022")
    #     add_emp_page.enter_date_of_joining("02-01-2022")
    #     add_emp_page.click_create_draft()
    #     assert "Date of Joining should be after Appointment Order Date" not in ls.page_source

    # def test_doj_before_appointment_order_date_negative(self, login_successfully):
    #     ls = login_successfully
    #     add_emp_page = AddNewEmployeePage(ls)
    #     add_emp_page.navigate_to_add_employee()
    #     add_emp_page.enter_app_order_date("05-01-2022")
    #     add_emp_page.enter_date_of_joining("02-01-2022")
    #     add_emp_page.click_create_draft()
    #     assert "Date of Joining should be after Appointment Order Date" in ls.page_source

###TESTED :: 6/11
    def test_enter_pancard(self,login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        #add_emp_page.navigate_to_add_employee()
        add_emp_page.enter_pancard()
#         value = ls.find_element(*add_emp_page.pancard_input).get_attribute("value")
#         assert value in add_emp_page.PAN_OPTIONS, "PAN entered is not from the predefined list"

## TESTED :: 6/13
    def test_enter_invalid_pancard(self,login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        add_emp_page.navigate_to_add_employee()
        add_emp_page.enter_invalid_pancard()
        add_emp_page.click_create_draft()
        assert "Invalid PAN Card format" in ls.page_source



############# SELECTING RANDON QUALIFICATIONS #########
##TESTED::6/13
    def test_select_random_qualification(self, login_successfully):
        # Step 1: Open the dropdown
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        add_emp_page.navigate_to_add_employee()
        add_emp_page.select_random_qualification() #.click()
        # WebDriverWait(ls, 10).until(
        #     EC.visibility_of_all_elements_located(
        #         (By.XPATH, "//ul[@role='listbox']//li[normalize-space()]")))
        options = ls.find_elements(By.XPATH, "//ul[@role='listbox']//li[normalize-space()]")
        selected = random.choice(options)
        #selected_text = selected.text
        selected.click()

## TESTED :: 6/13
    def test_enter_mobile_number_less_than_10_digits(self, login_successfully):
        ls = login_successfully
        add_emp = AddNewEmployeePage(ls)
        # add_emp.navigate_to_add_employee()
        short_number = "98765431"  # 8 digits
        mobile_elem = ls.find_element(*add_emp.mobile_no_input)
        mobile_elem.clear()
        mobile_elem.send_keys(short_number)
        # Now trigger blur: click outside the field (e.g., on the page body)
        ls.find_element(By.TAG_NAME, "body").click()
        # Or you can dispatch blur via JavaScript
        # ls.execute_script("arguments[0].blur();", mobile_elem)
        assert "Invalid mobile number. Must be 10 digits." in ls.page_source

 ###TESTED :: 6/13
    def test_enter_random_mobile_number(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        # add_emp_page.navigate_to_add_employee()
        mobile_number = add_emp_page.enter_random_mobile_number()
        entered_value = ls.find_element(*add_emp_page.mobile_no_input).get_attribute("value")
        ##assert entered_value == mobile_number
        assert len(entered_value) == 10

## TESTED ::6/13
    def test_enter_random_email(self,login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        add_emp_page.navigate_to_add_employee()

        email = add_emp_page.enter_random_email()
        entered_value = ls.find_element(*add_emp_page.email_input).get_attribute("value")

        assert entered_value == email
#
###TESTED : 6/13
    def test_check_whatsapp_same_checkbox(self,login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        add_emp_page.navigate_to_add_employee()

        add_emp_page.check_whatsapp_same()
        checkbox = ls.find_element(*add_emp_page.whatsapp_same_checkbox)

        assert checkbox.is_selected()
        ##UNCHECK IT
        checkbox.click()
        assert not checkbox.is_selected()
#


    def test_enter_whatsapp_number(self,login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        add_emp_page.navigate_to_add_employee()

        number = add_emp_page.enter_whatsapp_number()
        entered_value = ls.find_element(*add_emp_page.whatsapp_num_input).get_attribute("value")

        assert entered_value == number
        assert len(entered_value) == 10
#
    ########NO VERIFICATION IS IMPLEMENTED YET#######
    # def test_enter_whatsapp_number_less_than_10_digits(self,login_successfully):
    #     ls = login_successfully
    #     add_emp_page = AddNewEmployeePage(ls)
    #     #add_emp_page.navigate_to_add_employee()
    #     short_number = "98765431"  # 8 digits
    #     mobile_elem = ls.find_element(*add_emp_page.whatsapp_num_input)
    #     mobile_elem.clear()
    #     mobile_elem.send_keys(short_number)
    #     # Now trigger blur: click outside the field (e.g., on the page body)
    #     ls.find_element(By.TAG_NAME, "body").click()
    #     # Or you can dispatch blur via JavaScript
    #     # ls.execute_script("arguments[0].blur();", mobile_elem)
    #     assert "Invalid mobile number. Must be 10 digits." in ls.page_source
    # def test_navigate_to_dashboard(self,login_successfully):
    #     ls = login_successfully  # Already logged in and at dashboard
    #     ls.navigate_to_dashboard()
    #
    #     # Confirm navigation by checking current URL or presence of element
    #     assert "Welcome" in ls.current_url


#     #--------- test one positive flow-------#######
    def test_create_draft_after_mandatory_fields(self,login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        add_emp_page.navigate_to_add_employee()
        add_emp_page.navigate_to_dashboard()
        #add_emp_page = AddNewEmployeePage(ls)
        add_emp_page.navigate_to_add_employee()
        # Fill in all mandatory fields
        add_emp_page.select_random_service_class()
        add_emp_page.select_random_office()
        add_emp_page.select_random_title()
        add_emp_page.enter_random_first_name()
        add_emp_page.enter_random_middle_name()
        add_emp_page.enter_random_last_name()
        add_emp_page.enter_father_name('PK Mohanty')
        add_emp_page.enter_mother_name('Smt Malavika Venkatesh Ramayana')
        add_emp_page.select_random_gender()
        #add_emp_page.enter_date_of_birth()

        ##-- employement details ---##
        add_emp_page.select_random_recruitment_mode()
        #add_emp_page.enter_appointment_order_date()
        add_emp_page.select_random_employment_status()
        add_emp_page.enter_app_order_no()
        #add_emp_page.enter_date_of_joining()
        add_emp_page.enter_pancard()
        add_emp_page.select_random_qualification()
        add_emp_page.enter_random_mobile_number()
        add_emp_page.enter_random_email()
        #add_emp_page.enter_date_of_birth()
        add_emp_page.pick_app_order_date()
        add_emp_page.pick_dob(year="2006", month="Mar", day="20")
        #add_emp_page.pick_app_order_date()
        add_emp_page.pick_joining_date()

        # Click on Create Draft
        add_emp_page.click_create_draft()
        ##assert "Date of Birth is required" in ls.page_source
        ##assert "Date of Joining is required" in ls.page_source
        ##assert "Appointment Order Date is required" in ls.page_source
        #assert "Office Wise Employee Draft List" in ls.page_source

    # def test_pick_full_dob(self, login_successfully):
    #     ls = login_successfully
    #     add_emp_page = AddNewEmployeePage(ls)
    #     add_emp_page.pick_dob_ymd(year="2006", month="Mar", day="20")
    #
    #     dob_value = ls.find_element(*add_emp_page.DOB_INPUT).get_attribute("value")
    #     assert "20-03-2006" in dob_value, f"Expected '20-03-2006', got '{dob_value}'"

