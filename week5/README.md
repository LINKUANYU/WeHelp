# Task 2
CREATE TABLE member(
  id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  follower_count INT NOT NULL DEFAULT 0,
  time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

![task](task2.png)


# Task 3
INSERT INTO member (name, email, password) VALUES ('test', 'test@test.com', 'test');
INSERT INTO member (name, email, password) VALUES ('monday', 'monday@test.com', 'monday');
INSERT INTO member (name, email, password) VALUES ('tuesday', 'tuesday@test.com', 'tuesday');
INSERT INTO member (name, email, password) VALUES ('wednesday', 'wednesday@test.com', 'wednesday');
INSERT INTO member (name, email, password) VALUES ('thursday', 'thursday@test.com', 'thursday');
![task](task3-1.png)
SELECT * FROM member;
![task](task3-2.png)
SELECT * FROM member ORDER BY time DESC;
![task](task3-3.png)
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
![task](task3-4.png)
SELECT * FROM member WHERE email = 'test@test.com';
![task](task3-5.png)
SELECT * FROM member WHERE name LIKE '%es%';
![task](task3-6.png)
SELECT * FROM member WHERE email = 'test@test.com' AND password = 'test';
![task](task3-7.png)
UPDATE member SET name = 'test2' WHERE email = 'test@test.com';
![task](task3-8.png)

# Task 4
SELECT COUNT(*) FROM member;
![task](task4-1.png)
UPDATE member SET follower_count = FLOOR(RAND() * 100) WHERE id BETWEEN 1 AND 5;

SELECT SUM(follower_count) FROM member;
![task](task4-2.png)
SELECT AVG(follower_count) FROM member;
![task](task4-3.png)
SELECT AVG(follower_count) AS avg_follower_count FROM (SELECT follower_count FROM member ORDER BY follower_count DESC LIMIT 2) AS top2;
![task](task4-4.png)