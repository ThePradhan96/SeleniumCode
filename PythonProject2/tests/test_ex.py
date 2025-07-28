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

@pytest.mark.usefixtures("login_successfully")
class TestAddNew1:
    def test_enter_appointment_order_date(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        add_emp_page.navigate_to_add_employee()
        # add_emp_page.enter_appointment_order_date()
        add_emp_page.pick_app_order_date()
        or_value = ls.find_element(*add_emp_page.app_order_date).get_attribute("value")

    def test_pick_joining_date(self, login_successfully):
        ls = login_successfully
        add_emp_page = AddNewEmployeePage(ls)
        add_emp_page.navigate_to_add_employee()
        # Trigger the selection of day '1' as joining date
        add_emp_page.pick_joining_date()

        # Retrieve value after picking date
        doj_value = ls.find_element(*add_emp_page.DOJ).get_attribute("value")

        assert doj_value.startswith("01"), f"Expected DOJ date with day ‘01…’, but got '{doj_value}'"