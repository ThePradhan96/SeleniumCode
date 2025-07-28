import time
from random import random
from symtable import Class

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import login_successfully
from pages.EM_draft_list import EMDraftListPage

@pytest.mark.usefixtures("login_successfully")
class TestDraftList:

    def test_complete_draft_flow(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)

        draft_page.navigate_to_draft_list()
        draft_page.click_first_view_more()
        draft_page.click_complete_the_draft()
        assert "Employee Details Form" in ls.page_source

## CHECK MANDATORY FIELDS ##
    def test_click_next_with_blanks(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        draft_page.enter_height("190")
        draft_page.click_next()
        assert "Religion is required" in ls.page_source
        assert  "Caste is required" in ls.page_source
        assert  "Blood Group is required" in ls.page_source
        assert "Marital Status is required" in ls.page_source
        assert "Identification Mark is required" in ls.page_source
        assert "House No. is required" in ls.page_source
        assert "Street/Lane is required" in ls.page_source
        assert "Town/Village is required" in ls.page_source
        assert "Police Station is required" in ls.page_source
        assert "Post Office is required" in ls.page_source
        assert "Pin Code is required" in ls.page_source
        assert "City is required" in ls.page_source
        #assert "State is required"


#####------personal information -------####
    # TESTED :: 6/18
    def test_dropdown_personal_info(self,login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        # Nationality
        draft_page.select_random_nationality()
        selected_nation = ls.find_element(*draft_page.nationality_dd).get_attribute("value")
        assert selected_nation != "", "No option selected for Nationality"
        #Religion
        draft_page.select_random_religion()
        selected_religion= ls.find_element(*draft_page.religion_dd).get_attribute("value")
        assert selected_religion != "", "No option selected for religion"
        #caste
        draft_page.select_random_caste()
        selected_caste= ls.find_element(*draft_page.caste_dd).get_attribute("value")
        assert selected_caste != "", "No option selected for caste"
        #Blood type
        draft_page.select_random_blood_group()
        selected_bloodtype= ls.find_element(*draft_page.blood_group_dd).get_attribute("value")
        assert selected_bloodtype != "", "No option selected for bloodtype"

        ##-- Present address --
        # present state
        draft_page.select_present_random_state()
        selected_state= ls.find_element(*draft_page.present_state_dd).get_attribute("value")
        assert selected_state != "", "No option selected for present state"
        #present district
        draft_page.select_present_random_district()
        selected_district= ls.find_element(*draft_page.present_district_dd).get_attribute("value")
        assert selected_district != "", "No option selected for present district"

        ##-- permanent address-
        # permanent state
        draft_page.select_permanent_random_state()
        selected_state= ls.find_element(*draft_page.permanent_state_dd).get_attribute("value")
        assert selected_state != "", "No option selected for permanent state"
        # permament district
        draft_page.select_permanent_random_district()
        selected_district= ls.find_element(*draft_page.permanent_district_dd).get_attribute("value")
        assert selected_district != "", "No option selected for permanent district"

# TESTED :: 6/18
    def test_ph_vh_selection_and_percentage(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        # Select a random PH/VH option
        draft_page.select_random_ph_vh_option()
        # Check which radio button was selected
        selected_value = None
        if ls.find_element(*draft_page.ph_radio).is_selected():
            selected_value = "PH"
        elif ls.find_element(*draft_page.vh_radio).is_selected():
            selected_value = "VH"
        else:
            selected_value = "None"

        print(f"Selected PH/VH value in test: {selected_value}")

        # If PH or VH selected, fill the % field
        if selected_value in ["PH", "VH"]:
            percent_field = ls.find_element(By.NAME, "phVhPercentage")
            percent_field.clear()
            percent_field.send_keys("40")  # or any dummy value
            assert percent_field.get_attribute("value") != "", "Percent field was not filled for PH/VH"
        else:
            print("No % input required as 'None' was selected.")

## MARITIAL STATUS
# TESTED  :: 6/19
    def test_marital_status_selection(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        # Select a random marital status
        draft_page.select_maritial_status()
        # Validate that one of the radio buttons is selected
        married_selected = ls.find_element(*draft_page.married).is_selected()
        unmarried_selected = ls.find_element(*draft_page.unmarried).is_selected()
        assert married_selected or unmarried_selected, "No marital status option is selected"
        selected_status = "Married" if married_selected else "Unmarried"
        print(f"Marital status selected in test: {selected_status}")

## HEIGHT IN CM - should show an error
    def test_height_below_min(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        draft_page.enter_height("110")
        ##assert

### Allows 'e' '+'
    def test_height_rejects_alphabets(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        draft_page.enter_height("abc123")

# Exact height
# TESTED :: 6/19
    def test_valid_height_entry(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        valid_height = "165.5"
        draft_page.enter_height(valid_height)

        entered_value = ls.find_element(*draft_page.height_input).get_attribute("value")
        assert entered_value == valid_height, f"Expected height input to be '{valid_height}', but got '{entered_value}'"

## IDENTIFICATION MARK - INPUT TEXT
    # TESTED :: 6/19
    def test_enter_identification_mark(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        test_value = "Mole on left hand"
        draft_page.enter_identification(test_value)

        entered_value = ls.find_element(*draft_page.identification_mark).get_attribute("value")
        assert entered_value == test_value, f"Expected identification mark to be '{test_value}', but got '{entered_value}'"

    ########-- PRESENT ADDRESS -############
    def test_valid_present_address_fields(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        house_no = "123A"
        street = "MG Road"
        town = "Hyderabad municipal"
        draft_page.enter_present_house_num(house_no)
        draft_page.enter_present_street(street)
        draft_page.enter_present_town(town)

        assert ls.find_element(*draft_page.present_house_num).get_attribute("value") == house_no
        assert ls.find_element(*draft_page.present_street).get_attribute("value") == street
        assert ls.find_element(*draft_page.present_town).get_attribute("value") == town

## SHOULD NOT ALLOW JUST SPACES OR SPECIAL CHARCS
    def test_special_characters_in_house_num(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_input = "@#$%"
        draft_page.enter_present_house_num(invalid_input)
        value = ls.find_element(*draft_page.present_house_num).get_attribute("value")
        assert not any(char in value for char in "@#$%"), f"Special characters accepted in house number: {value}"

    def test_special_characters_in_street(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_input = "!*&#"
        draft_page.enter_present_street(invalid_input)
        value = ls.find_element(*draft_page.present_street).get_attribute("value")
        assert not any(char in value for char in "!*&#"), f"Special characters accepted in street: {value}"

    def test_special_characters_in_town(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_input = "$%^&"
        draft_page.enter_present_town(invalid_input)
        value = ls.find_element(*draft_page.present_town).get_attribute("value")
        assert not any(char in value for char in "$%^&"), f"Special characters accepted in town: {value}"

    def test_valid_present_police_post_city(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        police = "Central Station"
        postoffice = "GPO Sub"
        city = "Bangalore"
        draft_page.enter_present_policestation(police)
        draft_page.enter_present_postoffice(postoffice)
        draft_page.enter_present_city(city)

        assert ls.find_element(*draft_page.present_policestation).get_attribute("value") == police
        assert ls.find_element(*draft_page.present_postoffice).get_attribute("value") == postoffice
        assert ls.find_element(*draft_page.present_city).get_attribute("value") == city

    def test_special_characters_in_policestation(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_input = "@#Station$%"

        draft_page.enter_present_policestation(invalid_input)
        value = ls.find_element(*draft_page.present_policestation).get_attribute("value")

        assert not any(char in value for char in "@#$%"), f"Special characters accepted in Police Station: {value}"

    def test_special_characters_in_postoffice(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_input = "PO@123#"

        draft_page.enter_present_postoffice(invalid_input)
        value = ls.find_element(*draft_page.present_postoffice).get_attribute("value")

        assert not any(char in value for char in "@#$%"), f"Special characters accepted in Post Office: {value}"

    def test_special_characters_in_city(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_input = "Ci@ty#"

        draft_page.enter_present_city(invalid_input)
        value = ls.find_element(*draft_page.present_city).get_attribute("value")

        assert not any(char in value for char in "@#$%"), f"Special characters accepted in City: {value}"

####### PIN CODE ###
    # TESTED :: 6/19
    def test_valid_pincode(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        valid_pincode = "560001"
        draft_page.enter_present_pincode(valid_pincode)

        value = ls.find_element(*draft_page.present_pincode).get_attribute("value")
        assert value == valid_pincode, "Valid 6-digit pincode was not accepted"

    def test_alphabetic_or_special_chars_in_pincode(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_pincode = "56AB@1"
        draft_page.enter_present_pincode(invalid_pincode)

## pin code less than 6 digits
    # TESTED :: 6/11
    def test_short_pincode_rejected(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_pincode = "12345"  # 5 digits
        draft_page.enter_present_pincode(invalid_pincode)
        draft_page.enter_height("169")
        draft_page.click_next()

        assert "Pincode is invalid" in ls.page_source

# TESTED :: 6/19
    def test_long_pincode_rejected(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_pincode = "123452312345"
        draft_page.enter_present_pincode(invalid_pincode)
        draft_page.enter_height("169")
        draft_page.click_next()

        assert "Pincode is invalid" in ls.page_source

    ###### PERMANENT ADDRESS --- #######
# TESTED :: 6/19
    def test_valid_permanent_address_fields(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        house_no = "B - 432"
        street = "Harvard street"
        town = "Medford municipality"
        draft_page.enter_permanent_house_num(house_no)
        draft_page.enter_permanent_street(street)
        draft_page.enter_permanent_town(town)

        assert ls.find_element(*draft_page.permanent_house_num).get_attribute("value") == house_no
        assert ls.find_element(*draft_page.permanent_street).get_attribute("value") == street
        assert ls.find_element(*draft_page.permanent_town).get_attribute("value") == town

    def test_special_characters_in_p_house_num(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_input = "@#$%"
        draft_page.enter_permanent_house_num(invalid_input)
        value = ls.find_element(*draft_page.permanent_house_num).get_attribute("value")
        assert not any(char in value for char in "@#$%"), f"Special characters accepted in house number: {value}"

    def test_special_characters_in_p_street(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_input = "!*&#"
        draft_page.enter_permanent_street(invalid_input)
        value = ls.find_element(*draft_page.permanent_street).get_attribute("value")
        assert not any(char in value for char in "!*&#"), f"Special characters accepted in street: {value}"

    def test_special_characters_in_p_town(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_input = "$%^&"
        draft_page.enter_permanent_town(invalid_input)
        value = ls.find_element(*draft_page.permanent_town).get_attribute("value")
        assert not any(char in value for char in "$%^&"), f"Special characters accepted in town: {value}"

# TESTED :: 6/19
    def test_valid_permanent_police_post_city(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        police = "NYC Police station"
        postoffice = "P/O - Mystic Ave"
        city = "Boston"
        draft_page.enter_permanent_policestation(police)
        draft_page.enter_permanent_postoffice(postoffice)
        draft_page.enter_permanent_city(city)

        assert ls.find_element(*draft_page.permanent_policestation).get_attribute("value") == police
        assert ls.find_element(*draft_page.permanent_postoffice).get_attribute("value") == postoffice
        assert ls.find_element(*draft_page.permanent_city).get_attribute("value") == city

    def test_special_characters_in_p_policestation(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_input = "@#Station$%"

        draft_page.enter_permanent_policestation(invalid_input)
        value = ls.find_element(*draft_page.permanent_policestation).get_attribute("value")

        assert not any(char in value for char in "@#$%"), f"Special characters accepted in Police Station: {value}"

    def test_special_characters_in_p_postoffice(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_input = "PO@123#"

        draft_page.enter_permanent_postoffice(invalid_input)
        value = ls.find_element(*draft_page.permanent_postoffice).get_attribute("value")

        assert not any(char in value for char in "@#$%"), f"Special characters accepted in Post Office: {value}"


    def test_special_characters_in_p_city(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_input = "Ci@ty#"

        draft_page.enter_permanent_city(invalid_input)
        value = ls.find_element(*draft_page.permanent_city).get_attribute("value")

        assert not any(char in value for char in "@#$%"), f"Special characters accepted in City: {value}"

# TESTED 6/19
    def test_valid_p_pincode(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        valid_pincode = "560001"
        draft_page.enter_permanent_pincode(valid_pincode)

        value = ls.find_element(*draft_page.permanent_pincode).get_attribute("value")
        assert value == valid_pincode, "Valid 6-digit pincode was not accepted"

    def test_alphabetic_or_special_chars_in_p_pincode(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_pincode = "56AB@1"
        draft_page.enter_permanent_pincode(invalid_pincode)

        value = ls.find_element(*draft_page.permanent_pincode).get_attribute("value")
        assert value.isdigit() and len(value) == 6, f"Non-numeric characters accepted in pincode: {value}"


        ####less than 6
# TESTED ::6/19
    def test_short_p_pincode_rejected(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_pincode = "12345"  # 5 digits
        draft_page.enter_present_pincode(invalid_pincode)
        draft_page.enter_height("169")
        draft_page.click_next()

        assert "Pincode is invalid" in ls.page_source

# TESTED :: 6/19
    def test_long_p_pincode_rejected(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        invalid_pincode = "1234567845"  # 5 digits
        draft_page.enter_present_pincode(invalid_pincode)
        draft_page.enter_height("169")
        draft_page.click_next()

        assert "Pincode is invalid" in ls.page_source

    ####################################
    def test_overall_functionality(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)

        draft_page.navigate_to_draft_list()
        draft_page.click_first_view_more()
        draft_page.click_complete_the_draft()

        draft_page.select_random_nationality()
        draft_page.select_random_religion()
        draft_page.select_random_caste()
        draft_page.select_random_ph_vh_option()
        draft_page.select_random_blood_group()
        draft_page.select_maritial_status()
        draft_page.enter_height("170")
        draft_page.enter_identification("kuch bhi likh de")
        draft_page.enter_present_house_num("B-189")
        draft_page.enter_present_street("street ka address")
        draft_page.enter_present_town("sunabeda11")
        draft_page.enter_present_policestation("Policestuff needs")
        draft_page.enter_present_postoffice("P/O- SOMETHING")
        draft_page.enter_present_pincode("765123")
        draft_page.enter_present_city("koraput")
        draft_page.select_present_random_state()
        draft_page.select_present_random_district()

        draft_page.enter_permanent_house_num("HIG 77")
        draft_page.enter_permanent_street("harvard st")
        draft_page.enter_permanent_town("Medford")
        draft_page.enter_permanent_policestation("Mystic ave police")
        draft_page.enter_permanent_postoffice("P/O-4R5678")
        draft_page.enter_permanent_pincode('02155')
        draft_page.enter_permanent_city("Boston")
        draft_page.select_permanent_random_state()
        draft_page.select_permanent_random_district()

######################################------------------------------######################################
#######################################------------------------------######################################
#######################################------------------------------######################################
# TESTED :: 6/21
    def test_pay_structure_blank(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        #draft_page.enter_height("190")
        #draft_page.fill_basic_details()
        draft_page.click_pay_structure_next()
        assert "Group is required" in ls.page_source
        assert "Please select an option" in ls.page_source
        assert "Effective Date is required" in ls.page_source
        assert "Please select a PayBand" in ls.page_source
        assert "Please select a Grade Pay" in ls.page_source
        assert "Level is required" in ls.page_source
        assert "Basic Pay is required" in ls.page_source
        assert "Next Increment is required" in ls.page_source

    def test_select_group(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        selected_group =draft_page.select_group()

        if selected_group == 'B':
            draft_page.select_gazetted()

# TESTED :: 6/21
    def test_select_cadre_status(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()

        # Step 1: Select Cadre Status (Yes/No randomly)
        selected = draft_page.select_cadre_status()

        # Step 2: If Cadre = Yes, select from the Cadre dropdown
        if selected == 'true':
            draft_page.select_cadre()

# TESTED :: 6/21
    def test_posting_radio_btn(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()

        # Select one option from each radio group
        draft_page.select_posting_type()
        time.sleep(2)
        draft_page.select_ttaadc_posting()
        time.sleep(2)
        draft_page.select_posted_outside_state()
        time.sleep(2)
        draft_page.select_gis_eligibility()

    def test_payband_grade_posting(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        draft_page.select_group()
        draft_page.select_payband()
        draft_page.select_posted_designation()
        draft_page.select_grade_pay()


    def test_next_increment_after_effected_from_date(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()

        draft_page.pick_effected_from_date()
        draft_page.select_next_increment()
        draft_page.click_pay_structure_next()

    def test_overall_paystructure_details(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        draft_page.select_group_A()
        draft_page.select_posted_designation()
        draft_page.select_posting_type()
        time.sleep(2)
        draft_page.select_ttaadc_posting()
        time.sleep(2)
        draft_page.select_posted_outside_state()
        time.sleep(2)
        draft_page.pick_effected_from_date()
        draft_page.select_payband()
        draft_page.select_grade_pay()
        draft_page.select_gis_eligibility()
        time.sleep(2)
        draft_page.select_next_increment()
        draft_page.click_pay_structure_next()


############################################################################################################
############################################################################################################
#---- GENERAL INFORMATION -----BANK AND ALLOWANCE DETAILS---###

## TESTED
    def test_general_informtion_blank(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        #draft_page.click_pay_structure_next()
        draft_page.click_submit_preview()
        assert "Bank is required" in ls.page_source
        assert "Branch is required" in ls.page_source
        assert "Account number is required" in ls.page_source
        assert "IFSC Code is required" in ls.page_source
        #assert "Must Select Treasury" in ls.page_source

## TESTED
    def test_bank_branch_HOA_treasury(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        #draft_page.click_pay_structure_next()
        draft_page.select_bank()
        time.sleep(2)
        draft_page.select_branch()
        draft_page.select_head_of_account()
        #####draft_page.select_treasury() ##-----default value is selected - needs to cancel that first and then select

#TESTED
    def test_pension_fund_npa(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        draft_page.entitlement_to_pension()
        draft_page.retirement_fund_type()
        draft_page.npa_applicable()


    def test_bank_pf_account(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        draft_page.input_account_number('12345432123456')
        draft_page.input_pf_account('TF/IDK/09876345')

# TESTED
    def test_quater_occupied(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        draft_page.quater_occupied()
        yes_elem = draft_page.driver.find_element(*draft_page.quater_yes)
        yes_selected = yes_elem.is_selected()

        if yes_selected:
            time.sleep(1)
            draft_page.select_quater_type()
            time.sleep(1)
            draft_page.govt_quater_no('B-187/02')
        else:
            print("Quarter not occupied — no further input needed")



    def test_npa_section(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()
        # Select Yes/No
        draft_page.npa_applicable()
        time.sleep(1)

        # Determine which option was actually selected
        yes_elem = draft_page.driver.find_element(*draft_page.NPA_applicable_yes)
        yes_selected = yes_elem.is_selected()
        time.sleep(1)

        if yes_selected:
            time.sleep(1)
            # If “Yes”, fill in the amount
            draft_page.input_npa_amount("25000")
        else:
            # If “No”, skip input
            print("NPA not applicable — skipping amount input")

# TESTED
    def test_npa_section_yes(self, login_successfully):
        ls = login_successfully
        draft_page = EMDraftListPage(ls)
        draft_page.navigate_to_draft_continuation()

        # Force select "Yes" for NPA
        draft_page.driver.find_element(*draft_page.NPA_applicable_yes).click()

        # Optionally wait for the amount input to appear, then enter the value
        time.sleep(1)
        draft_page.input_npa_amount("25000")

        # Assert that the Yes radio is indeed selected
        yes_elem = draft_page.driver.find_element(*draft_page.NPA_applicable_yes)
        assert yes_elem.is_selected(), "Expected NPA 'Yes' to be selected"




