from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

CONNECTION = "192.168.45.165:39090"
SKIP = False
k = 0

desired_caps = {
    "platformName": "Android",
    "deviceName": "device",
    "udid": CONNECTION,
    "noReset": True,
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/hf0").click()

# element = driver.find_elements(by=AppiumBy.XPATH, value="//*[contains(@text,'sold')]")
# el = element[1::2]

# if k > 0 or SKIP == True:
#     del el[:2]

# # loc = []
# # for i in el:
# #     loc.append(i.location)

# loc = [i.location for i in el]



# print("list :", loc)