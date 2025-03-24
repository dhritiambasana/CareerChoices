from data_collection import collect_news_data
from visualize_data import plot_most_least_chart

def main():
    news_sites = {
        'Times of India': 'https://timesofindia.indiatimes.com/topic/',
        # 'NDTV': 'https://www.ndtv.com/search?searchtext='
    }
    
    keywords = [
        'Bollywood',
        'Red Carpet',
        'Filmfare',
        'Box Office',
        'Reality TV',
        'Influencers',
        'Engineering',
        'Medicine',
        'UPSC',
        'MBA',
        'Astronomy',
        'Nanotech',
        'Neurotech',
        'Genomics',
        'Ethnomusic',
        'Aerospace',
        'Cyberlaw',
        'Biomimetics',
        'Cartography',
        'Gastronomy'
    ]

    df = collect_news_data(news_sites, keywords)
    
    df.to_csv('news_coverage_counts.csv', index=False)
    
    plot_most_least_chart(df)

if __name__ == '__main__':
    main()
