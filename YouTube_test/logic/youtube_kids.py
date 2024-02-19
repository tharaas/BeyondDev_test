from selenium.webdriver.common.by import By
from infra.base_page import BasePage


class youtubeKids(BasePage):

    KID_BUTTON_YOUTUBE_KIDS = "kid-button"
    PARENT_BUTTON_YOUTUBE_KIDS = "parent-button"

    def __init__(self, driver):
        super().__init__(driver)
        self.kid = self._driver.find_element(By.ID, "kid-button")

    def setting_up_account_on_YouTube_Kids_as_a_kid(self):
        self.kid.click()

    def setting_up_account_on_YouTube_Kids_as_a_parent(self):
        self.parent_button = self._driver.find_element(By.ID, self.PARENT_BUTTON_YOUTUBE_KIDS)
        self.parent_button.click()
