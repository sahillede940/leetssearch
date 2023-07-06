import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Selenium Webdriver
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service = s)

#Provide the url of the page to visit
URL = "https://leetcode.com/problemset/all/?page="

#define a function that returns all the required problems links in array
def get_links(url):
    driver.get(url)  #visits webpage
    time.sleep(8)   #gives thime to load the page

    All_links_data = driver.find_elements(By.TAG_NAME, "a")   #get all atag links on that webpage

    links = []
    pattern = "/problems"

    for qlinks in All_links_data:
        try:
            href = qlinks.get_attribute('href')
            if(pattern in href):
                links.append(href)
        except:
            pass
    
    links = list(set(links))

    return links


# Calling get links for all 55 pages
for page in range(1,56): 
    All_links=[]
    url = URL + str(page)
    All_links += get_links(url)
    All_links = list(set(All_links))
    print(url)

    # Now we can store these links in a txt file
    # Open txt file lc.txt in a mode
    file_path = "Leetcode_all_links.txt"
    with open(file_path, 'a') as file:
        for i in All_links:
            file.write(i)
            file.write('\n')

driver.quit()