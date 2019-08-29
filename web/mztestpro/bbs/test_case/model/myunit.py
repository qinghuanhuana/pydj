from selenium import webdriver
from .driver import browser
import unittest
import os


class MyTest(unittest.TestCase):
    def setUp(self):
        self.dr = browser()
        self.dr.implicitly_wait(10)
        self.dr.maximize_window()

    def tearDown(self):
        self.dr.quit()
