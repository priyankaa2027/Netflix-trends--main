-- Drops tables if they exist to ensure a clean slate
DROP TABLE IF EXISTS ShowGenres, Genres, Shows;

-- Creates the main table for shows
CREATE TABLE Shows (
    show_id VARCHAR(10) PRIMARY KEY,
    type VARCHAR(10),
    title TEXT,
    director TEXT,
    cast_members TEXT,
    date_added DATE,
    release_year INT,
    rating VARCHAR(10),
    duration VARCHAR(20),
    description TEXT
);

-- Creates a table for unique genres
CREATE TABLE Genres (
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(50) UNIQUE
);

-- Creates a bridge table for the many-to-many relationship between shows and genres
CREATE TABLE ShowGenres (
    show_id VARCHAR(10) REFERENCES Shows(show_id),
    genre_id INT REFERENCES Genres(genre_id),
    PRIMARY KEY (show_id, genre_id)
);