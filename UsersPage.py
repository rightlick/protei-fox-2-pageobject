from BaseApp import BasePage
from selenium.webdriver.common.by import By


class ProteiUsersLocators:

    LOCATOR_PROTEI_CHECK_USERS = (By.ID, "usersPage")

    LOCATOR_PROTEI_USERS_BUTTON = (By.CLASS_NAME, "uk-button uk-button-primary")


class Users(BasePage):

    def check_users_page(self):
        users = self.find_element(ProteiUsersLocators.LOCATOR_PROTEI_CHECK_USERS)
        return users

    # def click_on_the_users_button(self, browser):
    #     self.find_element(ProteiUsersLocators.LOCATOR_PROTEI_USERS_BUTTON).click()
    #     return (browser)