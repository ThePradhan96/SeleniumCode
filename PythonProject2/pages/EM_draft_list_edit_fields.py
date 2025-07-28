from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.EM_draft_list import EMDraftListPage

class EditPreviewDraftPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # Locators
    select_bank_dd = (By.XPATH, '//label[text()="Select Bank"]/following-sibling::div[contains(@class,"MuiOutlinedInput-root")]')
    select_branch_dd = (By.XPATH, "//label[text()='Select Branch']/following-sibling::div//input[@role='combobox']")
    account_num_input = (By.NAME, "accountNo")
    previous_button = (By.XPATH, "//button[normalize-space(text())='Previous']")
    submit_preview_button = (By.XPATH, "//button[normalize-space(text())='Submit & Preview']")

    # def get_preview_field(self, label_text):
    #     #xpath = f"//label[normalize-space(text())='{label_text}']/following-sibling::div"
    #     xpath = f"//label[contains(normalize-space(.), '{label_text}')]/following-sibling::div"
    #     #self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    #     print("Trying to find preview field for label:", label_text)
    #     print("Using xpath:", xpath)
    #     WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    #     return self.driver.find_element(By.XPATH, xpath).text.strip()


    #
    # def get_bank_detail_value(self, label_text, timeout=10):
    #     """
    #     Returns the text value associated with a label (e.g., 'Bank Name') inside the 'Bank Details' card.
    #     """
    #     wait = WebDriverWait(self.driver, timeout)
    #
    #     # Locate the "Bank Details" card block
    #     card_xpath = "//h6[normalize-space()='Bank Details']/ancestor::div[contains(@class, 'MuiCard-root')]"
    #     bank_card = wait.until(EC.presence_of_element_located((By.XPATH, card_xpath)))
    #
    #     ####### Locate the label inside that card
    #     label_xpath = f".//h6[normalize-space()='{label_text}']/ancestor::div[contains(@class,'MuiGrid-item')]"
    #     label_container = bank_card.find_element(By.XPATH, label_xpath)
    #
    #     # Locate the corresponding value (usually in the next sibling grid item)
    #     value_xpath = "./following-sibling::div[contains(@class,'MuiGrid-item')]//p"
    #     value_elem = label_container.find_element(By.XPATH, value_xpath)
    #
    #
    #     # Ensure visibility by scrolling if needed
    #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", value_elem)
    #     #
    #     return value_elem.text.strip()
    #

    def click_previous_to_edit(self):
        self.wait.until(EC.element_to_be_clickable(self.previous_button)).click()

    def resubmit_preview(self):
        self.wait.until(EC.element_to_be_clickable(self.submit_preview_button)).click()
        # Wait until preview header appears (optional but recommended)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space(text())='Preview']")))

    def select_bank(self, bank_name):
        self.driver.find_element(*self.select_bank_dd).click()
        opt = f"//ul[@role='listbox']//li[normalize-space()='{bank_name}']"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, opt))).click()

    def select_branch(self, branch_name):
        self.driver.find_element(*self.select_branch_dd).click()
        opt = f"//ul[@role='listbox']//li[normalize-space()='{branch_name}']"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, opt))).click()

    def input_account_number(self, accountno):
        elem = self.driver.find_element(*self.account_num_input)
        elem.clear()
        elem.send_keys(accountno)

    def get_bank_detail_value(self, label_text, timeout=10):
        """
        Returns the text value associated with a label (e.g., 'Bank Name') inside the 'Bank Details' card.
        Always fetches the FRESH element after any page update.
        """
        wait = WebDriverWait(self.driver, timeout)

        # Locate the "Bank Details" card fresh every time
        card_xpath = "//h6[normalize-space()='Bank Details']/ancestor::div[contains(@class, 'MuiCard-root')]"
        bank_card = wait.until(EC.presence_of_element_located((By.XPATH, card_xpath)))

        # Match label (flexible, uses contains to avoid spacing issues)
        label_xpath = f".//h6[contains(normalize-space(.), '{label_text}')]/ancestor::div[contains(@class,'MuiGrid-item')]"
        label_container = bank_card.find_element(By.XPATH, label_xpath)

        # Find the value next to the label
        value_xpath = "./following-sibling::div[contains(@class,'MuiGrid-item')]//p"
        value_elem = label_container.find_element(By.XPATH, value_xpath)

        # Scroll into view (optional but useful if hidden)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", value_elem)

        # Return trimmed text
        return value_elem.text.strip()

    def get_other_detail_value(self, label_text, timeout=10):
        """
        Safely returns the value text for a given label in 'Other Details' section.
        """
        wait = WebDriverWait(self.driver, timeout)

        # Step 1: Locate the 'Other Details' card
        card_xpath = "//h6[normalize-space()='Other Details']/ancestor::div[contains(@class, 'MuiCard-root')]"
        card = wait.until(EC.presence_of_element_located((By.XPATH, card_xpath)))

        # Step 2: Within that card, find all row blocks (each label-value is inside a MuiGrid-container)
        rows = card.find_elements(By.XPATH, ".//div[contains(@class, 'MuiGrid-container')]")

        # Step 3: Loop through rows to find label match
        for row in rows:
            try:
                label_el = row.find_element(By.XPATH, ".//h6[normalize-space()='" + label_text + "']")
                value_el = row.find_element(By.XPATH, ".//p")
                # Scroll to value
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", value_el)
                return value_el.text.strip()
            except:
                continue  # move to next row if label not found

        raise Exception(f"Label '{label_text}' not found in 'Other Details'")

    def entitlement_to_pension(self, value=None):
        if value is not None:
            if value.lower() == "yes":
                self.driver.find_element(*self.pension_yes).click()
            elif value.lower() == "no":
                self.driver.find_element(*self.pension_no).click()
        else:
            self.select_random_radio(self.pension_yes, self.pension_no)

    def retirement_fund_type(self, value=None):
        if value is not None:
            if value.upper() == "NPS":
                self.driver.find_element(*self.retirement_fund_NPS).click()
            elif value.upper() == "UPS":
                self.driver.find_element(*self.retirement_fund_UPS).click()
        else:
            self.select_random_radio(self.retirement_fund_NPS, self.retirement_fund_UPS)

    def input_pf_account(self, pfaccountno):
        ele = self.driver.find_element(*self.PF_account_no_input)
        ele.clear()
        ele.send_keys(pfaccountno)

    def npa_applicable(self, value=None):
        if value is not None:
            if value.lower() == "yes":
                self.driver.find_element(*self.NPA_applicable_yes).click()
            elif value.lower() == "no":
                self.driver.find_element(*self.NPA_applicable_no).click()
        else:
            self.select_random_radio(self.NPA_applicable_yes, self.NPA_applicable_no)

    def input_npa_amount(self, amount):
        ele = self.driver.find_element(*self.NPA_amount)
        ele.clear()
        ele.send_keys(amount)

    def select_head_of_account(self, option_text=None):
        if option_text:
            self.select_dropdown_by_text(self.select_head_of_account_dd, option_text)
        else:
            self.select_random_option(self.select_head_of_account_dd, "//ul[@role='listbox']//li")

    def quater_occupied(self, value=None):
        if value is not None:
            if value.lower() == "yes":
                self.driver.find_element(*self.quater_yes).click()
            elif value.lower() == "no":
                self.driver.find_element(*self.quater_no).click()
        else:
            self.select_random_radio(self.quater_yes, self.quater_no)

    def select_quater_type(self, option_text=None):
        if option_text:
            self.select_dropdown_by_text(self.quater_type_dd, option_text)
        else:
            self.select_random_option(self.quater_type_dd, "//ul[@role='listbox']//li")

    def govt_quater_no(self, quaterno):
        ele = self.driver.find_element(*self.govt_quater_number_input)
        ele.clear()
        ele.send_keys(quaterno)
