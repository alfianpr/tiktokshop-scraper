import time
from utils_top import open_product_v1_cat_asuspromaxm1, driver, close_dialog, \
     ASUSPROMAXM1, SCROLL_DOWN

# Setup Connection and product
SCROLL_LOOP = 6
CATEGORY = "Avoskin"
CONNECTION = ASUSPROMAXM1
SKIP = False  # First time set to False, set True if you want to continue the process
SERVER_APPIUM_PORT = "4723"
SERVER_APPIUM_IP = "127.0.0.1"

DESIRED_CAPS = {
    "platformName": "Android",
    "deviceName": "device",
    "udid": CONNECTION,
    "noReset": True,
}

SC_1 = SCROLL_DOWN
driver = driver(SERVER_APPIUM_IP=SERVER_APPIUM_IP, SERVER_APPIUM_PORT=SERVER_APPIUM_PORT, desired_caps=DESIRED_CAPS)

k = 0
while k <= SCROLL_LOOP:
    print (f"Scrape the loop at {k}")
    time.sleep(2); open_product_v1_cat_asuspromaxm1(CATEGORY=CATEGORY)
    driver.swipe(SC_1[0], SC_1[1], SC_1[2], SC_1[3], SC_1[4]) # Adjust with your device
    time.sleep(2)
    try: close_dialog()
    except: pass
    k = k + 1