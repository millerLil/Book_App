DROP TABLE IF EXISTS users;

CREATE TABLE users (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL,
    email TEXT NOT NULL,
    userName TEXT NOT NULL UNIQUE,
    userPW TEXT NOT NULL,

    userWeight FLOAT DEFAULT 0,

    currentBook TEXT,
    userBio TEXT,
    userPhoto BLOB,
    userActive BOOLEAN DEFAULT TRUE

);

