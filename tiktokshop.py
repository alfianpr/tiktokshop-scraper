from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC

START_RANGE = 500
END_RANGE = 700
DELAY = 3

df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vR80_iHyMEDo4pgue9N7toAAtjFIaaA9bYAgg_QtRprTxl-a2aehbHbDE387irsoRV6TKljiI_Yv26v/pub?gid=0&single=true&output=csv")
df_link = df["productUrl"].iloc[START_RANGE:END_RANGE].reset_index(drop=True)
df_id = df["itemid"].iloc[START_RANGE:END_RANGE].reset_index(drop=True)
df_cat = df["category"].iloc[START_RANGE:END_RANGE].reset_index(drop=True)

desired_caps = {
    "platformName": "Android",
    "deviceName": "device",
    #udid": "emulator-5554",
    "udid": "192.168.8.121:37757",
    "noReset": True
}

sale_xpath = ["/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView[3]",
              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView[3]",
              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[5]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView[3]",
              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[6]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView[3]"]

name_xpath =["/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView",
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView",
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView"]

def sale_scrap():
    for a in sale_xpath:
        try:
            sale = driver.find_element(by=AppiumBy.XPATH, value=a)
            return sale.text
        except:
            pass

def name_scrap():
    for b in name_xpath:
        try:
            name = driver.find_element(by=AppiumBy.XPATH, value=b)
            return name.text
        except:
            pass

name_df = []
sale_df = []
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
for _, i in df_link.items():
    print("opening lazada")
    driver.execute_script("mobile: deepLink", {'url': 'https://{}'.format(i), 'package': 'com.lazada.android'})
    time.sleep(DELAY)
    #scape name  
    name_df.append(name_scrap())
    print (name_scrap())
    #scrape sale
    sale_df.append(sale_scrap())
    print (sale_scrap())

df_name = pd.DataFrame(name_df, columns=["product_name"])
df_sale = pd.DataFrame(sale_df, columns=["qty_sold"])
df = [df_link, df_name, df_sale, df_id, df_cat]
df_final = pd.concat(df, axis=1)
df_final.to_csv("50product.csv")
print(df_final)