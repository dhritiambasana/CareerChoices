def extract_count_times_of_india(soup):
    articles = soup.find_all('div', class_='fHv_i')  # Updated class
    return len(articles)

def extract_count_ndtv(soup):
    # New selector for 2024 NDTV layout
    articles = soup.find_all('div', class_='src_lst-li')
    return len(articles)

def extract_result_count(outlet, soup):
    if outlet == 'Times of India':
        return extract_count_times_of_india(soup)
    elif outlet == 'NDTV':
        return extract_count_ndtv(soup)
        return 0
