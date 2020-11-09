# Load libraries
import time
from selenium import webdriver
from datetime import datetime


def big_cookie_click():
    try:
        main_cookie = browser.find_element_by_id('bigCookie')
        main_cookie.click()
    except Exception:
        return


def diff_in_time(arg):
    now = datetime.now()
    duration = now - arg
    duration_in_s = duration.total_seconds()
    duration_in_m = int(duration_in_s / 60)
    return duration_in_m


def load_last_save(path):
    try:
        f = open(path, 'r')
        data = f.read()
        imp_button = browser.find_element_by_link_text("Import save")
        imp_button.click()
        area = browser.find_element_by_id('textareaPrompt')
        area.send_keys(data)
        f.close()
        load_button = browser.find_element_by_link_text("Load")
        load_button.click()
    except Exception:
        return


def auto_save(path):
    exp_button = browser.find_element_by_link_text("Export save")
    exp_button.click()
    data = browser.find_element_by_id('textareaPrompt').text
    f = open(path, 'w')
    print(data)
    f.write(data)
    f.close()
    ok_button = browser.find_element_by_link_text("All done!")
    ok_button.click()
    print("We made save.")
    time.sleep(5)


def check_if_products_enable():
    try:
        for i in range(17, -1, -1):
            product_elem = browser.find_element_by_id('product' + str(i))
            product_atr = product_elem.get_attribute("class")
            if product_atr == "product unlocked enabled":
                product_elem.click()
    except Exception:
        return


def check_if_upgrade_enable():
    try:
        upgrade_elem = browser.find_element_by_id('upgrade0')
        upgrade_atr = upgrade_elem.get_attribute("class")
        if upgrade_atr == "crate upgrade enabled":
            upgrade_elem.click()
    except Exception:
        return


# Create values Selenium
URL = "https://orteil.dashnet.org/cookieclicker/"
PATH_TO_SAVE = "/home/l1/python/coockie_monster/SolidParrotBakery.txt"
PATH_TO_DRIVER = "/home/l1/python/coockie_monster/chromedriver"

# Open Selenium
browser = webdriver.Chrome(executable_path=PATH_TO_DRIVER)
browser.get(URL)
time.sleep(10)

#Click accept button
gotit_button = browser.find_element_by_link_text("Got it!")
gotit_button.click()

# Open options tab
options_button = browser.find_element_by_id('prefsButton')
options_button.click()

# Load last save
load_last_save(PATH_TO_SAVE)

# Value of app start
start_time = datetime.now()

# Loop with all automation
while True:
    big_cookie_click()
    check_if_products_enable()
    check_if_upgrade_enable()
    # Auto save every n minutes
    time_diff = diff_in_time(start_time)
    if (time_diff > 0) & (time_diff % 5 == 0):
        auto_save(PATH_TO_SAVE)
        start_time = datetime.now()
