import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_most_least_chart(df, n=10):
    """Visualize top and bottom N keywords by article count."""
    df_agg = df.groupby('Keyword', as_index=False)['Count'].sum()
    
    df_agg = df_agg[df_agg['Count'] > 0]
    
    sorted_df = df_agg.sort_values('Count', ascending=False)
    
    top = sorted_df.head(n)
    bottom = sorted_df.tail(n).sort_values('Count', ascending=True)
    
    combined = pd.concat([top, bottom])
    combined['Category'] = ['Most Discussed']*n + ['Least Discussed']*n

    plt.figure(figsize=(16, 10))
    ax = sns.barplot(x='Count', y='Keyword', hue='Category', 
                    data=combined, dodge=False,
                    palette={'Most Discussed':'#1f77b4', 'Least Discussed':'#d7191c'})

    ax.set_xlim(0, df_agg['Count'].max() * 1.15)  # Add 15% padding
    
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))
    
    for p in ax.patches:
        ax.annotate(f'{p.get_width():,}', 
                   (p.get_width(), p.get_y() + p.get_height()/2.),
                   ha='left', va='center',
                   xytext=(10, 0), 
                   textcoords='offset points',
                   fontsize=10,
                   color='#2c3e50')

    plt.title('Comprehensive News Coverage Analysis: Actual Article Counts', 
             fontsize=18, pad=20, weight='bold')
    plt.xlabel('Total Articles', fontsize=14)
    plt.ylabel('')
    sns.despine()
    plt.tight_layout()
    plt.show()