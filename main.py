from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(executable_path="D:/Skills/Python/Projects/Google Meet Bot/ChromeDrivers/win32")
driver = webdriver.Chrome(service=service)