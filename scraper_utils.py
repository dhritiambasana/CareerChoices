import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def get_page_content_selenium(url):
    options = FirefoxOptions()
    options.add_argument('--headless')
    options.set_preference("dom.webdriver.enabled", False)  # Bypass bot detection
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    
    for _ in range(3):  # Scroll 3 times
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2) 
    
    try:
        # Wait for article elements to load (TOI uses <div class="uwU81"> for articles)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "uwU81"))
        )
    except Exception as e:
        print(f"Error loading articles for {url}: {e}")
    
    html = driver.page_source
    driver.quit()
    return BeautifulSoup(html, 'html.parser')