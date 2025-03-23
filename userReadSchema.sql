DROP TABLE IF EXISTS books_user_read;

-- links users and books they haveread. 
--single user can add read books / a book can be read by many users
CREATE Table books_user_read (
    user_id INTEGER, 
    book_id INTEGER, 

    dateRead DATE, 
    rating FLOAT, 
    userReview TEXT,

    FOREIGN KEY (user_id) REFERENCES user (id),
    FOREIGN Key (book_id) REFERENCES books (id), 
    PRIMARY KEY (user_id, book_id)

);