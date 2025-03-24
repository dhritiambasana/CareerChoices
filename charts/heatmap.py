import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Sample data (replace with your dataset)
data = {
    'Keyword': ['AI Startups', 'Renewable Energy Jobs', 'Ethical Hacking', 'Bollywood Gossip', 'UPSC Prep'],
    'Google Trends': [0.8, 0.6, 0.4, -0.2, 0.1],
    'AISHE Enrollment': [0.7, 0.5, 0.3, -0.1, 0.4],
    'Job Portal Trends': [0.6, 0.7, 0.5, -0.3, 0.2]
}
df = pd.DataFrame(data).set_index('Keyword')

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    df,
    annot=True,
    cmap='coolwarm',
    center=0,
    linewidths=0.5,
    fmt=".2f",
    annot_kws={'size': 10}
)
plt.title('Correlation: Media Coverage vs. Career Trends', fontsize=14, pad=15)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('coverage_correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()