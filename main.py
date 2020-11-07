# Load libraries
import time
from selenium import webdriver
from datetime import datetime


def diff_in_time(arg):
    now = datetime.now()
    duration = now - arg
    duration_in_s = duration.total_seconds()
    duration_in_m = int(duration_in_s / 60)
    return duration_in_m


def auto_save(arg):
    if (arg > 0) & (arg % 10 == 0):
        save_button = browser.find_element_by_link_text("Save to file")
        save_button.click()
        time.sleep(5)


def check_product_enable():
    for i in range(17, -1, -1):
        product_elem = browser.find_element_by_id('product' + str(i))
        product_atr = product_elem.get_attribute("class")
        if product_atr == "product unlocked enabled":
            product_elem.click()


# Create values Selenium
URL = "https://orteil.dashnet.org/cookieclicker/"

# Open Selenium
browser = webdriver.Firefox(executable_path=r"C:\Users\User\Desktop\test\geckodriver.exe")
browser.get(URL)
time.sleep(5)
options_button = browser.find_element_by_id('prefsButton')
options_button.click()

start_time = datetime.now()
while True:
    main_cookie = browser.find_element_by_id('bigCookie')
    main_cookie.click()

    time_diff = diff_in_time(start_time)
    #auto_save(time_diff)

    check_product_enable()
