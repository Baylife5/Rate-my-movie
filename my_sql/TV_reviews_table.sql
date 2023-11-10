CREATE DATABASE TV_polls;

USE TV_polls;

CREATE TABLE reviewer(

    id INT AUTO_INCREMENT PRIMARY KEY,
    f_name VARCHAR(255) NOT NULL,
    l_name VARCHAR(255) NOT NULL
);

CREATE TABLE series(

    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    release_date INT NOT NULL,
    genre VARCHAR(255) NOT NULL
);


CREATE TABLE reviews(

    id INT AUTO_INCREMENT PRIMARY KEY,
    rating DEC(2 , 1),
    series_id INT,
    reviewer_id INT,
    FOREIGN KEY(series_id) REFERENCES series(id),
    FOREIGN KEY(reviewer_id) REFERENCES reviewer(id)
);
