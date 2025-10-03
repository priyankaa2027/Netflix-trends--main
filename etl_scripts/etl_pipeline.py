import pandas as pd
from sqlalchemy import create_engine

# --- 1. CONNECT TO THE DATABASE ---
# Replace with your actual PostgreSQL credentials
db_uri = "postgresql://postgres:Priyankekek%402027@localhost:5432/netflix"
engine = create_engine(db_uri)

print("Connection to PostgreSQL database established.")

# --- 2. EXTRACT AND TRANSFORM DATA ---
# Load the raw dataset
df = pd.read_csv('../data/netflix_titles.csv')
print("Raw data loaded.")

# Clean up column names (replace spaces with underscores)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_', regex=False)

# Convert 'date_added' to datetime format, handling potential errors
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# --- 3. LOAD SHOWS TABLE ---
# Prepare the data for the 'Shows' table
df_shows = df[['show_id', 'type', 'title', 'director', 'cast', 'date_added', 'release_year', 'rating', 'duration', 'description']].copy()
df_shows.rename(columns={'cast': 'cast_members'}, inplace=True)

# Send data to the 'Shows' SQL table
df_shows.to_sql('shows', engine, if_exists='replace', index=False)
print("'Shows' table has been populated.")

# --- 4. NORMALIZE AND LOAD GENRE TABLES ---
# Create a dataframe for genres by splitting the 'listed_in' column
df_genres_exploded = df[['show_id', 'listed_in']].copy()
df_genres_exploded['listed_in'] = df_genres_exploded['listed_in'].str.split(', ')
df_genres_exploded = df_genres_exploded.explode('listed_in')
df_genres_exploded.rename(columns={'listed_in': 'genre_name'}, inplace=True)

# Create and load the 'Genres' table with unique genre names
df_unique_genres = pd.DataFrame(df_genres_exploded['genre_name'].unique(), columns=['genre_name'])
df_unique_genres.to_sql('genres', engine, if_exists='replace', index=True, index_label='genre_id')
print("'Genres' table has been populated.")

# Create and load the 'ShowGenres' bridge table
# First, get the genre_id from the 'Genres' table
genres_from_db = pd.read_sql('genres', engine)
df_show_genres = pd.merge(df_genres_exploded, genres_from_db, on='genre_name')
df_show_genres = df_show_genres[['show_id', 'genre_id']]

df_show_genres.to_sql('showgenres', engine, if_exists='replace', index=False)
print("'ShowGenres' table has been populated.")

print("ETL process complete!")