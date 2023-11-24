from BaseApp import BasePage
from selenium.webdriver.common.by import By


class ProteiAddUserLocators:

    LOCATOR_PROTEI_CHECK_ADD_USER = (By.TAG_NAME, "legend")

    # LOCATOR_PROTEI_USERS_BUTTON = (By.CLASS_NAME, "uk-button uk-button-primary")


class AddUser(BasePage):

    def check_add_user_page(self):
        add_user = self.find_element(ProteiAddUserLocators.LOCATOR_PROTEI_CHECK_ADD_USER)
        return add_user

    # def click_on_the_users_button(self, browser):
    #     self.find_element(ProteiUsersLocators.LOCATOR_PROTEI_USERS_BUTTON).click()
    #     return (browser)