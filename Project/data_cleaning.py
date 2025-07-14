# === CLEANING SECTION ===
import pandas as pd
import re

# Load the dataset
df = pd.read_csv("Drug_Review_Cleaned.csv")

# Basic Data Overview
print("Dataset shape:", df.shape)
print("\nDataset info:")
print(df.info())
print("\nNull values in each column:")
print(df.isnull().sum())
print("\nSample rows:")
print(df.head())

# Clean the 'review' column
df['review'] = df['review'].astype(str).str.strip('"').str.strip()
df['review_cleaned'] = df['review'].str.lower()
df['review_cleaned'] = df['review_cleaned'].apply(lambda x: re.sub(r'[^a-z\s]', '', x))
df['review_cleaned'] = df['review_cleaned'].apply(lambda x: re.sub(r'\s+', ' ', x).strip())

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Extract year, month, and day from the date column
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

# Preview cleaned text and date columns
print("\nPreview of cleaned review and date columns:")
print(df[['review_cleaned', 'date', 'year', 'month', 'day']].head())

# Save cleaned output
df.to_csv("review_cleaned_output.csv", index=False)
print("\nCleaned dataset saved as: review_cleaned_output.csv") 

# === EDA SECTION ===
# Start with importing visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")

# 1. Sentiment Distribution
plt.figure(figsize=(6,4))
sns.countplot(x="Sentiment", data=df)
plt.title("Sentiment Distribution")
plt.savefig("plots/sentiment_distribution.png")

# 2. Rating Distribution
plt.figure(figsize=(6,4))
sns.histplot(df["rating"], bins=10, kde=True)
plt.title("Rating Distribution")
plt.savefig("plots/rating_distribution.png")

# 3. Review Length vs Sentiment
plt.figure(figsize=(6,4))
sns.boxplot(x="Sentiment", y="review_length", data=df)
plt.title("Review Length by Sentiment")
plt.savefig("plots/review_length_by_sentiment.png")

# 4. Top 10 Conditions by Frequency
top_conditions = df['condition'].value_counts().head(10)
plt.figure(figsize=(8,5))
sns.barplot(x=top_conditions.values, y=top_conditions.index)
plt.title("Top 10 Conditions")
plt.xlabel("Number of Reviews")
plt.savefig("plots/top_conditions.png")

# 5. Reviews per Year
plt.figure(figsize=(8,5))
sns.countplot(x="year", data=df, order=sorted(df['year'].dropna().unique()))
plt.title("Reviews by Year")
plt.xticks(rotation=45)
plt.savefig("plots/reviews_by_year.png")