import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create figure
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Define nodes and positions
nodes = {
    "Web Scraping (TOI, NDTV)": (2, 6),
    "Data Cleaning (Pandas)": (2, 4.5),
    "Keyword Categorization": (2, 3),
    "Statistical Analysis (SciPy)": (5, 3),
    "Visualization (Seaborn)": (5, 1.5),
    "Insights & Report": (8, 1.5)
}

# Draw nodes
for text, (x, y) in nodes.items():
    ax.add_patch(patches.Rectangle((x-1.5, y-0.3), 3, 0.6, edgecolor='#2ecc71', facecolor='#ecf0f1', lw=2))
    plt.text(x, y, text, ha='center', va='center', fontsize=10, color='#2c3e50')

# Draw arrows
arrows = [
    ((2, 5.7), (2, 5)),  # Scraping → Cleaning
    ((2, 4.2), (2, 3.3)), # Cleaning → Categorization
    ((2, 2.7), (5, 3.3)), # Categorization → Stats
    ((5, 2.7), (5, 1.8)), # Stats → Visualization
    ((5, 1.2), (8, 1.8)), # Visualization → Insights
]

for (x1, y1), (x2, y2) in arrows:
    plt.annotate("", xy=(x2, y2), xytext=(x1, y1), 
                 arrowprops=dict(arrowstyle='->', lw=2, color='#3498db'))

# Add title
plt.title("Data Analysis Workflow", fontsize=14, pad=20, color='#2c3e50')
plt.savefig('data_pipeline_flowchart.png', dpi=300, bbox_inches='tight')
plt.show()