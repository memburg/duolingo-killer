import json
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    URL = 'https://www.duolingo.com'
    GET_STARTED = '//a[@data-test="get-started-top"]'
    SPANISH_CARD = '//a[contains(@data-test, "language-es")]'
    FAMILY_CARD = '//label[contains(@data-test, "family")]'
    CONTINUE_BUTTON = '//button[contains(text(), "Continue")]'
    INTENSE_OPTION = '//span[contains(text(), "Intense")]'
    CREATE_PROFILE_BUTTON = '//button[contains(text(), "Create a profile")]'
    NAME_INPUT = '//input[@autocomplete="name"]'
    EMAIL_INPUT = '//input[@autocomplete="email"]'
    AGE_INPUT = '//input[@data-test="age-input"]'
    PASSWORD_INPUT = '//input[@data-test="password-input"]'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def navigate_to_this_page(self):
        self.driver.get(self.URL)

    def click_get_started_button(self):
        el = self.driver.find_element_by_xpath(self.GET_STARTED)
        self.wait.until(EC.visibility_of(el))
        el.click()

    def click_spanish_card(self):
        el = self.driver.find_element_by_xpath(self.SPANISH_CARD)
        self.wait.until(EC.visibility_of(el))
        el.click()

    def click_family_card(self):
        el = self.driver.find_element_by_xpath(self.FAMILY_CARD)
        self.wait.until(EC.visibility_of(el))
        el.click()

    def click_continue_button(self):
        el = self.driver.find_element_by_xpath(self.CONTINUE_BUTTON)
        self.wait.until(EC.visibility_of(el))
        el.click()

    def click_intense_option(self):
        el = self.driver.find_element_by_xpath(self.INTENSE_OPTION)
        self.wait.until(EC.visibility_of(el))
        el.click()

    def click_create_profile_button(self):
        el = self.driver.find_element_by_xpath(self.CREATE_PROFILE_BUTTON)
        self.wait.until(EC.visibility_of(el))
        el.click()

    def fill_create_profile_form(self):
        f = open('data/user.json')
        data = json.load(f)
        f.close()

        age = random.randint(18, 120)
        name = random.choice(data['firstname'])
        surename = random.choice(data['surename'])
        email = f'{name}.{surename}@duolingo.com'.lower()
        password = 'teipon123..'

        age_input = self.driver.find_element_by_xpath(self.AGE_INPUT)
        name_input = self.driver.find_element_by_xpath(self.NAME_INPUT)
        email_input = self.driver.find_element_by_xpath(self.EMAIL_INPUT)
        password_input = self.driver.find_element_by_xpath(self.PASSWORD_INPUT)

        self.wait.until(EC.visibility_of(name_input))

        age_input.send_keys(age)
        name_input.send_keys(f'{name} {surename}')
        email_input.send_keys(email)
        password_input.send_keys(password)
