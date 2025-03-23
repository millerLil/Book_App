DROP TABLE IF EXISTS books;

CREATE TABLE books (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    isbn TEXT NOT NULL,
    title TEXT NOT NULL, 
    author TEXT, 
    cover_image TEXT, 
    countryPublished TEXT, 
    bookDescription TEXT,
    genre TEXT, 
    buy TEXT
    
);