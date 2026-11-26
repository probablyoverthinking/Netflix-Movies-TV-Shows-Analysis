
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("netflix_titles.csv")

print("=" * 50)
print("NETFLIX MOVIES AND TV SHOWS CONTENT ANALYSIS") 
print("=" * 50)

print("\nFirst 5 rows of dataset:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nTotal records:", len(df))
print("Total columns:", len(df.columns))


# ==========================================
# 2. DATA CLEANING
# ==========================================

print("\nMissing values before cleaning:")
print(df.isnull().sum())

columns_to_clean = [
    "director",
    "cast",
    "country",
    "rating",
    "duration"
]

for column in columns_to_clean:
    df[column] = df[column].fillna("Unknown")

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nTotal records after cleaning:", len(df))


# ==========================================
# 3. MOVIES VS TV SHOWS ANALYSIS
# ==========================================

content_counts = df["type"].value_counts()

total_movies = content_counts.get("Movie", 0)
total_tv_shows = content_counts.get("TV Show", 0)
total_content = len(df)

movie_percentage = (total_movies / total_content) * 100
tv_percentage = (total_tv_shows / total_content) * 100

print("\n--- Movies vs TV Shows Analysis ---")
print("Total Movies:", total_movies)
print("Total TV Shows:", total_tv_shows)
print(f"Movies Percentage: {movie_percentage:.2f}%")
print(f"TV Shows Percentage: {tv_percentage:.2f}%")

# Pie Chart

plt.figure(figsize=(8, 6))

plt.pie(
    [total_movies, total_tv_shows],
    labels=["Movies", "TV Shows"],
    autopct="%1.2f%%",
    startangle=90
)

plt.title("Netflix Movies vs TV Shows Distribution")
plt.tight_layout()
plt.show()


# ==========================================
# 4. COUNTRY ANALYSIS
# ==========================================

country_data = df[df["country"] != "Unknown"]["country"]

country_counts = (
    country_data
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
)

top_10_countries = country_counts.head(10)

print("\n--- Top 10 Countries by Netflix Content ---")
print(top_10_countries)

# Bar Chart

plt.figure(figsize=(12, 6))

plt.bar(top_10_countries.index, top_10_countries.values)

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ==========================================
# 5. GENRE ANALYSIS
# ==========================================

genre_counts = (
    df["listed_in"]
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
)

top_10_genres = genre_counts.head(10)

print("\n--- Top 10 Genres on Netflix ---")
print(top_10_genres)

# Bar Chart

plt.figure(figsize=(12, 6))

plt.bar(top_10_genres.index, top_10_genres.values)

plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ==========================================
# 6. RATINGS ANALYSIS
# ==========================================

rating_counts = df["rating"].value_counts()

top_10_ratings = rating_counts.head(10)

print("\n--- Netflix Content Ratings ---")
print(top_10_ratings)

# Bar Chart

plt.figure(figsize=(10, 6))

plt.bar(top_10_ratings.index, top_10_ratings.values)

plt.title("Distribution of Netflix Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ==========================================
# 7. YEARLY CONTENT TREND ANALYSIS
# ==========================================

df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

df["year_added"] = df["date_added"].dt.year

yearly_content = (
    df.dropna(subset=["year_added"])
    .groupby("year_added")
    .size()
)

print("\n--- Netflix Content Added Per Year ---")
print(yearly_content)

# Line Chart

plt.figure(figsize=(12, 6))

plt.plot(
    yearly_content.index,
    yearly_content.values,
    marker="o"
)

plt.title("Netflix Content Added Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles Added")
plt.grid(True)
plt.tight_layout()
plt.show()


# ==========================================
# 8. FINAL PROJECT INSIGHTS
# ==========================================

top_country = country_counts.index[0]
top_country_count = country_counts.iloc[0]

top_genre = genre_counts.index[0]
top_genre_count = genre_counts.iloc[0]

top_rating = rating_counts.index[0]
top_rating_count = rating_counts.iloc[0]

peak_year = int(yearly_content.idxmax())
peak_year_count = int(yearly_content.max())

print("\n" + "=" * 50)
print("FINAL PROJECT INSIGHTS")
print("=" * 50)

print(
    f"\n1. Movies make up {movie_percentage:.2f}% "
    "of Netflix content."
)

print(
    f"\n2. {top_country} leads with "
    f"{top_country_count} titles."
)

print(
    f"\n3. {top_genre} is the most common genre "
    f"with {top_genre_count} titles."
)

print(
    f"\n4. {top_rating} is the most common rating "
    f"with {top_rating_count} titles."
)

print(
    f"\n5. {peak_year} recorded the highest content additions "
    f"with {peak_year_count} titles."
)

print("\n" + "=" * 50)
print("PROJECT ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 50)
