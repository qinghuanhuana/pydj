# coidng=utf-8
import time
from uiautomator import Device
from appium import webdriver
import os
from threading import Thread
d = Device("")
print(d.info)
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
appPath = os.path.join(path, "apk", "lxyd.apk")

desired_caps={
            'platformName': 'Android',
            'deviceName': 'X2P5T16114009484',
            'platformVersion': '5.1',
            'app': appPath,
            'noreset': True,
            'appPackage': 'gz.lifesense.weidong.qa',
            'appActivity': 'gz.lifesense.weidong.ui.activity.main.LaunchActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
