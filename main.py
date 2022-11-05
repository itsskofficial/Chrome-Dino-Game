from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import *
import pyautogui
from PIL import ImageGrab,Image

service = Service(executable_path="D:/Skills/Python/Projects/Google Meet Bot/ChromeDrivers/win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://chromedino.com/')
sleep(2)
pyautogui.press('space')
t=30

while t:
    game=driver.find_element_by_class_name('runner-container')
    game.screenshot('screen.png')
    img=Image.open()
    sleep(1)
    t-=1

driver.quit()