from datetime import datetime, time
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EMDraftListPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 2)



    # Navigation elements from dashboard to employee _management to add new emp tab
    employee_management_tab = (By.XPATH, "//span[text()='Employee Management']")
    draft_list_tab = (By.XPATH, "//span[text()='Draft List']")
    view_more_btn = (By.XPATH, "(//button[contains(@class, 'hbutton') and text()='View More'])[1]" )
    complete_the_draft_btn = (By.XPATH, '//button[normalize-space()="Complete The Draft"]')
    ##next button
    click_next_btn =  (By.XPATH, "//button[@type='submit' and text()='Next']")


    # Methods
    def navigate_to_draft_list(self):
        self.wait.until(EC.element_to_be_clickable(self.employee_management_tab)).click()
        self.wait.until(EC.element_to_be_clickable(self.draft_list_tab)).click()

    def click_first_view_more(self):
        self.wait.until(EC.element_to_be_clickable(self.view_more_btn)).click()

    def click_complete_the_draft(self):
        self.wait.until(EC.element_to_be_clickable(self.complete_the_draft_btn)).click()

    def navigate_to_draft_continuation(self):
        self.wait.until(EC.element_to_be_clickable(self.employee_management_tab)).click()
        self.wait.until(EC.element_to_be_clickable(self.draft_list_tab)).click()
        self.wait.until(EC.element_to_be_clickable(self.view_more_btn)).click()
        self.wait.until(EC.element_to_be_clickable(self.complete_the_draft_btn)).click()

    def click_next(self):
        self.driver.find_element(*self.click_next_btn).click()

    #################---------------------------------------------###########################
    #################---------------------------------------------###########################
    ###############----------- Employee Details Form -------------###############
    ###### -------- Personal Information ---###########
    # BASIC INFORMATION #
    nationality_dd = (By.ID, "mui-component-select-nationality")
    religion_dd = (By.ID, "mui-component-select-religion")
    caste_dd = (By.ID, "mui-component-select-caste")
    ph_vh_none = (By.XPATH,"//input[@name='whichPhVh' and @value='none']")
    ph_radio = (By.XPATH, "//input[@name='whichPhVh' and @value='ph']")
    vh_radio = (By.XPATH, "//input[@name='whichPhVh' and @value='vh']")
    ph_vh_percentage = (By.NAME, "phVhPercentage")
    blood_group_dd = (By.ID, "mui-component-select-bloodGroup")
    married = (By.XPATH, "//input[@name='maritalStatus' and @value='Y']")
    unmarried = (By.XPATH, "//input[@name='maritalStatus' and @value='N']")
    height_input = (By.NAME, "exactHeight")
    identification_mark = (By.NAME, "markIdentification")

    # PRESENT ADDRESS #
    present_house_num = (By.NAME, "presentHouseNo")
    present_street = (By.NAME, "presentStreetLane")
    present_town = (By.NAME, "presentTownVillage")
    present_policestation = (By.NAME,"presentPoliceStation")
    present_postoffice = (By.NAME, "presentPostOffice")
    present_pincode = (By.NAME, "presentPinCode")
    present_city = (By.NAME, "presentCity")
    present_state_dd = (By.ID, "mui-component-select-presentStateId")
    present_district_dd = (By.ID, "mui-component-select-presentDistrictId")
    same_as_present_checkbox = (By.XPATH, "//label[.//span[text()='Same as Present Address']]//input[@type='checkbox']")

    # PERMANENT ADDRESS #
    permanent_house_num = (By.NAME, "permanentHouseNo")
    permanent_street = (By.NAME, "permanentStreetLane")
    permanent_town = (By.NAME, "permanentTownVillage")
    permanent_policestation = (By.NAME,"permanentPoliceStation")
    permanent_postoffice = (By.NAME, "permanentPostOffice")
    permanent_pincode = (By.NAME, "permanentPinCode")
    permanent_city = (By.NAME, "permanentCity")
    permanent_state_dd = (By.ID, "mui-component-select-permanentStateId")
    permanent_district_dd = (By.ID, "mui-component-select-permanentDistrictId")


    # Actions to navigate from the dashboard to the complete draft page
    # Employee Management -> Employee Draft List -> Draft Continuation


        ##########SELECTING RANDOM FROM THE LIST ########
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

    ### --- BASIC INFORMATION ----####
    def select_random_nationality(self):
        dropdown = self.nationality_dd #(By.ID, "mui-component-select-nationality")
        options_xpath = "//ul[@role='listbox']/li"
        self.select_random_option(dropdown, options_xpath)

    def select_random_religion(self):
        dropdown = self.religion_dd # (By.ID, "mui-component-select-religion")
        options_xpath = "//ul[@role='listbox']/li"
        self.select_random_option(dropdown, options_xpath)

    def select_random_caste(self):
        dropdown = self.caste_dd # (By.ID, "mui-component-select-caste")
        options_xpath = "//ul[@role='listbox']/li"
        self.select_random_option(dropdown, options_xpath)

    def select_random_ph_vh_option(self):
        options = [self.ph_vh_none, self.ph_radio, self.vh_radio]
        selected_locator = random.choice(options)
        self.driver.find_element(*selected_locator).click()
        print(f"Selected PH/VH option: {selected_locator}")

    def select_random_blood_group(self):
        dropdown = self.blood_group_dd  # (By.ID, "mui-component-select-bloodGroup")
        options_xpath = "//ul[@role='listbox']/li"
        self.select_random_option(dropdown, options_xpath)

    def select_maritial_status(self):
        options = [self.married , self.unmarried]
        selected_locator = random.choice(options)
        self.driver.find_element(*selected_locator).click()
        print(f"status: {selected_locator}")

    def enter_height(self, height_value):
        self.driver.find_element(*self.height_input).clear()
        self.driver.find_element(*self.height_input).send_keys(height_value)

    def enter_identification(self,identification_remark):
        self.driver.find_element(*self.identification_mark).clear()
        self.driver.find_element(*self.identification_mark).send_keys(identification_remark)


