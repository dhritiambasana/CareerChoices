from data_collection import collect_news_data
from visualize_data import plot_bar_chart, plot_pie_charts

def main():
    # Define target news sites with their search URL bases
    news_sites = {
        'Times of India': 'https://timesofindia.indiatimes.com/topic/',
        # 'Indian Express': 'https://indianexpress.com/?s=',
        'NDTV': 'https://www.ndtv.com/search?searchtext=',
        # 'Hindustan Times': 'https://www.hindustantimes.com/search?q=',
        # 'The Better India': 'https://www.thebetterindia.com/?s='
    }
    
    # Define keywords (Group 1 and Group 2 combined)
    keywords = [
        # Group 1: Entertainment & Education Keywords
        'Bollywood celebrity gossip',
        'Red Carpet events',
        'Filmfare Awards',
        'Movie box office collection',
        'Reality TV careers',
        'Influencer lifestyle',
        'Engineering colleges',
        'Medical entrance exams',
        'UPSC preparation',
        'MBA placements',
        # Group 2: Innovation, Science & Career Topics
        'Indian scientists breakthrough',
        'Social entrepreneurship India',
        'Grassroots innovators',
        'Rural healthcare workers',
        'Environmental conservation careers',
        'Sports achievements (non-cricket)',
        'Arts fellowship grants',
        'AI startups India',
        'Renewable energy jobs',
        'Ethical hacking careers',
        'Digital content creation careers',
        'Vocational training success',
        'Craftsman livelihoods',
        'Culinary arts institutes',
        'Animation industry growth'
    ]
    
    # Collect data from all news sites and keywords
    df = collect_news_data(news_sites, keywords)
    
    # Optionally save the data to a CSV file
    df.to_csv('news_coverage_counts.csv', index=False)
    
    # Visualize the data
    plot_bar_chart(df)
    plot_pie_charts(df)

if __name__ == '__main__':
    main()
