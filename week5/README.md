# Week 5 assignment 

## Task 2
1. Create a new database named website.

`CREATE DATABASE website;`

2. Create a new table named member, in the website database, designed as below:

`CREATE TABLE member(
  id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  follower_count INT NOT NULL DEFAULT 0,
  time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);`
![task](task2.png)


## Task 3
1. INSERT a new row to the member table where name, email and password must beset to test, test@test.com, and test. INSERT additional 4 rows with arbitrary data.


`INSERT INTO member (name, email, password) VALUES ('test', 'test@test.com', 'test');`

`INSERT INTO member (name, email, password) VALUES ('monday', 'monday@test.com', 'monday');`

`INSERT INTO member (name, email, password) VALUES ('tuesday', 'tuesday@test.com', 'tuesday');`

`INSERT INTO member (name, email, password) VALUES ('wednesday', 'wednesday@test.com', 'wednesday');`

`INSERT INTO member (name, email, password) VALUES ('thursday', 'thursday@test.com', 'thursday');`

![task](task3/task3-1.png)

2. SELECT all rows from the member table.

`SELECT * FROM member;`
![task](task3/task3-2.png)

3. SELECT all rows from the member table, in descending order of time.

`SELECT * FROM member ORDER BY time DESC;`
![task](task3/task3-3.png)

4. SELECT total 3 rows, second to fourth, from the member table, in descending order of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.

`SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;`
![task](task3/task3-4.png)

5. SELECT rows where email equals to test@test.com.

`SELECT * FROM member WHERE email = 'test@test.com';`
![task](task3/task3-5.png)

6. SELECT rows where name includes the es keyword.

`SELECT * FROM member WHERE name LIKE '%es%';`
![task](task3/task3-6.png)

7. SELECT rows where email equals to test@test.com and password equals to test.

`SELECT * FROM member WHERE email = 'test@test.com' AND password = 'test';`
![task](task3/task3-7.png)

8. UPDATE data in name column to test2 where email equals to test@test.com.

`UPDATE member SET name = 'test2' WHERE email = 'test@test.com';`
![task](task3/task3-8.png)

# Task 4
1. SELECT how many rows from the member table.

`SELECT COUNT(*) FROM member;`

![task](task4/task4-1.png)

2. SELECT the sum of follower_count of all the rows from the member table.

`UPDATE member SET follower_count = FLOOR(RAND() * 100);`

`SELECT SUM(follower_count) FROM member;`
![task](task4/task4-2.png)

3. SELECT the average of follower_count of all the rows from the member table.

`SELECT AVG(follower_count) FROM member;`
![task](task4/task4-3.png)

4. SELECT the average of follower_count of the first 2 rows, in descending order of
follower_count, from the member table.

`SELECT AVG(follower_count) AS avg_follower_count FROM (SELECT follower_count FROM member ORDER BY follower_count DESC LIMIT 2) AS top2;`
![task](task4/task4-4.png)

# Task 5
### Create table 

`CREATE TABLE message(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    member_id INT UNSIGNED NOT NULL,
    content TEXT NOT NULL,
    like_count INT NOT NULL DEFAULT 0,
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES member (id)
);`

### Insert arbitrary data


`INSERT INTO message(member_id, content, like_count) VALUES (FLOOR(RAND() * 5) + 1, 'This is good!', FLOOR(RAND() * 10));`

`INSERT INTO message(member_id, content, like_count) VALUES (FLOOR(RAND() * 5) + 1, 'NICE!!!', FLOOR(RAND() * 10));`

`INSERT INTO message(member_id, content, like_count) VALUES (FLOOR(RAND() * 5) + 1, 'GOOD!!!', FLOOR(RAND() * 10));`

`INSERT INTO message(member_id, content, like_count) VALUES (FLOOR(RAND() * 5) + 1, 'So good!!!', FLOOR(RAND() * 10));`

`INSERT INTO message(member_id, content, like_count) VALUES (FLOOR(RAND() * 5) + 1, 'LOVE it!!!', FLOOR(RAND() * 10));`

`INSERT INTO message(member_id, content, like_count) VALUES (FLOOR(RAND() * 5) + 1, 'Omg bro!', FLOOR(RAND() * 10));`

`INSERT INTO message(member_id, content, like_count) VALUES (FLOOR(RAND() * 5) + 1, 'On fire!', FLOOR(RAND() * 10));`

`INSERT INTO message(member_id, content, like_count) VALUES (FLOOR(RAND() * 5) + 1, 'Kepp going!', FLOOR(RAND() * 10));`

`INSERT INTO message(member_id, content, like_count) VALUES (FLOOR(RAND() * 5) + 1, 'I knew you can do it!', FLOOR(RAND() * 10));`

`INSERT INTO message(member_id, content, like_count) VALUES (FLOOR(RAND() * 5) + 1, 'Good for you man!', FLOOR(RAND() * 10));`

`INSERT INTO message(member_id, content, like_count) VALUES (FLOOR(RAND() * 5) + 1, 'So proud of you!', FLOOR(RAND() * 10));`

`INSERT INTO message(member_id, content, like_count) VALUES (FLOOR(RAND() * 5) + 1, 'My idol!', FLOOR(RAND() * 10));`

`INSERT INTO message(member_id, content, like_count) VALUES (FLOOR(RAND() * 5) + 1, 'Excellent!', FLOOR(RAND() * 10));`

`INSERT INTO message(member_id, content, like_count) VALUES (FLOOR(RAND() * 5) + 1, "Let's do it!", FLOOR(RAND() * 10));`

`INSERT INTO message(member_id, content, like_count) VALUES (FLOOR(RAND() * 5) + 1, 'THE GOAT', FLOOR(RAND() * 10));`


1. SELECT all messages, including sender names. We have to JOIN the member table to get that.

`SELECT * FROM message JOIN member ON message.member_id = member.id;`
![task](task5/task5-1.png)

2. SELECT all messages, including sender names, where sender email equals to test@test.com. We have to JOIN the member table to filter and get that.

`SELECT * FROM message JOIN member ON message.member_id = member.id WHERE member.email = 'test@test.com';`
![task](task5/task5-2.png)

3. Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender email equals to test@test.com.

`SELECT AVG(like_count) FROM message JOIN member ON message.member_id = member.id WHERE member.email = 'test@test.com';`
![task](task5/task5-3.png)

4. Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender email.

`SELECT AVG(like_count), email FROM message JOIN member ON message.member_id = member.id GROUP BY email;`
![task](task5/task5-4.png)