########-- PRESENT ADDRESS -############
    def enter_present_house_num(self, houseno):
        self.driver.find_element(*self.present_house_num).clear()
        self.driver.find_element(*self.present_house_num).send_keys(houseno)

    def enter_present_street(self, street):
        self.driver.find_element(*self.present_street).clear()
        self.driver.find_element(*self.present_street).send_keys(street)

    def enter_present_town(self, town):
        self.driver.find_element(*self.present_town).clear()
        self.driver.find_element(*self.present_town).send_keys(town)

    def enter_present_policestation(self, police):
        self.driver.find_element(*self.present_policestation).clear()
        self.driver.find_element(*self.present_policestation).send_keys(police)

    def enter_present_postoffice(self, postoffice):
        self.driver.find_element(*self.present_postoffice).clear()
        self.driver.find_element(*self.present_postoffice).send_keys(postoffice)

    def enter_present_pincode(self, zip):
        self.driver.find_element(*self.present_pincode).clear()
        self.driver.find_element(*self.present_pincode).send_keys(zip)

    def enter_present_city(self, city):
        self.driver.find_element(*self.present_city).clear()
        self.driver.find_element(*self.present_city).send_keys(city)

    def select_present_random_state(self):
        dropdown = self.present_state_dd    #(By.ID, "mui-component-select-state")
        options_xpath = "//ul[@role='listbox']/li"
        self.select_random_option(dropdown, options_xpath)

    def select_present_random_district(self):
        dropdown = self.present_district_dd     # (By.ID, "mui-component-select-district")
        options_xpath = "//ul[@role='listbox']/li"
        self.select_random_option(dropdown, options_xpath)

    def ensure_same_as_present_checkbox_unselected(self):
        checkbox = self.driver.find_element(*self.same_as_present_checkbox)
        if checkbox.is_selected():
            checkbox.click()  # Unselect it
        assert not checkbox.is_selected(), "Checkbox should remain unselected"

