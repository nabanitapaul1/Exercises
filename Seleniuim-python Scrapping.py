# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:09:33 2023

@author: Nabanita Paul
"""

## Download file in Selenium

#   import modules
from selenium import webdriver
import time
## open Chrome 

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
## navigate to the URL


driver.get("http://demo.automationtesting.in/FileDownload.html")
time.sleep(10)

# Enter text
driver.find_element_by_id("textbox").send_keys("Hello World. This is a text file.")


# Generate Text  File

driver.find_element_by_id("createTxt").click()

# Click on Download Button  to  download text file

driver.find_element_by_id("link-to-download").click()


# Enter text
driver.find_element_by_id("pdfbox").send_keys("Hello World. This is a pdf file.")


# Generate PDF  File

driver.find_element_by_id("createPdf").click()

# Click on Download Button   to download text file

driver.find_element_by_id("pdf-link-to-download").click()

driver.quit()
