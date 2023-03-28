import time
from utils_keyword import open_product_v1_search_asuspromaxm1, open_product_v2_search_asuspromaxm1, driver, close_dialog

# Setup Connection and product
SCROLL_LOOP = 100
CATEGORY = "Avoskin"
CONNECTION = "192.168.0.100:5555"
SKIP = False  # First time set to False, set True if you want to continue the process
SERVER_APPIUM_PORT = "4723"
SERVER_APPIUM_IP = "127.0.0.1"

# Setup Component
SHARE_BUTTON = "com.ss.android.ugc.trill:id/hf0"
COPY_BUTTON = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]"
CLOSE_DIALOG = "com.ss.android.ugc.trill:id/f54"

DESIRED_CAPS = {
    "platformName": "Android",
    "deviceName": "device",
    "udid": CONNECTION,
    "noReset": True,
}

driver = driver(SERVER_APPIUM_IP=SERVER_APPIUM_IP, SERVER_APPIUM_PORT=SERVER_APPIUM_PORT, desired_caps=DESIRED_CAPS)

### Scroll Default
startx = driver.get_window_size()['width']*1/4; endx = driver.get_window_size()['width']*1/4
starty = driver.get_window_size()['height']*8/11; endy = driver.get_window_size()['height']/8

k = 0
while k <= SCROLL_LOOP:
    print (f"Scrape the loop at {k}")
    open_product_v1_search_asuspromaxm1(CATEGORY)
    driver.swipe(startx, 1900, endx, 850, 400) # Adjust with your device
    time.sleep(1)
    try: close_dialog()
    except: pass
    k = k + 1