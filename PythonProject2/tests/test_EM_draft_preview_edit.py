
from conftest import login_successfully
from pages.EM_draft_list_edit_fields  import EditPreviewDraftPage
from pages.EM_draft_list import EMDraftListPage


class TestEMPreviewEdit:
    def test_edit_bank_branch_account_and_verify_preview(self, login_successfully):
        ls = login_successfully
        page = EditPreviewDraftPage(ls)
        draftpage = EMDraftListPage(ls)
        draftpage.navigate_to_draft_continuation()

        # Step A: Capture original values (if you want)
        bank_name = page.get_bank_detail_value("Bank Name")
        branch_name = page.get_bank_detail_value("Branch Name")
        account_no = page.get_bank_detail_value("Account No")
        ifsc = page.get_bank_detail_value("IFSC Code")

        print("Original Preview values:", bank_name, branch_name, account_no)

        # Step B: Go back and edit
        page.click_previous_to_edit()
        new_bank = "PUNJAB NATIONAL BANK"
        new_branch = "UBI AMBASSA"
        new_account = "999999999999"
        page.select_bank(new_bank)
        page.select_branch(new_branch)
        page.input_account_number(new_account)
        draftpage.select_head_of_account()

        # Step C: Re-submit and navigate back to Preview
        #page.resubmit_preview()
        draftpage.click_submit_preview()

        # Step D: Assert that changes are reflected
        assert page.get_bank_detail_value("AccountBalanceIcon") == new_bank, "Bank not updated correctly"
        assert page.get_bank_detail_value("Branch Name") == new_branch, "Branch not updated correctly"
        assert page.get_bank_detail_value("Account No") == new_account  , "Account No not updated correctly"

    def test_edit_bank_branch_account_and_verify_preview(self, login_successfully):
        ls = login_successfully
        page = EditPreviewDraftPage(ls)
        draftpage = EMDraftListPage(ls)
        draftpage.navigate_to_draft_continuation()

        # Step A: Capture original values
        bank_name = page.get_bank_detail_value("Bank Name")
        branch_name = page.get_bank_detail_value("Branch Name")
        account_no = page.get_bank_detail_value("Account No")
        ifsc = page.get_bank_detail_value("IFSC Code")

        print("Original Preview values:", bank_name, branch_name, account_no, ifsc)

        # Step B: Go back and edit
        page.click_previous_to_edit()
        new_bank = "PUNJAB NATIONAL BANK"
        new_branch = "UBI AMBASSA"
        new_account = "999999999999"
        page.select_bank(new_bank)
        page.select_branch(new_branch)
        page.input_account_number(new_account)
        draftpage.select_head_of_account()

        # Step C: Re-submit
        draftpage.click_submit_preview()

        # Step D: Re-fetch updated values
        updated_bank = page.get_bank_detail_value("Bank Name")
        updated_branch = page.get_bank_detail_value("Branch Name")
        updated_account = page.get_bank_detail_value("Account No")

        assert updated_bank == new_bank, f"Bank not updated correctly: got {updated_bank}"
        assert updated_branch == new_branch, f"Branch not updated correctly: got {updated_branch}"
        assert updated_account == new_account, f"Account No not updated correctly: got {updated_account}"

    def test_edit_other_details_and_verify_preview(self, login_successfully):
        ls = login_successfully
        page = EditPreviewDraftPage(ls)
        draftpage = EMDraftListPage(ls)
        draftpage.navigate_to_draft_continuation()

        # Step A: Capture preview values
        fund_type = page.get_other_detail_value("Retirement Fund Type")
        fund_account = page.get_other_detail_value("Retirement Fund Account No")
        quarter = page.get_other_detail_value("Quarter Occupied")
        hoa = page.get_other_detail_value("HOA Details")
        #treasury = page.get_other_detail_value("Treasury")
        pension = page.get_other_detail_value("Entitled for Pension")

        print("Original values:", fund_type, fund_account, quarter, hoa,pension)

        # Step B: Go back to edit
        page.click_previous_to_edit()

        # Step C: Update values
        page.retirement_fund_type("NPS")
        page.input_pf_account("T/J/708")
        page.quater_occupied("No")
        page.entitlement_to_pension("Yes")
        page.select_head_of_account("2054-00-97-07-05-01")

        # Step D: Submit preview again
        draftpage.click_submit_preview()

        # Step E: Validate updated preview values
        assert page.get_other_detail_value("Retirement Fund Type") == "NPS"
        assert page.get_other_detail_value("Retirement Fund Account No") == "T/J/999"
        assert page.get_other_detail_value("Quarter Occupied") == "Yes"
        assert page.get_other_detail_value("HOA Details") == "2210-06-001-98-52-01"
        assert page.get_other_detail_value("Treasury") == "KAILASHAHAR TREASURY"
        assert page.get_other_detail_value("Entitled for Pension") == "No"
