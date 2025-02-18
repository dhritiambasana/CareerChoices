import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys  # Added for Keys.RETURN
from numpy import random

def get_page_content_selenium(url, outlet=None):
    options = FirefoxOptions()
    options.add_argument('--headless')
    options.set_preference("dom.webdriver.enabled", False)  # Bypass bot detection
    options.set_preference("javascript.enabled", True)
    options.set_preference("permissions.default.image", 2)  # Disable images
    # Randomize browser fingerprint
    options.set_preference("general.appname.override", "Netscape")
    options.set_preference("general.platform.override", "Win32")
    options.set_preference("privacy.trackingprotection.enabled", True)
    driver = webdriver.Firefox(options=options)
    # Add human-like delay before scrolling
    time.sleep(random.uniform(1, 3))
    driver.get(url)
    
    for _ in range(3):  # Scroll 3 times
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2) 
        
    try:
        driver.find_element(By.ID, 'cookie-close').click()
    except:
        pass
    
    try:
        if outlet == 'Times of India':
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.fHv_i, div.uwU81"))
            )
        elif outlet == 'NDTV':
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.src_lst-li"))
            )
            for _ in range(5):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1.5)
                
    except Exception as e:
        print(f"Error loading articles for {url}: {e}")
    
    html = driver.page_source
    driver.quit()
    return BeautifulSoup(html, 'html.parser')