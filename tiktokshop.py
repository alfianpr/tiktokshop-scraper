from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import requests

SCROLL_LOOP = 10
CATEGORY = "Womenswear"
SWIPE = "yes" # yes or no
SWIPE_LOOP = 1
SESSION = 5
CONNECTION = "192.168.1.31:32869"

desired_caps = {
    "appium:appPackage": "com.ss.android.ugc.trill",
    "appium:appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    "platformName": "Android",
    "deviceName": "device",
    "udid": CONNECTION,
    "noReset": True,
    "unlockType": "pattern",
    "unlockValue": "751236"

}

appium_connect = {
    "platformName": "Android",
    "deviceName": "device",
    "udid": CONNECTION,
    "noReset": True
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", appium_connect)
def ses():
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    driver.implicitly_wait(4)
    #time.sleep(2)
    driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/ayo").click()
    #driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/azn").click()

########## Open the category

#def refresh():


def to_cat():
    time.sleep(3)
    i = 0
    if SWIPE == "yes":
        while i < SWIPE_LOOP:
            try:
                driver.swipe(953, 1512, 369, 1512, 400)
                i = i+1
            except:
                pass
    else:
        pass
    driver.implicitly_wait(3)
    try:
        driver.find_element(by=AppiumBy.XPATH, value=f'//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="{CATEGORY}"]').click()
    except:
        driver.swipe(953, 1730, 369, 1730, 400)
        driver.find_element(by=AppiumBy.XPATH, value=f'//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="{CATEGORY}"]').click()

########## Scroll up and down
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

j = 1
while j <= SESSION:
    ses()
    to_cat()
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
    j = j+1