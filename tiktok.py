from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import requests

SCROLL_LOOP = 100
CATEGORY = "Beauty"
SESSION = 5
CONNECTION = "RR8T704RCKK"

desired_caps = {
    "appium:appPackage": "com.ss.android.ugc.trill",
    "appium:appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    "platformName": "Android",
    "deviceName": "device",
    "udid": CONNECTION,
    "noReset": True
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

driver.implicitly_wait(4)
driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/ayo").click()

time.sleep(3)

### Scroll
deviceSize = driver.get_window_size()
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']
startx = screenWidth*1/4
endx = screenWidth*1/4
starty = screenHeight*8/11
endy = screenHeight/8

actions = TouchAction(driver)

actions.long_press(None,startx,screenHeight*8/9).move_to(None,endx,endy).release().perform()

### Looking for category
isfind = driver.find_elements(by=AppiumBy.XPATH, value=f'//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="{CATEGORY}"]')
try:    
    while len([l[0] for l in isfind if len(l) > 0]) == 0:
        driver.swipe(953, 300, 369, 300, 400)
        isfind.append(driver.find_elements(by=AppiumBy.XPATH, value=f'//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="{CATEGORY}"]'))
    else:
        time.sleep(2)
        [l[0] for l in isfind if len(l) > 0][0].click()
except:
    isfind[0].click()

def get_link():
    #driver.implicitly_wait(4)
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView").click()
    #driver.implicitly_wait(4)
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]").click()
    text = driver.get_clipboard_text()
    return text

def open_product():
    df = []
    xy = {279 : 600, 864 : 600, 268 : 1362, 786 : 1362, 264 : 2201, 823 : 2201}
    for i, j in xy.items():
        try:
            time.sleep(1)
            actions.tap(None,i,j,1)
            actions.perform()
            link = get_link()
            print("found link : ", link)
            df.append(link)
            driver.back()
        except:
            continue
    df = pd.DataFrame(df)
    df.to_csv(f'{CATEGORY}.csv', mode='a', index=False, header=False)

k = 0
while k <= SCROLL_LOOP:
    print (f"Scrape the loop at {k}")
    try:
        time.sleep(1)
        open_product()
    except:
        continue
    driver.swipe(startx, 2153, endx, 445)
    try :
        driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView").click()
    except:
        pass
    k = k + 1