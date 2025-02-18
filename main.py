from data_collection import collect_news_data
from visualize_data import plot_bar_chart, plot_pie_charts, plot_timeseries_comparison

def main():
    # Define target news sites with their search URL bases
    news_sites = {
        'Times of India': 'https://timesofindia.indiatimes.com/topic/',
        'NDTV': 'https://www.ndtv.com/search?searchtext='
    }
    
    # Define keywords (Group 1 and Group 2 combined)
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
        'Forensics',
        'Genomics',
        'Conservation',
        'Archaeology',
        'Ethnomusic',
        'Quantum',
        'Aerospace',
        'Cyberlaw',
        'Biomimetics',
        'Cartography',
        'Gastronomy',
        'Cinematography'
    ]

    
    # Collect data from all news sites and keywords
    df = collect_news_data(news_sites, keywords)
    
    # Optionally save the data to a CSV file
    df.to_csv('news_coverage_counts.csv', index=False)
    
    # Visualize the data
    plot_bar_chart(df)
    plot_pie_charts(df)
    plot_timeseries_comparison(df)

if __name__ == '__main__':
    main()
