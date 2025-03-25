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
    # options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    
    try:
        # Navigate to the URL
        driver.get(url)
        if outlet == 'Times of India':
            # Wait for the <a id="Articles"> element to be present (up to 15 seconds)
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "Articles"))
            )
        # Get the page source after the element is loaded
        html = driver.page_source
        
        with open('page_source.html', 'w', encoding='utf-8') as f:
            f.write(html)
        
    except Exception as e:
        print(f"Selenium error: {str(e)}")
        html = "empty"  # Return empty HTML on failure
            
        if outlet == 'NDTV':
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.src_lst-li"))
            )
            
        html = driver.page_source
        
    finally:
        driver.quit()
        
    return BeautifulSoup(html, 'html.parser')