from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from infra.base_page import BasePage


class youtubePage(BasePage):

    MENU_INPUT = "guide-icon"
    YOUTUBE_KIDS_BUTTON = "//ytd-guide-section-renderer[5]/div/ytd-guide-entry-renderer[3]/a[@id='endpoint']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_menu_button(self):
        self.menu_button = self._driver.find_element(By.ID, self.MENU_INPUT)
        self.menu_button.click()

    def click_on_youtube_kids_button(self):
        self.youtube_kids_button = self._driver.find_element(By.XPATH, self.YOUTUBE_KIDS_BUTTON)
        self.youtube_kids_button.click()
        self.url_youtube_kids = self.youtube_kids_button.get_attribute("href")
        return self.url_youtube_kids

    def open_youtube_kids_through_menu_button(self):
        self.click_on_menu_button()
        return self.click_on_youtube_kids_button()
