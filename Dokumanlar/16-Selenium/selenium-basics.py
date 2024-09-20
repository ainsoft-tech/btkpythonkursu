from selenium import webdriver
import time

driver = webdriver.Edge()

url = "http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.com-homepage.png")

url = "http://github.com/ainsoft-tech"
driver.get(url)

print(driver.title)

if "ainsoft-tech" in driver.title:
    driver.save_screenshot("github-ainsoft-tech.png")

time.sleep(2)

driver.back()
# driver.forward()

time.sleep(2)

driver.close()

