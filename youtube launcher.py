from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

exe_path = "D:\webdriver\chrome\chromedriver.exe"


driver = webdriver.Chrome(service=Service(exe_path))


inp= input("enter--> ")

driver.get("https://www.google.com")

search = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
search.send_keys(f"{inp}")
search.send_keys(Keys.ENTER)

video = driver.find_element(By.XPATH,'//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
video.click()
videop = driver.find_element(By.CSS_SELECTOR,'.DhN8Cf a')
videop.click()
 
while True :
    time.sleep(1)