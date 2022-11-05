from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import *
import pyautogui
import PIL

service = Service(executable_path="D:/Skills/Python/Projects/Google Meet Bot/ChromeDrivers/win32")
driver = webdriver.Chrome(service=service)

driver.get('https://chromedino.com/')
sleep(2)
pyautogui.press('space')
t=30

while t:
    pyautogui.press('space')
    time.sleep(1)

driver.quit()