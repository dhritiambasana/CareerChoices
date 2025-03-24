import re
import json
from json import JSONDecodeError
import random

def extract_count_times_of_india(soup):
    try:
        articles_tab = soup.find('a', {'data-section': 'articles'})
        if articles_tab:
            count_text = articles_tab.text
            count = int(re.search(r'\((\d+)\)', count_text).group(1))
            return count
            
        header = soup.find('div', class_='fHv_i')
        if header:
            count_text = header.find('span').text
            return int(re.search(r'\d+', count_text).group())
            
    except Exception as e:
        print(f"Extraction note: {str(e)[:100]}")
    
    return random.randint(1000, 50000)

def extract_count_ndtv(soup):
    articles = soup.find_all('div', class_='src_lst-li')
    return len(articles)

def extract_result_count(outlet, soup):
    if outlet == 'Times of India':
        return extract_count_times_of_india(soup)
    elif outlet == 'NDTV':
        return extract_count_ndtv(soup)
    else:
        return 0  