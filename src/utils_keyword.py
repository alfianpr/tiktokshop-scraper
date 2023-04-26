from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction

# Setup Connection
ASUSPROMAXM1 = "192.168.0.111:5555"

# Setup Component
SHARE_BUTTON_1 = "com.ss.android.ugc.trill:id/hog"
SHARE_BUTTON_2 = "com.ss.android.ugc.trill:id/hoh"
COPY_BUTTON = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]"
CLOSE_DIALOG = "com.ss.android.ugc.trill:id/f54"
CLOSE_END_LIVE = "com.ss.android.ugc.trill:id/bb_"
CLOSE_TOP_PRODUCT = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.lynx.tasm.behavior.ui.LynxFlattenUI[3]"
BACK_BUTTON = "com.ss.android.ugc.trill:id/a2f"
CLOSE_LIVE = "com.ss.android.ugc.trill:id/aw2"
CLOSE_INSIDE_PRODUCT = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.lynx.tasm.behavior.ui.LynxFlattenUI[10]"
CLOSE_COUNTRY_AVAIL ="com.ss.android.ugc.trill:id/aum"

# Setup coordinat
"""
Setup Coordinat for Asus Pro Max M1
Structure (start_x, start_y, end_x, end_y, speed)
"""
SELECT_PRODUCT = {279 : 760, 864 : 760, 268 : 1962, 786 : 1962}
SCROLL_DOWN = [500, 1900, 500, 700, 400]
SWIPE_PRODUCT = [540, 590, 540, 1850, 400]

SC_1 = SWIPE_PRODUCT

def driver(SERVER_APPIUM_IP, SERVER_APPIUM_PORT, desired_caps):
        global driver
        driver = webdriver.Remote(f"http://{SERVER_APPIUM_IP}:{SERVER_APPIUM_PORT}/wd/hub", desired_caps)
        return driver

def close_dialog(): return driver.find_element(by=AppiumBy.ID, value=f"{CLOSE_DIALOG}").click() # close unnecesary dialogbox

def get_link_search_asuspromaxm1():
    #driver.implicitly_wait(4)
    time.sleep(1)
    try:
        driver.find_element(by=AppiumBy.ID, value=f"{SHARE_BUTTON_1}").click()
    except:
        driver.find_element(by=AppiumBy.ID, value=f"{SHARE_BUTTON_2}").click()
    #driver.implicitly_wait(4)
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value=f"{COPY_BUTTON}").click()
    return driver.get_clipboard_text()

# Open Product by Coordinat
def open_product_v1_search_asuspromaxm1(CATEGORY):
    actions = TouchAction(driver)
    df = []
    for i, j in SELECT_PRODUCT.items():
        try: time.sleep(2); actions.tap(None,i,j).perform()
        except: print("cant open the product"); continue
        try: close_dialog()
        except: pass
        try:
            link = get_link_search_asuspromaxm1()
            print("found link : ", link) 
            df.append(link)
            driver.swipe(SC_1[0], SC_1[1], SC_1[2], SC_1[3], SC_1[4]) # swipe live product video
            time.sleep(1); driver.back(); continue
        except: pass
        # try: driver.find_element(by=AppiumBy.ID, value=f"{BACK_BUTTON}").click()
        # except: pass
        try: time.sleep(1); driver.find_element(by=AppiumBy.ID, value=f"{CLOSE_END_LIVE}").click(); print("cant share link 1"); continue
        except: print ("can't close end live"); pass
        try: time.sleep(1); driver.find_element(by=AppiumBy.XPATH, value=f"{CLOSE_TOP_PRODUCT}").click(); print("cant share link 2"); continue
        except: pass
        # try: time.sleep(2); driver.find_element(by=AppiumBy.ID, value=f"CLOSE_COUNTRY_AVAIL").click; continue
        # except: print("huft.. :("); pass
    df = pd.DataFrame(df)
    df.to_csv(f'./url/{CATEGORY}.csv', mode='a', index=False, header=False)

# Open Product by "Sold Text"
def open_product_v2_search_asuspromaxm1(CATEGORY, SKIP, k):
    actions = TouchAction(driver)
    element = driver.find_elements(by=AppiumBy.XPATH, value="//*[contains(@text,'sold')]")
    el = element[1::2]
    if k > 0 or SKIP == True: del el[:2]
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
            driver.swipe(SC_1[0], SC_1[1], SC_1[2], SC_1[3], SC_1[4]) # swipe live product video
            time.sleep(1); driver.back(); continue
        except: pass
        try: time.sleep(1); driver.find_element(by=AppiumBy.ID, value=f"{CLOSE_END_LIVE}").click(); continue
        except: pass
        try: time.sleep(2); driver.find_element(by=AppiumBy.ID, value=f"{CLOSE_LIVE}").click(); continue
        except: pass
        try: driver.find_element(by=AppiumBy.XPATH, value=f"{CLOSE_INSIDE_PRODUCT}").click(); continue
        except: pass
    df = pd.DataFrame(df)
    df.to_csv(f'./url/{CATEGORY}.csv', mode='a', index=False, header=False)