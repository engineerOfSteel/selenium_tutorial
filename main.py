from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# https://googlechromelabs.github.io/chrome-for-testing/#stable

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

# Wait for element with class belonging to search bar input text to load
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("tech with tim" + Keys.ENTER)

# Wait for elements matching partial text to load
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
)

# partial match
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")

# exact match
# link = driver.find_element(By.LINK_TEXT, "Tech With Tim")

# return an array of all elements on page with text match
# links = driver.find_elements(By.LINK_TEXT, "Tech With Tim")


link.click()

time.sleep(10)

driver.quit()
