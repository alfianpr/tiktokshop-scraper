from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction
from utils_category import open_product_v1_cat_asuspromaxm1, driver, close_dialog

# Setup Connection and product
SESSION = 100
SCROLL_LOOP = 100
CATEGORY = "Whitelab"
CONNECTION = "192.168.0.100:38763"
SERVER_APPIUM_PORT = "4723"
SERVER_APPIUM_IP = "127.0.0.1"

DESIRED_CAPS = {
    "platformName": "Android",
    "deviceName": "device",
    "udid": CONNECTION,
    "noReset": True,
}

driver = driver(SERVER_APPIUM_IP=SERVER_APPIUM_IP, SERVER_APPIUM_PORT=SERVER_APPIUM_PORT, desired_caps=DESIRED_CAPS)

### Scroll
startx = driver.get_window_size()['width']*1/4; endx = driver.get_window_size()['width']*1/4
starty = driver.get_window_size()['height']*8/11; endy = driver.get_window_size()['height']/8
actions = TouchAction(driver)

A = 0
while A <= SESSION:
    k = 0
    while k <= SCROLL_LOOP:
        print (f"Scrape the loop at {k}")
        try:
            time.sleep(2)
            open_product()
        except:
            pass
        driver.swipe(startx, 1855, endx, 445, 400)

        time.sleep(2)
        k = k + 1
    try:
        driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/X.blv/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout").click()
    except:
        pass
    time.sleep(3)
    driver.swipe(500, 465, 500, 948, 400)
    # time.sleep(3)
    driver.swipe(startx, 1855, endx, 400, 400)
    try:
        driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/f54").click()
    except:
        pass
    A = A + 1