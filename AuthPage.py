from BaseApp import BasePage
from selenium.webdriver.common.by import By
from MainPage import Navigation


class ProteiAuthLocators:

    LOCATOR_PROTEI_AUTH_EMAIL = (By.ID, "loginEmail")
    LOCATOR_PROTEI_AUTH_PASSWORD = (By.ID, "loginPassword")
    LOCATOR_PROTEI_AUTH_BUTTON = (By.ID, "authButton")

    LOCATOR_PROTEI_CHECK_AUTH = (By.CLASS_NAME, "uk-fieldset")


class Authorization(BasePage):

    def enter_email(self, email):
        search_field = self.find_element(ProteiAuthLocators.LOCATOR_PROTEI_AUTH_EMAIL)
        search_field.click()
        search_field.send_keys(email)
        return search_field

    def enter_password(self, password):
        search_field = self.find_element(ProteiAuthLocators.LOCATOR_PROTEI_AUTH_PASSWORD)
        search_field.click()
        search_field.send_keys(password)
        return search_field

    def click_on_the_authorization_button(self, browser):
        self.find_element(ProteiAuthLocators.LOCATOR_PROTEI_AUTH_BUTTON).click()
        return Navigation(browser)

    def check_auth_page(self):
        auth = self.find_element(ProteiAuthLocators.LOCATOR_PROTEI_CHECK_AUTH).click()
        return auth
