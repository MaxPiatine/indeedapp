# Job search will find the specified jobs I want and put them into the search bar of Indeed.com, 
# After scanning through different html code, it will Identify the Job Position, and Company
# Then will be sent to the Word.py so that my Cover Letter can be modified according to 
# Job position and company

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import numpy as np
from datetime import date

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
careers = ["Statistics", "Physics"]


class Indeed:
    def __init__(self, position, place, salary=50000) -> None:
        self.url = 'https://secure.indeed.com/auth?hl=en_CA&co=CA&continue=https%3A%2F%2Fca.indeed.com%2F%3Ffrom%3Dgnav-resume--myind&tmpl=desktop&service=my&from=gnav-util-homepage&jsContinue=https%3A%2F%2Fca.indeed.com%2F&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess&_ga=2.34578849.1220811309.1651437530-1444345694.1651206427'
        self.position = position
        self.salary = 50000
        self.place = place
        self.email = "max.piatine@hotmail.com"
        with open('Password.txt') as f:
            self.password = f.readlines()[0]
        self.links1 = []
        self.links2 = []
    
    def search(self):
        driver.get(self.url)

    def signin(self):

        username = driver.find_element_by_id("ifl-InputFormField-3")
        username.send_keys(self.email)
        driver.find_element_by_xpath("//button[@type='submit'][@class='i-unmask css-157vc5a e8ju0x51']").click()

        time.sleep(1)
                                                
        password = driver.find_element_by_id("ifl-InputFormField-126")
        password.send_keys(self.password)
        driver.find_element_by_xpath("//button[@type='submit'][@class='i-unmask css-157vc5a e8ju0x51']").click()


    def interest(self):
        what = driver.find_element_by_name("q")
        what.send_keys(self.position)
        driver.find_element_by_xpath("//button[@class='yosegi-InlineWhatWhere-primaryButton'][@type='submit']").click()

    def information(self):
        if len(self.links1) == 0:
            lst = self.links2
        else:
            lst = self.links1

        for k in lst:
            Link(k).execute()
    
    def apply(self):
        options = driver.find_elements(By.XPATH,"//ul[@class='jobsearch-ResultsList']/li")
        print(options)
        for i in range(len(options)):
            self.links1.append(options[i].get_attribute("href"))
            print(options[i].find_element_by_tag_name("a").get_attribute("href"))
        return self.links1

    def apply2(self):
        options = driver.find_elements(By.XPATH,"//div[@id='mosaic-provider-jobcards'][@class='mosaic mosaic-provider-jobcards mosaic-provider-hydrated']/a")
        print(options)
        for j in range(len(options)):
            self.links2.append(options[j].get_attribute("href"))
            print(options[j].get_attribute("href"))
        return self.links2

class Link:
    def __init__(self,http):
        self.http = http
    
    def execute(self):
        driver.execute_script("window.open('"+str(self.http)+"','_blank');")


class LinkedIn(Indeed):
    def __init__(self, position, place, salary=50000):
        self.position = position
        self.where = where
        self.email = "max.piatine@hotmail.com"
        self.place = place
        with open('Password.txt') as f:
            self.password = f.readlines()[0]
        self.url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"

    def signin(self):
        self.search()

        username = driver.find_element_by_id("username")
        password = driver.find_element_by_id("password")

        username.send_keys(self.email)
        password.send_keys(self.password)

        driver.find_element_by_name("submit").click()

    def interest(self):
        pass