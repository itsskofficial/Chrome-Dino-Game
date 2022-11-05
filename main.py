from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import *

service = Service(executable_path="D:/Skills/Python/Projects/Google Meet Bot/ChromeDrivers/win32")
driver = webdriver.Chrome(service=service)

driver.get('https://chromedino.com/')
sleep(2)

