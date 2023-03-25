from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction

# Setup Component
SHARE_BUTTON = "com.ss.android.ugc.trill:id/hf0"
COPY_BUTTON = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]"
CLOSE_DIALOG = "com.ss.android.ugc.trill:id/f54"

def driver(SERVER_APPIUM_IP, SERVER_APPIUM_PORT, desired_caps):
        global driver
        driver = webdriver.Remote(f"http://{SERVER_APPIUM_IP}:{SERVER_APPIUM_PORT}/wd/hub", desired_caps)
        return driver

def close_dialog(): driver.find_element(by=AppiumBy.ID, value=f"{CLOSE_DIALOG}").click() # close unnecesary dialogbox

def get_link_search_asuspromaxm1():
    #driver.implicitly_wait(4)
    time.sleep(1)
    driver.find_element(by=AppiumBy.ID, value=f"{SHARE_BUTTON}").click()
    #driver.implicitly_wait(4)
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value=f"{COPY_BUTTON}").click()
    return driver.get_clipboard_text()

# Open Product by Coordinat
def open_product_v1_search_asuspromaxm1(CATEGORY):
    actions = TouchAction(driver)
    df = []
    xy = {279 : 760, 864 : 760, 268 : 1962, 786 : 1962, # Click coordinat
        #264 : 1855, 823 : 1855
        }
    for i, j in xy.items():
        try: actions.tap(None,i,j).perform()
        except: pass
        try: close_dialog()
        except: pass
        try:
            link = get_link_search_asuspromaxm1()
            print("found link : ", link)
            df.append(link)
        except: pass
        try:
            driver.swipe(540, 590, 540, 1850, 400) # swipe live product video
            driver.back()
        except: pass
    df = pd.DataFrame(df)
    df.to_csv(f'./csv/{CATEGORY}.csv', mode='a', index=False, header=False)

# Open Product by "Sold Text"
def open_product_v2_search_asuspromaxm1(SKIP, CATEGORY, k):
    actions = TouchAction(driver)
    element = driver.find_elements(by=AppiumBy.XPATH, value="//*[contains(@text,'sold')]")
    el = element[1::2]
    if k > 0 or SKIP == True: del el[:2]
    loc = [i.location for i in el]
    print("list :", loc)

    df = []
    for i in loc:
        try: actions.tap(None, i["x"], i["y"]).perform()
        except: pass
        try: close_dialog()
        except: pass
        try:
            link = get_link_search_asuspromaxm1()
            print("found link : ", link)
            df.append(link)
        except: pass
        try:
            time.sleep(1)
            driver.swipe(540, 590, 540, 1850, 400) # swipe live product video
            time.sleep(1)
            driver.back()
        except: pass
    df = pd.DataFrame(df)
    df.to_csv(f'./csv/{CATEGORY}.csv', mode='a', index=False, header=False)