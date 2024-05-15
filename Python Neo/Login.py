import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# Creates a new instance of the Chrome Webdriver
driver = webdriver.Chrome()
driver.get("https://stage.neo.clootrack.com/")
driver.maximize_window()
input("Press Enter to close the browser window...")