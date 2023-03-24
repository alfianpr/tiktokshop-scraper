from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction

SCROLL_LOOP = 100
CATEGORY = "Whitelab"
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

### Scroll
deviceSize = driver.get_window_size()
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']
startx = screenWidth*1/4
endx = screenWidth*1/4
starty = screenHeight*8/11
endy = screenHeight/8
# com.ss.android.ugc.trill:id/iea
def get_link():
    #driver.implicitly_wait(4)
    time.sleep(2)
    driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/hf0").click()
    #driver.implicitly_wait(4)
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]").click()
    return driver.get_clipboard_text()

def open_product_v1():
    df = []
    xy = {279 : 760, 864 : 760, 268 : 1962, 786 : 1962, 
        #264 : 1855, 823 : 1855
        }
    for i, j in xy.items():
        try:
            #time.sleep(1)
            actions.tap(None,i,j,1)
            actions.perform()
            time.sleep(2)
            link = get_link()
            print("found link : ", link)
            df.append(link)
            time.sleep(1)
            driver.swipe(540, 590, 540, 1850, 400)
            # time.sleep(1)
        except:
            pass
        driver.back()
        try:
            driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/b93").click()
        except:
            pass
        
    df = pd.DataFrame(df)
    df.to_csv(f'{CATEGORY}.csv', mode='a', index=False, header=False)

def open_product_v2():
    element = driver.find_elements(by=AppiumBy.XPATH, value="//*[contains(@text,'sold')]")
    teks = []
#   el = []

    # for i in element:
    #     try:
    #         teks.append(i.text.replace("|", ""))
    #     except:
    #         pass

    # [el.append(x) for x in teks if x not in el]
    el = element[1::2]

    # if k > 0:
    del el[:2]

    print("list :", el)
    df = []
    for i in el:
        try:
            time.sleep(1)
            driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.lynx.tasm.behavior.ui.LynxFlattenUI[13]").click()
        except:
            pass
        # try:
        #     driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Shop").click()
        # except:
        #     pass
        
        # driver.find_element(by=AppiumBy.XPATH, value=f"//*[contains(@text,'{i}')]").click()
        i.click()
        try:
            #time.sleep(2)
            link = get_link()
            print("found link : ", link)
            df.append(link)
            time.sleep(1)
            driver.swipe(540, 590, 540, 1850, 400)
            time.sleep(1)
        except:
            pass
        driver.back()
        # try:
        #     driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/b93").click()
        # except:
        #     pass

    #time.sleep(2)
    df = pd.DataFrame(df)
    df.to_csv(f'{CATEGORY}.csv', mode='a', index=False, header=False)

k = 0
while k <= SCROLL_LOOP:
    print (f"Scrape the loop at {k}")
    time.sleep(1)
    open_product_v2()
    driver.swipe(startx, 1900, endx, 850, 400)
    time.sleep(1)
    k = k + 1