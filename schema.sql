DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    post_id INTEGER PRIMARY KEY,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title  TEXT NOT NULL,
    content TEXT NOT NULL

);
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL



);
DROP TABLE IF EXISTS comments;
CREATE TABLE comments (
    comment_id INTEGER PRIMARY KEY,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    text  TEXT NOT NULL,
    post_id INTEGER NOT NULL,
        FOREIGN KEY (post_id)
                      REFERENCES posts(post_id)

);
