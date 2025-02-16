import matplotlib.pyplot as plt
import seaborn as sns

def plot_bar_chart(df):
    plt.figure(figsize=(10,6))
    sns.barplot(x='Keyword', y='Count', hue='Outlet', data=df)
    plt.title("Article Counts per Keyword by News Outlet")
    plt.xlabel("Keyword")
    plt.ylabel("Article Count")
    plt.show()

def plot_pie_charts(df):
    outlets = df['Outlet'].unique()
    for outlet in outlets:
        outlet_data = df[df['Outlet'] == outlet]
        plt.figure(figsize=(6,6))
        plt.pie(outlet_data['Count'], labels=outlet_data['Keyword'], autopct='%1.1f%%', startangle=140)
        plt.title(f"{outlet} Article Distribution by Keyword")
        plt.show()
