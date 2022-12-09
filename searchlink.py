from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {
    "platformName": "Android",
    "deviceName": "device",
    #udid": "emulator-5554",
    "udid": "192.168.8.121:37757",
    "noReset": True
}