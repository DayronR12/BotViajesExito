from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=service)
bot.maximize_window()
time.sleep(3)

bot.get("https://www.viajesexito.com/")
time.sleep(40)
 
closewindow = bot.find_element(By.XPATH, '/html/body/div/div/div/div[1]')
time.sleep(4)
closewindow.click()
time.sleep(3)