###### PERMANENT ADDRESS --- #######
    def enter_permanent_house_num(self, houseno):
        self.driver.find_element(*self.permanent_house_num).clear()
        self.driver.find_element(*self.permanent_house_num).send_keys(houseno)

    def enter_permanent_street(self, street):
        self.driver.find_element(*self.permanent_street).clear()
        self.driver.find_element(*self.permanent_street).send_keys(street)

    def enter_permanent_town(self, town):
        self.driver.find_element(*self.permanent_town).clear()
        self.driver.find_element(*self.permanent_town).send_keys(town)

    def enter_permanent_policestation(self, police):
        self.driver.find_element(*self.permanent_policestation).clear()
        self.driver.find_element(*self.permanent_policestation).send_keys(police)

    def enter_permanent_postoffice(self, post):
        self.driver.find_element(*self.permanent_postoffice).clear()
        self.driver.find_element(*self.permanent_postoffice).send_keys(post)

    def enter_permanent_pincode(self, zip):
        self.driver.find_element(*self.permanent_pincode).clear()
        self.driver.find_element(*self.permanent_pincode).send_keys(zip)

    def enter_permanent_city(self, city):
        self.driver.find_element(*self.permanent_city).clear()
        self.driver.find_element(*self.permanent_city).send_keys(city)

    def select_permanent_random_state(self):
        dropdown = self.permanent_state_dd   #(By.ID, "mui-component-select-state")
        options_xpath = "//ul[@role='listbox']/li"
        self.select_random_option(dropdown, options_xpath)

    def select_permanent_random_district(self):
        dropdown = self.permanent_district_dd     #    (By.ID, "mui-component-select-district")
        options_xpath = "//ul[@role='listbox']/li"
        self.select_random_option(dropdown, options_xpath)

    def fill_basic_details(self):
        self.select_random_nationality()
        self.select_random_religion()
        self.select_random_caste()
        self.select_random_ph_vh_option()
        self.select_random_blood_group()
        self.select_maritial_status()
        self.enter_height("170")
        self.enter_identification("Random ID marks")
        self.enter_present_house_num("B-189")
        self.enter_present_street("Some Street")
        self.enter_present_town("Sunabeda")
        self.enter_present_policestation("XYZ Police")
        self.enter_present_postoffice("ABC Post")
        self.enter_present_pincode("765123")
        self.enter_present_city("Koraput")
        self.select_present_random_state()
        self.select_present_random_district()
        self.enter_permanent_house_num("HIG 77")
        self.enter_permanent_street("Harvard St")
        self.enter_permanent_town("Medford")
        self.enter_permanent_policestation("Mystic Ave Police")
        self.enter_permanent_postoffice("P/O-4R5678")
        self.enter_permanent_pincode("02155")
        self.enter_permanent_city("Boston")
        self.select_permanent_random_state()
        self.select_permanent_random_district()
        next_button = self.driver.find_element(By.XPATH, "//button[@type='submit' and text()='Next']")
        next_button.click()

    #################---------------------------------------------###########################
    #################---------------------------------------------###########################

    ######### ------Pay Structure Details-------####### ( page after personal information details)
    select_group_dd = (By.ID, "mui-component-select-groupId")
    posted_designation_dd = (By.XPATH, "//fieldset[contains(@class, 'MuiOutlinedInput-notchedOutline')]"
                                       "//legend[span[text()='Posted Designation']]")
    posted_designation_input_b = (
        By.XPATH, "//label[text()='Posted Designation']/following-sibling::div//input[@role='combobox']")
    gazetted_yes_radio = (By.XPATH, "//input[@name='isGazetted' and @value='true']")
    gazetted_no_radio = (By.XPATH, "//input[@name='isGazetted' and @value='false']")
    cadre_radio = (By.XPATH, "//input[@name='isCadre' and @value='true']")
    non_cadre_radio = (By.XPATH, "//input[@name='isCadre' and @value='false']")
    select_cadre_dropdown = (By.XPATH,"//label[normalize-space()='Select Cadre']/following-sibling::div//div[@role='combobox']")
    posting_radio = (By.XPATH, "//input[@name='postingType' and @value='Posting']")
    deputation_radio = (By.XPATH, "//input[@name='postingType' and @value='Deputation']")
    ttaadc_yes = (By.XPATH, "//input[@name='isPostedAtTtaadc' and @value='true']") ##check this the value doesnt change to false
    ttaadc_no = (By.XPATH, "//input[@name='isPostedAtTtaadc' and @value='false']")
    posted_outside_state_yes = (By.XPATH, "//input[@name='isPostedOutsideState' and @value='true']")
    posted_outside_state_no = (By.XPATH, "//input[@name='isPostedOutsideState' and @value='false']")
    calendar_icon_button = (By.XPATH, "//label[text()='Effected From']/following::button[@aria-label='Choose date'][1]")
    select_payband_dropdown = (
        By.XPATH, "//label[normalize-space()='Select PayBand']/following-sibling::div//div[@role='combobox']")
    select_grade_pay_dropdown = (
        By.XPATH, "//label[normalize-space()='Select Grade Pay']/following-sibling::div//div[@role='combobox']")
    gis_yes_radio = (By.XPATH, "//input[@name='isApplicableForGis' and @value='true']")
    gis_no_radio = (By.XPATH, "//input[@name='isApplicableForGis' and @value='false']")
    next_increment_dropdown = (By.XPATH,"//label[text()='Next Increment']/following-sibling::div//div[@role='combobox']")
    pay_structure_next_btn = (By.XPATH, "//button[@type='submit' and @form='form-Pay Structure Details']")



    def select_random_radio(self, yes_locator, no_locator):
        selected_locator = random.choice([yes_locator, no_locator])
        self.driver.find_element(*selected_locator).click()
        #print(f"Selected radio option: {'Yes' if selected_locator == yes_locator else 'No'}")


    def select_group(self):
        self.select_random_option(self.select_group_dd, "//ul[@role='listbox']//li")



    def select_group_A(self):
        # 1. Click on the dropdown to open the options
        dropdown = self.driver.find_element(By.ID, "mui-component-select-groupId")
        dropdown.click()

        # 2. Wait for the list with role="listbox", then click the first item
        first_option = WebDriverWait(self.driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, "(//ul[@role='listbox']//li)[1]"))
        )
        first_option.click()



    def select_posted_designation(self):
        self.select_random_option(self.posted_designation_input_b, "//ul[@role='listbox']//li")

    def select_gazetted(self):
        self.select_random_radio(self.gazetted_yes_radio, self.gazetted_no_radio)

    def select_cadre_status(self):
        self.select_random_radio(self.cadre_radio, self.non_cadre_radio)

    def select_cadre(self):
        self.select_random_option(self.select_cadre_dropdown, "//ul[@role='listbox']//li")

    def select_posting_type(self):
        self.select_random_radio(self.posting_radio, self.deputation_radio)

    def select_ttaadc_posting(self):
        self.select_random_radio(self.ttaadc_yes, self.ttaadc_no)

    def select_posted_outside_state(self):
        self.select_random_radio(self.posted_outside_state_yes, self.posted_outside_state_no)
    #


    def pick_effected_from_date(self):
        # Click the calendar icon (use JavaScript in case it's overlaid)
        calendar_icon = self.driver.find_element(
            By.XPATH, "//label[text()='Effected From']/following::button[@aria-label='Choose date'][1]"
        )
        self.driver.execute_script("arguments[0].click();", calendar_icon)

        # Wait for the date picker to be visible
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@role='gridcell' and @tabindex='0']"))
        )

        # Select the first focusable date (usually today)
        self.driver.find_element(By.XPATH, "//button[@role='gridcell' and @tabindex='0']").click()

        # Optionally wait for calendar to close
        time.sleep(1)

    def select_payband(self):
        self.select_random_option(self.select_payband_dropdown, "//ul[@role='listbox']//li")

    def select_grade_pay(self):
        self.select_random_option(self.select_grade_pay_dropdown, "//ul[@role='listbox']//li")

    def select_gis_eligibility(self):
        self.select_random_radio(self.gis_yes_radio, self.gis_no_radio)


    def select_next_increment(self):
        #self.driver.find_element(*self.next_increment_dropdown).click()
        self.select_random_option(self.next_increment_dropdown, "//ul[@role='listbox']//li")
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown)
        # time.sleep(0.5)


    def click_pay_structure_next(self):
        self.driver.find_element(*self.pay_structure_next_btn).click()



    #################---------------------------------------------###########################
    #################---------------------------------------------###########################
    #------GENERAL INFORMATION --#########
    select_bank_dd = (By.XPATH, '//label[text()="Select Bank"]/following-sibling::div[contains(@class,"MuiOutlinedInput-root")]')
    select_branch_dd =  (By.XPATH, "//label[text()='Select Branch']/following-sibling::div//input[@role='combobox']")
    account_num_input = (By.NAME, "accountNo")
    # pension_yes_radio = (By.XPATH, '//fieldset[.//h6[text()="Entitlement to Pension"]]'
    #                          '//input[@name="entitlementsPension" and @value="true"]')
    pension_yes = (By.CSS_SELECTOR, 'input[type="radio"][name="entitlementsPension"][value="true"]')
    pension_no = (By.CSS_SELECTOR, 'input[type="radio"][name="entitlementsPension"][value="false"]')
    retirement_fund_UPS = (By.CSS_SELECTOR,'input[name="retirementFundType"][value="UPS"]')
    retirement_fund_NPS = (By.CSS_SELECTOR, 'input[name="retirementFundType"][value="NPS"]')
    retirement_fund_GPF = (By.CSS_SELECTOR, 'input[name="retirementFundType"][value="GPF"]')
    PF_account_no_input = (By.NAME, "retirementFundAccountNo")
    NPA_applicable_yes = (By.CSS_SELECTOR, 'input[name="npaApplicable"][value="true"]')
    NPA_applicable_no = (By.CSS_SELECTOR, 'input[name="npaApplicable"][value="false"]')
    NPA_amount = (By.NAME, "npaAmount")
    select_head_of_account_dd = (By.XPATH, '//label[text()="Head of Account"]/following-sibling'
                                    '::div[contains(@class,"MuiOutlinedInput-root")]')
    quater_yes = (By.CSS_SELECTOR, 'input[name="quarterOccupied"][value="true"]')
    quater_no = (By.CSS_SELECTOR, 'input[name="quarterOccupied"][value="false"]')
    quater_type_dd = (By.ID, "mui-component-select-quarterId")
    govt_quater_number_input = (By.NAME, "quarterNo")
    select_treasury_dd = (By.XPATH, '//label[text()="Select Treasury"]'
                                 '/following-sibling::div[contains(@class,"MuiAutocomplete-inputRoot")]')
    click_submit_preview_btn = (By.XPATH, "//button[normalize-space(text())='Submit & Preview']")

    ##METHODS##
    def select_bank(self):
        self.select_random_option(self.select_bank_dd,"//ul[@role='listbox']//li")

    def select_branch(self):
        self.select_random_option(self.select_branch_dd,"(//ul[@role='listbox']//li)")

    def input_account_number(self, accountno):
        self.driver.find_element(*self.account_num_input).send_keys(accountno)

    def entitlement_to_pension(self):
        self.select_random_radio(self.pension_yes, self.pension_no)

    def retirement_fund_type(self):
        self.select_random_radio(self.retirement_fund_NPS, self.retirement_fund_UPS)

    def input_pf_account(self, pfaccountno):
        self.driver.find_element(*self.PF_account_no_input).send_keys(pfaccountno)

    def npa_applicable(self):
        self.select_random_radio(self.NPA_applicable_yes, self.NPA_applicable_no)

    def input_npa_amount(self, amount):
        ele = self.driver.find_element(*self.NPA_amount)
        ele.clear()
        ele.send_keys(amount)

    def select_head_of_account(self):
        self.select_random_option(self.select_head_of_account_dd,"//ul[@role='listbox']//li")

    def quater_occupied(self):
        self.select_random_radio(self.quater_yes, self.quater_no)

    def select_quater_type(self):
        self.select_random_option(self.quater_type_dd,"//ul[@role='listbox']//li" )

    def govt_quater_no(self, quaterno):
        self.driver.find_element(*self.govt_quater_number_input).send_keys(quaterno)

    def select_treasury(self):
        self.driver.find_element(*self.select_treasury_dd).clear()
        self.select_random_option(self.select_treasury_dd,"//ul[@role='listbox']//li")

    def click_submit_preview(self):
        self.driver.find_element(*self.click_submit_preview_btn).click()


