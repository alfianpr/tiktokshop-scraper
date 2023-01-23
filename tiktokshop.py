from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import requests

SCROLL_LOOP = 100
CATEGORY = "Womenswear"
SWIPE = "yes" # yes or no
SWIPE_LOOP = 1

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

time.sleep(2)
el1 = driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/ayo")
el1.click()
time.sleep(2)

i = 0
if SWIPE == "yes":
    while i < SWIPE_LOOP:
        driver.swipe(953, 1512, 369, 1512, 400)
        i = i+1
else:
    pass

#scroll up
time.sleep(1)
el3 = driver.find_element(by=AppiumBy.XPATH, value=f'//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="{CATEGORY}"]')
el3.click()
deviceSize = driver.get_window_size()
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']
startx = screenWidth/2
endx = screenWidth/2
starty = screenHeight*8/9
endy = screenHeight/8

actions = TouchAction(driver)

def get_link():
    time.sleep(2)
    el11 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView")
    el11.click()
    time.sleep(2)
    el21 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]")
    el21.click()
    text = driver.get_clipboard_text()
    return text

def open_product():
    df = []
    xy = {
        279 : 600,
        864 : 600,
        268 : 1362,
        786 : 1362,
        264 : 2201,
        823 : 2201
    }
    for i, j in xy.items():
        try:
            actions.tap(None,i,j,1)
            actions.perform()
            link = get_link()
            print("found link : ", link)
            df.append(link)
            driver.back()
        except:
            continue
    df = pd.DataFrame(df)
    df.to_csv('womenswear.csv', mode='a', index=False, header=False)

i = 1
while i <= SCROLL_LOOP:
    print (f"Scrape the loop at {i}")
    actions.long_press(None,startx,starty).move_to(None,endx,endy).release().perform()
    try:
        time.sleep(1)
        open_product()
    except:
        continue
    i = i+1