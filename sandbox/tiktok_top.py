from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction
import requests
# from appium.webdriver.appium_service import AppiumService

# service = AppiumService()
SCROLL_LOOP = 100
CATEGORY = "Rumah Tangga"
CONNECTION = "192.168.0.111:39170"
LAYER = False

desired_caps = {
    "appium:appPackage": "com.ss.android.ugc.trill",
    "appium:appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    "platformName": "Android",
    "deviceName": "device",
    "udid": CONNECTION,
    "noReset": True,
    # "unlockType": "pattern",
    # "unlockValue": "751236"
}

# service.start(args=['–address', 'localhost', '-p', '4723'])
# print(service.is_running)
# print(service.is_listening)
#service.stop()
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
actions = TouchAction(driver)


#time.sleep(3)
driver.implicitly_wait(4)
driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/b05").click()
#driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/azn").click()
time.sleep(3)

### Scroll
deviceSize = driver.get_window_size()
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']
startx = screenWidth*1/4
endx = screenWidth*1/4
starty = screenHeight*8/11
endy = screenHeight/8

if LAYER == True:
    layer = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup")
    layer.click()
    time.sleep(2)
    driver.back()

time.sleep(2)
el6 = driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/d63")
el6.click()
time.sleep(1)
el7 = driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/bxk")
el7.send_keys(f"{CATEGORY}")
time.sleep(2)
el8 = driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/j1c")
el8.click()
time.sleep(2)
el9 = driver.find_element(by=AppiumBy.XPATH, value="//com.lynx.tasm.behavior.ui.text.UIText[@content-desc=\"Top sales\"]")
el9.click()

def get_link():
    #driver.implicitly_wait(4)
    time.sleep(2)
    driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/h3b").click()
    #driver.implicitly_wait(4)
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]").click()
    text = driver.get_clipboard_text()
    return text

def open_product():
    df = []
    xy = {279 : 760, 864 : 760, 268 : 1962, 786 : 1962, 
        #264 : 1855, 823 : 1855
        }
    for i, j in xy.items():
        try:
            time.sleep(1)
            actions.tap(None,i,j,1)
            actions.perform()
            time.sleep(2)
            link = get_link()
            print("found link : ", link)
            df.append(link)
            time.sleep(1)
            driver.swipe(540, 590, 540, 1800, 400)
            time.sleep(1)
            # if close.is_displayed() == True:
            #     close.click()
            # else:
            #     driver.back()
            # close_1 = driver.find_element(by=AppiumBy.ID, value="com.ss.android.ugc.trill:id/b8u")
            # close_1.click()
            time.sleep(1)
            driver.back()
        except:
            continue
    df = pd.DataFrame(df)
    df.to_csv(f'{CATEGORY}.csv', mode='a', index=False, header=False)

k = 0
while k <= SCROLL_LOOP:
    print (f"Scrape the loop at {k}")
    try:
        time.sleep(2)
        open_product()
    except:
        pass
    driver.swipe(startx, 1855, endx, 1000, 400)

    time.sleep(2)
    close = driver.find_elements(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView")
    if len(close) > 0:
        close[0].click()
    k = k + 1