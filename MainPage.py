from BaseApp import BasePage
from selenium.webdriver.common.by import By
from VariantsPage import Variants
from UsersPage import Users
from AddUserPage import AddUser


class ProteiMainLocators:

    LOCATOR_PROTEI_MAIN_TAB_AUTH = (By.ID, "menuAuth")
    LOCATOR_PROTEI_MAIN_TAB_MAIN = (By.ID, "menuMain")
    LOCATOR_PROTEI_MAIN_TAB_USERS = (By.ID, "menuUsersOpener")
    LOCATOR_PROTEI_MAIN_DROPDOWN_USERS_TABLE = (By.ID, "menuUsers")
    LOCATOR_PROTEI_MAIN_DROPDOWN_ADD_USER = (By.ID, "menuUserAdd")
    LOCATOR_PROTEI_MAIN_TAB_VARIANTS = (By.ID, "menuMore")

    LOCATOR_PROTEI_CHECK_AUTH = (By.CLASS_NAME, "uk-fieldset")
    LOCATOR_PROTEI_CHECK_HELLO = (By.TAG_NAME, "h3")


class Navigation(BasePage):

    def check_main_page(self):
        hello = self.find_element(ProteiMainLocators.LOCATOR_PROTEI_CHECK_HELLO, time=5)
        return hello

    def click_on_the_users_tab(self, browser):
        click = self.find_element(ProteiMainLocators.LOCATOR_PROTEI_MAIN_TAB_USERS, time=5)
        click.click()
        click.click()
        return Users(browser)

    def click_on_the_users_table_dropdown(self, browser):
        self.find_element(ProteiMainLocators.LOCATOR_PROTEI_MAIN_TAB_USERS, time=5).click()
        self.find_element(ProteiMainLocators.LOCATOR_PROTEI_MAIN_DROPDOWN_USERS_TABLE, time=5).click()
        return Users(browser)

    def click_on_the_add_user_dropdown(self, browser):
        self.find_element(ProteiMainLocators.LOCATOR_PROTEI_MAIN_TAB_USERS, time=5).click()
        self.find_element(ProteiMainLocators.LOCATOR_PROTEI_MAIN_DROPDOWN_ADD_USER, time=5).click()
        return AddUser(browser)

    def click_on_the_variants_tab(self, browser):
        self.find_element(ProteiMainLocators.LOCATOR_PROTEI_MAIN_TAB_VARIANTS, time=5).click()
        return Variants(browser)
