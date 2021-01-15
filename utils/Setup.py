# ==================================================================
# PLEASE DO NOT ATTEMPT TO SIMPLIFY THIS CODE.
# KEEP THE SPACE SHUTTLE FLYING.
# ==================================================================
#
# This module is intentionally written in a very verbose style. You will
# notice:
#
# 1. Every 'if' statement has a matching 'else'
# 2. Things that may seem obvious are commented explicitly
#
# We call this style 'space shuttle style'. Space shuttle style is meant to
# ensure that every branch and condition is considered and accounted for -
# the same way code is written at NASA for applications like the space
# shuttle.
#
# ==================================================================
# PLEASE DO NOT ATTEMPT TO SIMPLIFY THIS CODE.
# KEEP THE SPACE SHUTTLE FLYING.
# ==================================================================

from selenium import webdriver


class Setup:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.fullscreen_window()

    def get_driver(self):
        return self.driver
