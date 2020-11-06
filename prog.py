#!/usr/bin/env python3
import cv2
import time
from selenium import webdriver





browser = webdriver.Chrome(executable_path='/home/l1/python/coockie_monster/chromedriver')
browser.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)
options_button = browser.find_element_by_id('prefsButton')
options_button.click()

count = 1
while True:
  count = count+1
  main_cookie = browser.find_element_by_id('bigCookie')
  main_cookie.click()
  print (count)
  if (count==100):
    save_button = browser.find_element_by_link_text("Save to file")
    save_button.click()
    time.sleep(5)


