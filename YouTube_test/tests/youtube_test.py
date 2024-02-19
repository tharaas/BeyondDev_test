import unittest
import time

from selenium.common import ElementNotInteractableException
from selenium.webdriver.common.by import By
from infra.browser_wrapper import browserWrapper
from logic.youtube_page import youtubePage


class YouTubePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = browserWrapper()
        self.base_url = "https://www.youtube.com/"
        self.driver = self.browser.get_driver(self.base_url)
        self.youtube_page = youtubePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_click_on_youtube_kids_to_open(self):
        print("Test Name: Click on YouTube Kids from youtube menu")
        print(self.base_url)
        #logic
        self.base_url = self.youtube_page.open_youtube_kids_through_menu_button()
        #change the url for the new page (Youtube kids)
        #inra
        self.driver = self.browser.get_driver(self.base_url)
        print(self.base_url)
        time.sleep(3)
        #test

    def test_setting_up_account_on_YouTube_Kids_as_a_kid(self):
        print("Test Name: Kid setting up their own account on YouTube Kids")
        #logic
        self.base_url = self.youtube_page.open_youtube_kids_through_menu_button()
        #infra
        self.driver = self.browser.get_driver(self.base_url)
        time.sleep(3)
        #logic
        self.youtube_page.setting_up_account_on_YouTube_Kids_as_a_kid()
        time.sleep(3)
        #test

    def test_setting_up_account_on_YouTube_Kids_as_a_parent_steps(self):
        print("Test Name: Parents setting up a kid account on YouTube Kids")
        self.base_url = self.youtube_page.open_youtube_kids_through_menu_button()
        #infra
        self.driver = self.browser.get_driver(self.base_url)
        time.sleep(3)
        #logic
        self.parent_button = self.driver.find_element(By.ID, "parent-button")
        self.parent_button.click()
        self.next_in_parent_button = self.driver.find_element(By.ID, "next-button")
        self.next_in_parent_button.click()
        self.age_input_parent = self.driver.find_element(By.XPATH, "//input[@id='onboarding-age-gate-digit-1']")
        self.age_input_parent.send_keys("1")
        self.age_input_parent = self.driver.find_element(By.XPATH, "//input[@id='onboarding-age-gate-digit-2']")
        self.age_input_parent.send_keys("9")
        self.age_input_parent = self.driver.find_element(By.XPATH, "//input[@id='onboarding-age-gate-digit-3']")
        self.age_input_parent.send_keys("9")
        self.age_input_parent = self.driver.find_element(By.XPATH, "//input[@id='onboarding-age-gate-digit-4']")
        self.age_input_parent.send_keys("0")
        self.submit = self.driver.find_element(By.XPATH, "//div/div[5]/button[@id='submit-button']")
        self.submit.click()
        time.sleep(3)
        self.last_step = self.driver.find_element(By.XPATH, "//button[@id='sign-in-info-next-button']")
        time.sleep(27)
        self.last_step.click()
        self.last_step = self.driver.find_element(By.XPATH, "//button[@id='skip-button']")
        self.last_step.click()
        time.sleep(2)
        self.last_step = self.driver.find_element(By.XPATH, "//div[2]/div/button[@id='next-button']")
        self.last_step.click()
        time.sleep(2)
        self.cards_kids = self.driver.find_element(By.XPATH, "//div[@id='content-cards']/ytk-kids-age-selection-card-renderer[2]")
        self.cards_kids.click()
        time.sleep(1)
        self.select_younger = self.driver.find_element(By.XPATH, "//button[@id='select-link']")
        self.select_younger.click()
        time.sleep(1)
        self.search_off_button = self.driver.find_element(By.XPATH, "//button[@id='search-off-button']")
        self.search_off_button.click()
        time.sleep(1)
        self.setup_done = self.driver.find_element(By.XPATH, "//button[@id='done-button']")
        self.setup_done.click()
        time.sleep(1)
        #test

    def test_mute_video_on_youtube_kids(self):
        print("Test Name: Mute video button kids account")
        self.base_url = self.youtube_page.open_youtube_kids_through_menu_button()
        #infra
        self.driver = self.browser.get_driver(self.base_url)
        time.sleep(3)
        #logic
        self.parent_button = self.driver.find_element(By.ID, "parent-button")
        self.parent_button.click()
        self.next_in_parent_button = self.driver.find_element(By.ID, "next-button")
        self.next_in_parent_button.click()
        self.age_input_parent = self.driver.find_element(By.XPATH, "//input[@id='onboarding-age-gate-digit-1']")
        self.age_input_parent.send_keys("1")
        self.age_input_parent = self.driver.find_element(By.XPATH, "//input[@id='onboarding-age-gate-digit-2']")
        self.age_input_parent.send_keys("9")
        self.age_input_parent = self.driver.find_element(By.XPATH, "//input[@id='onboarding-age-gate-digit-3']")
        self.age_input_parent.send_keys("9")
        self.age_input_parent = self.driver.find_element(By.XPATH, "//input[@id='onboarding-age-gate-digit-4']")
        self.age_input_parent.send_keys("0")
        self.submit = self.driver.find_element(By.XPATH, "//div/div[5]/button[@id='submit-button']")
        self.submit.click()
        time.sleep(3)
        self.last_step = self.driver.find_element(By.XPATH, "//button[@id='sign-in-info-next-button']")
        self.mute = self.driver.find_element(By.XPATH, "//tp-yt-paper-icon-button[@id='volume-button']")
        self.mute.click()
        time.sleep(27)
        #test

    def test_search_input_on_YouTube_Kids_without_search(self):
        print("Test Name: Search input on kids account that not include search input ")
        self.base_url = self.youtube_page.open_youtube_kids_through_menu_button()
        #infra
        self.driver = self.browser.get_driver(self.base_url)
        time.sleep(3)
        #logic
        self.parent_button = self.driver.find_element(By.ID, "parent-button")
        self.parent_button.click()
        self.next_in_parent_button = self.driver.find_element(By.ID, "next-button")
        self.next_in_parent_button.click()
        self.age_input_parent = self.driver.find_element(By.XPATH, "//input[@id='onboarding-age-gate-digit-1']")
        self.age_input_parent.send_keys("1")
        self.age_input_parent = self.driver.find_element(By.XPATH, "//input[@id='onboarding-age-gate-digit-2']")
        self.age_input_parent.send_keys("9")
        self.age_input_parent = self.driver.find_element(By.XPATH, "//input[@id='onboarding-age-gate-digit-3']")
        self.age_input_parent.send_keys("9")
        self.age_input_parent = self.driver.find_element(By.XPATH, "//input[@id='onboarding-age-gate-digit-4']")
        self.age_input_parent.send_keys("0")
        self.submit = self.driver.find_element(By.XPATH, "//div/div[5]/button[@id='submit-button']")
        self.submit.click()
        time.sleep(3)
        self.last_step = self.driver.find_element(By.XPATH, "//button[@id='sign-in-info-next-button']")
        self.mute = self.driver.find_element(By.XPATH, "//tp-yt-paper-icon-button[@id='volume-button']")
        self.mute.click()
        time.sleep(27)
        self.last_step.click()
        self.last_step = self.driver.find_element(By.XPATH, "//button[@id='skip-button']")
        self.last_step.click()
        time.sleep(2)
        self.last_step = self.driver.find_element(By.XPATH, "//div[2]/div/button[@id='next-button']")
        self.last_step.click()
        time.sleep(2)
        self.cards_kids = self.driver.find_element(By.XPATH, "//div[@id='content-cards']/ytk-kids-age-selection-card-renderer[2]")
        self.cards_kids.click()
        time.sleep(1)
        self.select_younger = self.driver.find_element(By.XPATH, "//button[@id='select-link']")
        self.select_younger.click()
        time.sleep(1)
        self.search_off_button = self.driver.find_element(By.XPATH, "//button[@id='search-off-button']")
        self.search_off_button.click()
        time.sleep(1)
        self.setup_done = self.driver.find_element(By.XPATH, "//button[@id='done-button']")
        self.setup_done.click()
        time.sleep(1)
        #test
        with self.assertRaises(ElementNotInteractableException) as context:
            self.search_button = self.driver.find_element(By.XPATH, "//input[@id='input']")
            self.search_button.click()

        exception = context.exception
        self.assertEqual("Your expected exception message", str(exception))
        self.assertIsNotNone(exception.screen)
        self.assertIsNotNone(exception.stacktrace)

    def test_play_video_on_youtube_kids(self):
        print("Test Name: Commence video playback on YouTube Kids.")
        self.base_url = self.youtube_page.open_youtube_kids_through_menu_button()
        #infra
        self.driver = self.browser.get_driver(self.base_url)
        time.sleep(3)
        #logic
        self.parent_button = self.driver.find_element(By.ID, "parent-button")
        self.parent_button.click()
        self.next_in_parent_button = self.driver.find_element(By.ID, "next-button")
        self.next_in_parent_button.click()
        self.age_input_parent = self.driver.find_element(By.XPATH, "//input[@id='onboarding-age-gate-digit-1']")
        self.age_input_parent.send_keys("1")
        self.age_input_parent = self.driver.find_element(By.XPATH, "//input[@id='onboarding-age-gate-digit-2']")
        self.age_input_parent.send_keys("9")
        self.age_input_parent = self.driver.find_element(By.XPATH, "//input[@id='onboarding-age-gate-digit-3']")
        self.age_input_parent.send_keys("9")
        self.age_input_parent = self.driver.find_element(By.XPATH, "//input[@id='onboarding-age-gate-digit-4']")
        self.age_input_parent.send_keys("0")
        self.submit = self.driver.find_element(By.XPATH, "//div/div[5]/button[@id='submit-button']")
        self.submit.click()
        time.sleep(3)
        self.last_step = self.driver.find_element(By.XPATH, "//button[@id='sign-in-info-next-button']")
        self.mute = self.driver.find_element(By.XPATH, "//tp-yt-paper-icon-button[@id='volume-button']")
        self.mute.click()
        time.sleep(27)
        self.last_step.click()
        self.last_step = self.driver.find_element(By.XPATH, "//button[@id='skip-button']")
        self.last_step.click()
        time.sleep(2)
        self.last_step = self.driver.find_element(By.XPATH, "//div[2]/div/button[@id='next-button']")
        self.last_step.click()
        time.sleep(2)
        self.cards_kids = self.driver.find_element(By.XPATH, "//div[@id='content-cards']/ytk-kids-age-selection-card-renderer[2]")
        self.cards_kids.click()
        time.sleep(1)
        self.select_younger = self.driver.find_element(By.XPATH, "//button[@id='select-link']")
        self.select_younger.click()
        time.sleep(1)
        self.search_off_button = self.driver.find_element(By.XPATH, "//button[@id='search-off-button']")
        self.search_off_button.click()
        time.sleep(1)
        self.setup_done = self.driver.find_element(By.XPATH, "//button[@id='done-button']")
        self.setup_done.click()
        time.sleep(1)
        self.play = self.driver.find_element(By.ID, "ytk-compact-video-renderer-NKc3lIN_yDQ")
        self.play.click()
        time.sleep(2)
        self.mute = self.driver.find_element(By.XPATH, "//tp-yt-paper-icon-button[@id='volume-button']")
        self.mute.click()
        time.sleep(10)
        #test
        