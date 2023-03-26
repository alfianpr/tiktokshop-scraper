from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction

# Setup Component
SHARE_BUTTON = "com.ss.android.ugc.trill:id/hf0"
COPY_BUTTON = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]"
CLOSE_DIALOG = "com.ss.android.ugc.trill:id/f54"
UP_BUTTON = "com.ss.android.ugc.trill:id/c4f"

def driver(SERVER_APPIUM_IP, SERVER_APPIUM_PORT, desired_caps):
        global driver
        driver = webdriver.Remote(f"http://{SERVER_APPIUM_IP}:{SERVER_APPIUM_PORT}/wd/hub", desired_caps)
        return driver

def up_button_asuspromaxm1(): TouchAction(driver).tap(None, 985, 1904).perform() # coordinat of up button # Adjust with your device

def close_dialog(): 
    return driver.find_element(by=AppiumBy.ID, value=f"{CLOSE_DIALOG}").click() # close unnecesary dialogbox

def get_link_cat_asuspromaxm1():
    #driver.implicitly_wait(4)
    time.sleep(1)
    driver.find_element(by=AppiumBy.ID, value=f"{SHARE_BUTTON}").click()
    #driver.implicitly_wait(4)
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value=f"{COPY_BUTTON}").click()
    return driver.get_clipboard_text()

#Open Product by Coordinat
def open_product_v1_cat_asuspromaxm1(CATEGORY):
    actions = TouchAction(driver)
    df = []
    xy = {279 : 600, 864 : 600, 268 : 1350, 786 : 1350, # Click coordinat # Adjust with your device
        #264 : 1855, 823 : 1855
        }
    for i, j in xy.items():
        try: actions.tap(None,i,j).perform()
        except: continue
        try: close_dialog()
        except: pass
        try:
            link = get_link_cat_asuspromaxm1()
            print("found link : ", link)
            df.append(link)
            driver.back()
        except: pass
    df = pd.DataFrame(df)
    df.to_csv(f'./csv/{CATEGORY}.csv', mode='a', index=False, header=False)
