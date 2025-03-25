import re
import json
from json import JSONDecodeError
import random

def extract_count_times_of_india(soup):
    try:
        # Find the <a> element with id="Articles"
        articles_link = soup.find('a', id='Articles')
        if articles_link:
            # Find the <span> inside the <a> element
            count_span = articles_link.find('span')
            if count_span:
                # Get the text and remove whitespace
                count_text = count_span.text.strip()
                # DEBUGGING 
                print(f"Extracted text: {count_text}")
                # Keep only the digits
                count_text = ''.join(filter(str.isdigit, count_text))
                # Convert to integer
                return int(count_text)
        # Return 0 if elements are not found
        return 0
    except Exception as e:
        print(f"Extraction error: {str(e)}")
        return 0

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