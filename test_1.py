from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
serve_obj = Service()

#create browser instance
driver= webdriver.Chrome(executable_path="/home/prayog/Desktop/Sakshi_Work_Linux/Data_Work/scraping_test/chromedriver")

# to visit/open any website
driver.get("https://github.com/login")
time.sleep(3)


#tell browser to find element
driver.find_element(By.NAME, "login").send_keys("sakshi-279")
driver.find_element(By.NAME, "password").send_keys("567@Papa")

#to tell browser to click any element of website
driver.find_element(By.NAME, "commit").click()
time.sleep(3)