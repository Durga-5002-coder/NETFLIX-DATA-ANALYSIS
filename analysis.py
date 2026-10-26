import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")

# 1. Load Data
df = pd.read_csv("netflix_titles.csv")
print("=== First 5 Rows ===")
print(df.head())

# 2. Inspect Structure & Missing Values
print("\n=== Dataset Info ===")
print(df.info())

print("\n=== Missing Values ===")
print(df.isnull().sum())

# 3. Data Cleaning
# Fill missing ratings and countries with standard placeholders
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")
# Drop rows where title or date_added is missing
df.dropna(subset=["date_added"], inplace=True)

# 4. Analysis 1: Content Type Distribution (Movies vs TV Shows)
type_counts = df["type"].value_counts()
print("\n=== Content Type Distribution ===")
print(type_counts)

plt.figure(figsize=(6, 4))
sns.countplot(x="type", data=df, palette="Blues_d")
plt.title("Distribution of Movies vs. TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Total Count")
plt.tight_layout()
plt.savefig("content_distribution.png")
plt.close()

# 5. Analysis 2: Top 10 Content Producing Countries
top_countries = df[df["country"] != "Unknown"]["country"].value_counts().head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="mako")
plt.title("Top 10 Content Producing Countries")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("top_countries.png")
plt.close()

# 6. Analysis 3: Release Trend by Year (2000 to Present)
recent_content = df[df["release_year"] >= 2000]

plt.figure(figsize=(12, 5))
sns.histplot(data=recent_content, x="release_year", hue="type", multiple="stack", bins=25)
plt.title("Growth of Movies and TV Shows (2000 - Present)")
plt.xlabel("Release Year")
plt.ylabel("Number of Releases")
plt.tight_layout()
plt.savefig("release_trends.png")
plt.close()

print("\nAnalysis complete! Charts saved to folder.")