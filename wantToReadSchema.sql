DROP TABLE IF EXISTS user_want_to_read;

-- links users and books they want to read. 
--single user can add many books / a book can go to many users
CREATE Table user_want_to_read (
    user_id INTEGER, 
    book_id INTEGER, 

    FOREIGN KEY (user_id) REFERENCES user (id),
    FOREIGN Key (book_id) REFERENCES books (id), 
    PRIMARY KEY (user_id, book_id)

);