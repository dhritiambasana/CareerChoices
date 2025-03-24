import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys  # Added for Keys.RETURN
from numpy import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def get_page_content_selenium(url, outlet=None):
    options = FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    
    try:
        driver.get(url)
        last_height = driver.execute_script("return document.body.scrollHeight")
        scroll_attempts = 0
        
        if outlet == 'Times of India':
            try:
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "a[data-section='articles'], div.HdLk")
                    )
                )
            except:
                print("Timeout waiting for count elements")
            
        if outlet == 'NDTV':
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.src_lst-li"))
            )
            
        html = driver.page_source
        
    finally:
        driver.quit()
        
    return BeautifulSoup(html, 'html.parser')