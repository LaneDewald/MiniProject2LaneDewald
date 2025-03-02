### INF601 - Advanced Programming in Python
### Lane Dewald
### Mini Project 1

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random

# Initialize Faker for generating random state names
fake = Faker()

# Set Seaborn theme
sns.set_theme(style="darkgrid")

# Generate random data for 20 states
states = [fake.state() for _ in range(20)]
num_homes = [random.randint(10000, 1000000) for _ in range(20)]
high_speed_access = [random.uniform(50, 100) for _ in range(20)]

# Create a DataFrame to store the generated data
data = pd.DataFrame({
    "State": states,
    "Total Homes Sampled": num_homes,
    "% with 100Mbps+": high_speed_access
})

# Create directory for saving charts
os.makedirs("charts", exist_ok=True)

# --- BAR CHART: High-Speed Internet Access by State ---
plt.figure(figsize=(12, 6))
sns.barplot(y=data["State"], x=data["% with 100Mbps+"], hue=data["State"], palette="coolwarm", legend=False)
plt.xlabel("Percentage with 100Mbps+ Internet")
plt.ylabel("State")
plt.title("Percentage of Homes with High-Speed Internet by State")
plt.savefig("charts/high_speed_access.png")
plt.close()

# --- SCATTER PLOT: Internet Speed Access vs. Sample Size ---
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data["Total Homes Sampled"], y=data["% with 100Mbps+"], hue=data["State"], palette="viridis", s=100)
plt.xlabel("Total Homes Sampled")
plt.ylabel("Percentage with 100Mbps+ Internet")
plt.title("Internet Speed Access vs. Sample Size")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig("charts/internet_access_scatter.png")
plt.close()

# --- PIE CHART: Top 5 States with Highest High-Speed Internet Access ---
top5 = data.nlargest(5, "% with 100Mbps+")
plt.figure(figsize=(8, 8))
plt.pie(top5["% with 100Mbps+"], labels=top5["State"], autopct="%1.1f%%", colors=sns.color_palette("pastel"))
plt.title("Top 5 States with Highest High-Speed Internet Access")
plt.savefig("charts/top5_high_speed.png")
plt.close()

# --- BOX PLOT (Distribution of High-Speed Internet Access) ---
plt.figure(figsize=(8, 5))
sns.boxplot(y=data["% with 100Mbps+"])  # Box plot to show spread and outliers
plt.ylabel("Percentage with 100Mbps+ Internet")
plt.title("Distribution of High-Speed Internet Access Across States")
plt.savefig("charts/high_speed_distribution.png")
plt.close()

# --- HISTOGRAM (Frequency of Internet Access Percentage) ---
plt.figure(figsize=(10, 6))
sns.histplot(data["% with 100Mbps+"], bins=10, kde=True, color="blue")  # Histogram to show distribution
plt.xlabel("Percentage with 100Mbps+ Internet")
plt.ylabel("Frequency")
plt.title("Distribution of States by Internet Access Percentage")
plt.savefig("charts/internet_access_histogram.png")
plt.close()

# Print first few rows of the dataset to verify the generated data
print(data.head())