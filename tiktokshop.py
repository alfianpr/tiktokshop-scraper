from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import requests

LOOP = 2

desired_caps = {
    "appium:appPackage": "com.ss.android.ugc.trill",
    "appium:appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    "platformName": "Android",
    "deviceName": "device",
    #udid": "emulator-5554",
    #"udid": "192.168.8.121:37757",
    "udid": "RR8T704RCKK",
    "noReset": True
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(4)
el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/X.Uf6/android.widget.TabHost/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ImageView")
el1.click()

time.sleep(4)

#bypass layer
actions = TouchAction(driver)
actions.tap(None,164,514,1)
actions.perform()
time.sleep(3)
driver.back()

#scroll up

time.sleep(1)
el3 = driver.find_element(by=AppiumBy.XPATH, value='//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="Womenswear"]')
el3.click()

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
    time.sleep(1)
    el21 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]")
    el21.click()
    text = driver.get_clipboard_text()
    return text

df = []
def open_product():
    xy = {
        279 : 600,
        864 : 600,
        268 : 1362,
        786 : 1362,
        264 : 2201,
        823 : 2201
    }
    for i, j in xy.items():
        actions.tap(None,i,j,1)
        actions.perform()
        link = get_link()
        print("found link : ", link)
        df.append(link)
        driver.back()

try:
    i = 1
    while i <= LOOP:
        actions.long_press(None,startx,starty).move_to(None,endx,endy).release().perform()
        open_product()
        i = i+1
except:
    pass

result = []
session = requests.Session()  # so connections are recycled

url = []
for i in df:
    resp = session.head(i, allow_redirects=True)
    url.append(resp.url)

[result.append(x) for x in url if x not in result]
df_result = pd.DataFrame(result)
df_result.to_csv("test.csv")
print(df_result)