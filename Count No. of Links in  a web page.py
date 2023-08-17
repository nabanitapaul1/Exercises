# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 22:15:04 2023

@author: Nabanita Paul
"""

#   import modules
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

## open Chrome



driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
## navigate to the URL


driver.get("https://www.geeksforgeeks.org/")
time.sleep(10)

list_link = driver.find_elements(By.TAG_NAME, 'a')

# using len function count how many links
print(len(list_link))
driver.close()