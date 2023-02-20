#import selenium
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.ebay.com/")
time.sleep(4)
driver.find_element(By.XPATH,"(//input[@id='gh-ac'])[1]").click()
time.sleep(4)
driver.find_element(By.XPATH,"(//b[normalize-space()='iphone 11'])[1]").click()
time.sleep(4)
