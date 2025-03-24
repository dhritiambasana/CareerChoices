import pandas as pd
from scraper_utils import get_page_content_selenium
from results_extractor import extract_result_count

import random
import time

def collect_news_data(news_sites, keywords):
    data = []
    for outlet, base_url in news_sites.items():
        for keyword in keywords:
            time.sleep(random.randint(5, 15))
            total_count = 0
            
            try:
                if outlet == 'Times of India':
                    formatted_keyword = keyword.replace(' ', '-').lower()
                    search_url = f"{base_url}{formatted_keyword}/news" 
                    soup = get_page_content_selenium(search_url, outlet)
                    total_count = extract_result_count(outlet, soup)
                            
                else:
                    formatted_keyword = keyword.replace(' ', '+')
                    search_url = base_url + formatted_keyword
                    soup = get_page_content_selenium(search_url, outlet)
                    total_count = extract_result_count(outlet, soup)
                    
                print(f"{outlet} - {keyword}: {total_count} articles")
                data.append({'Outlet': outlet, 'Keyword': keyword, 'Count': total_count})
                
            except Exception as e:
                print(f"Error: {e}")
                data.append({'Outlet': outlet, 'Keyword': keyword, 'Count': 0})
                
    return pd.DataFrame(data)