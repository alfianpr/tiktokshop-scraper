from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction

SCROLL_LOOP = 100
CATEGORY = "Skintific"
CONNECTION = "192.168.45.165:5555"
LAYER = False

desired_caps = {
    # "appium:appPackage": "com.ss.android.ugc.trill",
    # "appium:appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    "platformName": "Android",
    "deviceName": "device",
    "udid": CONNECTION,
    "noReset": True,
    # "unlockType": "pattern",
    # "unlockValue": "751236"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
actions = TouchAction(driver)

element = driver.find_elements(by=AppiumBy.XPATH, value="//*[contains(@text,'sold')]")
teks = []
el = []

print(element)

for i in element:
    try:
        teks.append(i.text.replace("|", ""))
    except:
        pass

[el.append(x) for x in teks if x not in el]

print (teks)
print (el)