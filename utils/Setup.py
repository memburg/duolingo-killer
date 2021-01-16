from selenium import webdriver


class Setup:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(20)

    def get_driver(self):
        return self.driver
