from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains# time.sleep(3)
# el3 = driver.find_element(by=AppiumBy.XPATH, value='//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="Womenswear"]')
# el3.click()

from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

desired_caps = {
    "appium:appPackage": "com.ss.android.ugc.trill",
    "appium:appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    "platformName": "Android",
    "deviceName": "device",
    #udid": "emulator-5554",
    #"udid": "192.168.8.121:37757",
    "udid": "RR8T704RCKK",
    "noReset": True
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(4)
el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/X.VSu/android.widget.TabHost/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ImageView")
el1.click()

time.sleep(4)

#bypass layer
actions = TouchAction(driver)
actions.tap(None,971,1901,1)
actions.perform()
time.sleep(2)
driver.back()

# try:
#     actions = TouchAction(driver)
#     actions.tap(None,971,1901,1)
#     actions.perform()
#     time.sleep(2)
#     driver.back()
# except:
#      pass
time.sleep(1)
el3 = driver.find_element(by=AppiumBy.XPATH, value='//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="Womenswear"]')
el3.click()

