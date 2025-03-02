### INF601 - Advanced Programming in Python
### Lane Dewald
### Mini Project 1

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random


fake = Faker()
sns.set_theme(style="darkgrid")

states = [fake.state() for _ in range(20)]
num_homes = [random.randint(10000, 1000000) for _ in range(20)]
high_speed_access = [random.uniform(50, 100) for _ in range(20)]

data = pd.DataFrame({
    "State": states,
    "Total Homes Sampled": num_homes,
    "% with 100Mbps+": high_speed_access
})

os.makedirs("charts", exist_ok=True)

plt.figure(figsize=(12, 6))
sns.barplot(y=data["State"], x=data["% with 100Mbps+"], hue=data["State"], palette="coolwarm", legend=False)
plt.xlabel("Percentage with 100Mbps+ Internet")
plt.ylabel("State")
plt.title("Percentage of Homes with High-Speed Internet by State")
plt.savefig("charts/high_speed_access.png")
plt.close()

plt.figure(figsize=(10, 6))
sns.scatterplot(x=data["Total Homes Sampled"], y=data["% with 100Mbps+"], hue=data["State"], palette="viridis", s=100)
plt.xlabel("Total Homes Sampled")
plt.ylabel("Percentage with 100Mbps+ Internet")
plt.title("Internet Speed Access vs. Sample Size")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig("charts/internet_access_scatter.png")
plt.close()

top5 = data.nlargest(5, "% with 100Mbps+")
plt.figure(figsize=(8, 8))
plt.pie(top5["% with 100Mbps+"], labels=top5["State"], autopct="%1.1f%%", colors=sns.color_palette("pastel"))
plt.title("Top 5 States with Highest High-Speed Internet Access")
plt.savefig("charts/top5_high_speed.png")
plt.close()

print(data.head())