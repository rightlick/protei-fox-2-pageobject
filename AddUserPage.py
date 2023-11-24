from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ProteiAddUserLocators:

    LOCATOR_PROTEI_CHECK_ADD_USER = (By.TAG_NAME, "legend")

    LOCATOR_PROTEI_ADD_USER_EMAIL = (By.ID, "dataEmail")
    LOCATOR_PROTEI_ADD_USER_PASSWORD = (By.ID, "dataPassword")
    LOCATOR_PROTEI_ADD_USER_NAME = (By.ID, "dataName")

    LOCATOR_PROTEI_ADD_USER_SEX = (By.TAG_NAME, "select")

    # RADIO BUTTON
    LOCATOR_PROTEI_ADD_USER_VARIANT_1_1 = (By.ID, "dataSelect11")
    LOCATOR_PROTEI_ADD_USER_VARIANT_1_2 = (By.ID, "dataSelect12")

    # CHECKBOX
    LOCATOR_PROTEI_ADD_USER_VARIANT_2_1 = (By.ID, "dataSelect21")
    LOCATOR_PROTEI_ADD_USER_VARIANT_2_2 = (By.ID, "dataSelect22")
    LOCATOR_PROTEI_ADD_USER_VARIANT_2_3 = (By.ID, "dataSelect23")

    # BUTTON
    LOCATOR_PROTEI_ADD_USER_BUTTON = (By.ID, "dataSend")

    # MODAL WINDOW
    LOCAL_PROTEI_ADD_USER_MODAL = (By.CLASS_NAME, "uk-modal-dialog")
    LOCAL_PROTEI_ADD_USER_MODAL_BUTTON = (By.XPATH, "//div/div/div/button")

    # ALERTS
    LOCAL_PROTEI_ADD_USER_ALERT_EMAIL = (By.ID, "emailFormatError")
    LOCAL_PROTEI_ADD_USER_ALERT_PASSWORD = (By.ID, "blankPasswordError")
    LOCAL_PROTEI_ADD_USER_ALERT_NAME = (By.ID, "blankNameError")




class AddUser(BasePage):

    def check_add_user_page(self):
        add_user = self.find_element(ProteiAddUserLocators.LOCATOR_PROTEI_CHECK_ADD_USER)
        return add_user

    def enter_email(self, email):
        search_field = self.find_element(ProteiAddUserLocators.LOCATOR_PROTEI_ADD_USER_EMAIL)
        search_field.click()
        search_field.send_keys(email)
        return search_field

    def enter_password(self, password):
        search_field = self.find_element(ProteiAddUserLocators.LOCATOR_PROTEI_ADD_USER_PASSWORD)
        search_field.click()
        search_field.send_keys(password)
        return search_field

    def enter_name(self, name):
        search_field = self.find_element(ProteiAddUserLocators.LOCATOR_PROTEI_ADD_USER_NAME)
        search_field.click()
        search_field.send_keys(name)
        return search_field

    def enter_sex(self, sex):
        search_field = self.find_element(ProteiAddUserLocators.LOCATOR_PROTEI_ADD_USER_SEX)
        select_sex = Select(search_field)

        select_sex.select_by_index(0)
        select_sex.select_by_index(1)

        if sex == 0:
            select_sex.select_by_index(0)
        elif sex == 1:
            select_sex.select_by_index(1)
        return select_sex

    def enter_radio_button(self, variant_1):
        add_user_variant_1_1 = self.find_element(ProteiAddUserLocators.LOCATOR_PROTEI_ADD_USER_VARIANT_1_1)
        add_user_variant_1_2 = self.find_element(ProteiAddUserLocators.LOCATOR_PROTEI_ADD_USER_VARIANT_1_2)

        add_user_variant_1_1.click()
        add_user_variant_1_2.click()

        if variant_1 == 1:
            add_user_variant_1_1.click()
        elif variant_1 == 2:
            add_user_variant_1_2.click()
        return variant_1

    def enter_checkbox(self, variant_2):
        add_user_variant_2_1 = self.find_element(ProteiAddUserLocators.LOCATOR_PROTEI_ADD_USER_VARIANT_2_1)
        add_user_variant_2_2 = self.find_element(ProteiAddUserLocators.LOCATOR_PROTEI_ADD_USER_VARIANT_2_2)
        add_user_variant_2_3 = self.find_element(ProteiAddUserLocators.LOCATOR_PROTEI_ADD_USER_VARIANT_2_3)

        # 1 по первому чекбоксу, чтобы снять дефолтную настройку
        add_user_variant_2_1.click()

        if variant_2 == 1:
            add_user_variant_2_1.click()
        elif variant_2 == 2:
            add_user_variant_2_2.click()
        elif variant_2 == 3:
            add_user_variant_2_3.click()
        return variant_2

    def click_on_the_add_button(self):
        add_user = self.find_element(ProteiAddUserLocators.LOCATOR_PROTEI_ADD_USER_BUTTON, 10)
        add_user.click()
        return add_user

    def check_modal_success(self):
        modal = self.find_element(ProteiAddUserLocators.LOCAL_PROTEI_ADD_USER_MODAL)
        return modal

    def click_modal_button(self):
        modal_button = self.find_element(ProteiAddUserLocators.LOCAL_PROTEI_ADD_USER_MODAL_BUTTON)
        return modal_button

    def check_modal_fail(self):
        modal = self.find_element(ProteiAddUserLocators.LOCAL_PROTEI_ADD_USER_MODAL)
        return modal

    def check_alert_fail_email(self):
        modal = self.find_element(ProteiAddUserLocators.LOCAL_PROTEI_ADD_USER_ALERT_EMAIL)
        return modal

    def check_alert_fail_password(self):
        modal = self.find_element(ProteiAddUserLocators.LOCAL_PROTEI_ADD_USER_ALERT_PASSWORD)
        return modal

    def check_alert_fail_name(self):
        modal = self.find_element(ProteiAddUserLocators.LOCAL_PROTEI_ADD_USER_ALERT_NAME)
        return modal
