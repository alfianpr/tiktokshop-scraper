from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

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
endy = screenHeight/10

actions = TouchAction(driver)

def get_link():
    time.sleep(4)
    el11 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView")
    el11.click()
    time.sleep(3)
    el21 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]")
    el21.click()
    text = driver.get_clipboard_text()
    print (text)
    return text

df = []
def first_click():
    first = {
        279 : 600,
        864 : 600,
    }
    for i, j in first:
        actions.tap(None,i,j,1)
        actions.perform()
        get_link()
        df.append(get_link())
        driver.back()

def second_click():
    second = {
        268 : 1362,
        786 : 1362,
        264 : 2201,
        823 : 2201
    }
    for i, j in second:
        actions.tap(None,i,j,1)
        actions.perform()
        get_link()
        df.append(get_link())
        driver.back()


i = 1
while i <= LOOP:
    if i < 1:
        actions.long_press(None,startx,starty).move_to(None,endx,endy).release().perform()
        first_click()
        second_click()
    else:
        actions.long_press(None,startx,starty).move_to(None,endx,endy).release().perform()
        second_click()
    i = i+1

