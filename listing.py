from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///Users/maxpiatine/Documents/indeedapp/index.html")
options = driver.find_elements(By.XPATH,"//ul/li")
for i in range(len(options)):
    print(options[i].find_element_by_tag_name("a").text)

    driver.execute_script('''window.open("http://bings.com","_blank");''')

    time.sleep(5)
