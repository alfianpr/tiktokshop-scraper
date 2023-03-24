
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction
import requests

CATEGORY = "Baby"

desired_caps = {
    # "appium:appPackage": "com.ss.android.ugc.trill",
    # "appium:appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    "platformName": "Android",
    "deviceName": "device",
    "udid": "J9AXGF00S840NWB",
    "noReset": True,
    # "unlockType": "pattern",
    # "unlockValue": "751236"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
actions = TouchAction(driver)

isfind = driver.find_elements(by=AppiumBy.XPATH, value=f'//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="{CATEGORY}"]')

while not isfind:
    driver.swipe(954, 230, 369, 230)
    try:
        isfind.append(driver.find_element(by=AppiumBy.XPATH, value=f'//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="{CATEGORY}"]'))
    except:
        pass
else:
    isfind[0].click()
# try:
#     time.sleep(2)
#     while len([l[0] for l in isfind if len(l) > 0]) == 0:
#         driver.swipe(954, 230, 369, 230, 400)
#         time.sleep(1)
#         try:
#             isfind.append(driver.find_element(by=AppiumBy.XPATH, value=f'//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="{CATEGORY}]'))
#         except:
#             isfind.append(0)
#     else:
#         time.sleep(2)
#         [l[0] for l in isfind if len(l) > 0][0].click()
# except:
#         isfind[0].click()

# #print([l[0] for l in isfind if len(l) > 0])