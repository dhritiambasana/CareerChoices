def extract_count_times_of_india(soup):
    # Find all article containers (update class based on live inspection)
    articles = soup.find_all('div', class_='uwU81')  # Replace with actual class
    return len(articles)

def extract_count_indian_express(soup):
    element = soup.find('span', class_='results-count')
    if element:
        count_text = element.get_text()
        count = int(''.join(filter(str.isdigit, count_text)))
        return count
    else:
        return 0

def extract_count_ndtv(soup):
    element = soup.find('div', class_='search-results')  # Adjust selector as needed
    if element:
        count_text = element.get_text()
        count = int(''.join(filter(str.isdigit, count_text)))
        return count
    else:
        return 0

def extract_count_hindustan_times(soup):
    element = soup.find('div', class_='search-results-count')  # Adjust as needed
    if element:
        count_text = element.get_text()
        count = int(''.join(filter(str.isdigit, count_text)))
        return count
    else:
        return 0

def extract_count_the_better_india(soup):
    element = soup.find('div', class_='search-results-count')  # Adjust as needed
    if element:
        count_text = element.get_text()
        count = int(''.join(filter(str.isdigit, count_text)))
        return count
    else:
        return 0

def extract_result_count(outlet, soup):
    if outlet == 'Times of India':
        return extract_count_times_of_india(soup)
    elif outlet == 'Indian Express':
        return extract_count_indian_express(soup)
    elif outlet == 'NDTV':
        return extract_count_ndtv(soup)
    elif outlet == 'Hindustan Times':
        return extract_count_hindustan_times(soup)
    elif outlet == 'The Better India':
        return extract_count_the_better_india(soup)
    else:
        return 0
