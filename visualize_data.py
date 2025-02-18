import pandas as pd  # Add this line
import matplotlib.pyplot as plt
import seaborn as sns
from textwrap import wrap
import matplotlib.pyplot as plt
import seaborn as sns
from textwrap import wrap  # For wrapping long labels

# Set professional style
plt.style.use('ggplot')  # Or choose from available styles
sns.set_palette("husl")

def plot_bar_chart(df):
    plt.figure(figsize=(14, 8))
    
    # Sort data and create grouped bars
    df_sorted = df.sort_values(by='Count', ascending=False)
    
    ax = sns.barplot(x='Keyword', y='Count', hue='Outlet', data=df_sorted,
                    estimator=sum, ci=None, dodge=True)
    
    # Improve labels and titles
    plt.title("News Coverage Analysis: Keyword Distribution Across Outlets", 
             fontsize=14, pad=20)
    plt.xlabel("Keywords", fontsize=12)
    plt.ylabel("Article Count", fontsize=12)
    
    # Wrap x-axis labels and rotate
    ax.set_xticklabels(["\n".join(wrap(label.get_text(), 10)) 
                       for label in ax.get_xticklabels()], 
                      rotation=45, ha='right')
    
    # Add value labels
    for p in ax.patches:
        ax.annotate(f"{int(p.get_height())}", 
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha='center', va='center', 
                   xytext=(0, 5), 
                   textcoords='offset points')
    
    plt.legend(title='News Outlet', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def plot_pie_charts(df):
    outlets = df['Outlet'].unique()
    
    # Create subplots
    fig, axes = plt.subplots(1, len(outlets), figsize=(15, 6))
    fig.suptitle('Keyword Distribution by News Outlet', fontsize=16, y=1.02)
    
    for ax, outlet in zip(axes, outlets):
        outlet_data = df[df['Outlet'] == outlet]
        
        # Group small percentages into "Other"
        threshold = 5  # Percentage threshold
        data = outlet_data.copy()
        data['Percentage'] = (data['Count'] / data['Count'].sum()) * 100
        small_categories = data[data['Percentage'] < threshold]
        
        if not small_categories.empty:
            other_row = pd.DataFrame({  # Requires pandas import
                'Keyword': ['Other'],
                'Count': [small_categories['Count'].sum()],
                'Percentage': [small_categories['Percentage'].sum()]
            })
            data = pd.concat([data[data['Percentage'] >= threshold], other_row])
        
        # Create donut chart
        wedges, texts, autotexts = ax.pie(
            data['Count'],
            labels=data['Keyword'],
            autopct='%1.1f%%',
            startangle=140,
            pctdistance=0.85,
            wedgeprops={'width': 0.4, 'edgecolor': 'white'}
        )
        
        # Improve label readability
        plt.setp(texts + autotexts, size=8, weight='bold')
        ax.set_title(outlet, fontsize=12, pad=20)
        ax.axis('equal')  # Equal aspect ratio ensures pie is circular
    
    plt.tight_layout()
    plt.show()

def plot_timeseries_comparison(df):
    # If you have date information, add a time series plot
    plt.figure(figsize=(14, 6))
    sns.lineplot(x='Date', y='Count', hue='Outlet', 
                style='Keyword', data=df, markers=True)
    plt.title('Temporal Coverage Pattern Analysis', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Article Count', fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.show()