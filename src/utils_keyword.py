from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction

# Setup Component
SHARE_BUTTON = "com.ss.android.ugc.trill:id/hf0"
COPY_BUTTON = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]"
CLOSE_DIALOG = "com.ss.android.ugc.trill:id/f54"
CLOSE_END_LIVE = "com.ss.android.ugc.trill:id/auy"
CLOSE_TOP_PRODUCT = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.lynx.tasm.behavior.ui.LynxFlattenUI[3]"
BACK_BUTTON = "com.ss.android.ugc.trill:id/a20"
CLOSE_LIVE = "com.ss.android.ugc.trill:id/auy"

def driver(SERVER_APPIUM_IP, SERVER_APPIUM_PORT, desired_caps):
        global driver
        driver = webdriver.Remote(f"http://{SERVER_APPIUM_IP}:{SERVER_APPIUM_PORT}/wd/hub", desired_caps)
        return driver

def close_dialog(): return driver.find_element(by=AppiumBy.ID, value=f"{CLOSE_DIALOG}").click() # close unnecesary dialogbox

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
        try: time.sleep(2); actions.tap(None,i,j).perform()
        except: print("cant open the product"); continue
        try: close_dialog()
        except: pass
        try:
            link = get_link_search_asuspromaxm1()
            print("found link : ", link)
            df.append(link)
            driver.swipe(540, 590, 540, 1850, 400) # swipe live product video
            driver.back(); continue
        except: pass
        # try: driver.find_element(by=AppiumBy.ID, value=f"{BACK_BUTTON}").click()
        # except: pass
        try: # Close end live
            time.sleep(1); driver.find_element(by=AppiumBy.ID, value=f"{CLOSE_END_LIVE}").click()
            print("cant share link 1")
        except: print ("can't close end live"); pass
        try: # Close top prodct
            time.sleep(1); driver.find_element(by=AppiumBy.XPATH, value=f"{CLOSE_TOP_PRODUCT}").click()
            print("cant share link 2")
        except: pass
    df = pd.DataFrame(df)
    df.to_csv(f'./url/{CATEGORY}.csv', mode='a', index=False, header=False)

# Open Product by "Sold Text"
def open_product_v2_search_asuspromaxm1(CATEGORY, SKIP, k):
    actions = TouchAction(driver)
    element = driver.find_elements(by=AppiumBy.XPATH, value="//*[contains(@text,'sold')]")
    el = element[1::2]
    if k > 0 or SKIP == True: del el[:1]
    loc = [i.location for i in el]
    print("list :", loc)

    df = []
    for i in loc:
        try: actions.tap(None, i["x"], i["y"]).perform()
        except: continue
        try: close_dialog()
        except: pass
        try:
            time.sleep(1)
            link = get_link_search_asuspromaxm1()
            print("found link : ", link)
            df.append(link)
            driver.swipe(540, 590, 540, 1850, 400) # swipe live product video
            time.sleep(1)
            driver.back(); continue
        except: pass
        try: # Close end live
            time.sleep(1); driver.find_element(by=AppiumBy.ID, value=f"{CLOSE_END_LIVE}").click()
            print("cant share link 1")
        except: pass
        try: time.sleep(2); driver.find_element(by=AppiumBy.ID, value=f"{CLOSE_LIVE}").click()
        except: pass
    df = pd.DataFrame(df)
    df.to_csv(f'./url/{CATEGORY}.csv', mode='a', index=False, header=False)