from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import requests

SCROLL_LOOP = 1
CATEGORY = "Fashion Anak"
SESSION = 100
CONNECTION = "192.168.45.165:39090"
LAYER = True

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

#time.sleep(3)
# driver.implicitly_wait(4)
# driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/X.JtW/android.widget.TabHost/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.TextView").click()
#driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/azn").click()
time.sleep(3)

### Scroll
deviceSize = driver.get_window_size()
startx = deviceSize['width']*1/4
endx = deviceSize['width']*1/4
starty = deviceSize['height']*8/11
endy = deviceSize['height']/8

# if LAYER == True:
#     time.sleep(2)
#     layer = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup")
#     layer.click()
#     time.sleep(3)
#     driver.back()

actions = TouchAction(driver)
# driver.swipe(startx, 1855, endx, 445)

# try:
#     driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[5]").click()
# except:
#     pass
#actions.long_press(None,startx,screenHeight*8/9).move_to(None,endx,endy).release().perform()

### Looking for category
# isfind = driver.find_elements(by=AppiumBy.XPATH, value=f'//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="{CATEGORY}"]')
# while not isfind:
#     driver.swipe(954, 230, 369, 230)
#     try:
#         isfind.append(driver.find_element(by=AppiumBy.XPATH, value=f'//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="{CATEGORY}"]'))
#     except:
#         pass
# else:
#     isfind[0].click()

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
    xy = {279 : 600, 864 : 600, 268 : 1362, 786 : 1362, 
        #264 : 1855, 823 : 1855
        }
    for i, j in xy.items():
        try:
            time.sleep(1)
            actions.tap(None,i,j,1)
            actions.perform()
            link = get_link()
            print("found link : ", link)
            df.append(link)
            time.sleep(1)
            driver.back()
        except:
            continue
    df = pd.DataFrame(df)
    df.to_csv(f'csv/{CATEGORY}.csv', mode='a', index=False, header=False)

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