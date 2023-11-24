from BaseApp import BasePage
from selenium.webdriver.common.by import By


class ProteiVariantsLocators:

    LOCATOR_PROTEI_CHECK_VARIANTS = (By.TAG_NAME, "h3")


class Variants(BasePage):

    def check_variants_page(self):
        var = self.find_element(ProteiVariantsLocators.LOCATOR_PROTEI_CHECK_VARIANTS)
        return var
