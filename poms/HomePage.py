from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    URL = 'https://www.duolingo.com'
    GET_STARTED = '//a[@data-test="get-started-top"]'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    def navigate_to_this_page(self):
        self.driver.get(self.URL)

    def click_get_started_button(self):
        el = self.driver.find_element_by_xpath(self.GET_STARTED)
        self.wait.until(EC.visibility_of(el))
        el.click()
