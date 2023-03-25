from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction

SCROLL_LOOP = 100
CATEGORY = "Somethinc"
CONNECTION = "192.168.45.165:39090"
SKIP = True  # First time set to False, set True if you want to continue the process

desired_caps = {
    "platformName": "Android",
    "deviceName": "device",
    "udid": CONNECTION,
    "noReset": True,
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

### Scroll Default
actions = TouchAction(driver)
startx = driver.get_window_size()['width']*1/4; endx = driver.get_window_size()['width']*1/4
starty = driver.get_window_size()['height']*8/11; endy = driver.get_window_size()['height']/8

def get_link():
    #driver.implicitly_wait(4)
    time.sleep(2)
    driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/hf0").click()
    #driver.implicitly_wait(4)
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]").click()
    return driver.get_clipboard_text()

# Open Product by Coordinat
def open_product_v1():
    df = []
    xy = {279 : 760, 864 : 760, 268 : 1962, 786 : 1962, 
        #264 : 1855, 823 : 1855
        }
    for i, j in xy.items():
        try:
            actions.tap(None,i,j,1)
            actions.perform()
            time.sleep(2)
            link = get_link()
            print("found link : ", link)
            df.append(link)
            time.sleep(1)
            driver.swipe(540, 590, 540, 1850, 400)
        except: pass
        driver.back()
        try: driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/b93").click()
        except: pass
    df = pd.DataFrame(df)
    df.to_csv(f'{CATEGORY}.csv', mode='a', index=False, header=False)

# Open Product by "Sold Text"
def open_product_v2():
    element = driver.find_elements(by=AppiumBy.XPATH, value="//*[contains(@text,'sold')]")
    el = element[1::2]
    if k > 0 or SKIP == True: del el[:2]
    loc = [i.location for i in el]
    print("list :", loc)

    df = []
    for i in loc:
        try: actions.tap(None, i["x"], i["y"]).perform()
        except: pass
        try:
            link = get_link()
            print("found link : ", link)
            df.append(link)
            time.sleep(1)
            driver.swipe(540, 590, 540, 1850, 400)
            time.sleep(1)
        except: pass
        driver.back()
    df = pd.DataFrame(df)
    df.to_csv(f'{CATEGORY}.csv', mode='a', index=False, header=False)

k = 0
while k <= SCROLL_LOOP:
    print (f"Scrape the loop at {k}")
    time.sleep(1)
    open_product_v2()
    driver.swipe(startx, 1900, endx, 850, 400)
    time.sleep(1)
    try: driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/f54").click()
    except: pass
    k = k + 1