import pandas as pd
from scraper_utils import get_page_content_selenium
from results_extractor import extract_result_count

import random
import time

def collect_news_data(news_sites, keywords):
    data = []
    for outlet, base_url in news_sites.items():
        for keyword in keywords:
            # Add random delay (2-10 seconds) between requests
            time.sleep(random.randint(2, 10))
            if outlet == 'Times of India':
                formatted_keyword = keyword.lower().replace(' ', '-')
                search_url = base_url + formatted_keyword
            else:
                formatted_keyword = keyword.replace(' ', '+')
                search_url = base_url + formatted_keyword
            try:
                soup = get_page_content_selenium(search_url)
                count = extract_result_count(outlet, soup)
            except Exception as e:
                print(f"Error processing {outlet} for '{keyword}': {e}")
                count = 0
            data.append({'Outlet': outlet, 'Keyword': keyword, 'Count': count})
    return pd.DataFrame(data)
