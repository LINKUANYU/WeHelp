-- create DB
CREATE DATABASE IF NOT EXISTS website
    DEFAULT CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
USE website;

-- create table member
CREATE TABLE IF NOT EXISTS member(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    follower_count INT NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uk_member_email (email)
)ENGINE=InnoDB;

-- create table message
CREATE TABLE IF NOT EXISTS message(
    id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT NOT NULL,
    content TEXT NOT NULL,
    like_count INT NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_message_member
        FOREIGN KEY (member_id) REFERENCES member (id)
        ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=InnoDB;


