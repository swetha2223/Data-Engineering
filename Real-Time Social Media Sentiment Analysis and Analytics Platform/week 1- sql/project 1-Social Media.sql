create database Project_1

use project_1

-- User Dimension Table
CREATE TABLE user_data (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(255),
    location VARCHAR(255),
    date_joined DATE
);

-- Create post_fact table 
CREATE TABLE post_fact (
    post_id INT PRIMARY KEY,
    user_id INT,
    post_text VARCHAR(500),
    post_date DATETIME2, 
    sentiment_score DECIMAL(3, 2), 
    platform VARCHAR(50) 
);



-- Sentiment Dimension Table (Optional, for categorizing sentiment)
CREATE TABLE sentiment_dim (
    sentiment_id INT PRIMARY KEY,
    sentiment_label VARCHAR(50), -- Positive, Negative, Neutral
    sentiment_score DECIMAL(3, 2)
);


INSERT INTO user_data (user_id, user_name, location, date_joined)
VALUES
(1, 'Aarav', 'Mumbai', '2024-01-15'),
(2, 'Priya', 'Bangalore', '2024-02-05'),
(3, 'Rahul', 'Delhi', '2024-03-10'),
(4, 'Sneha', 'Chennai', '2024-04-22'),
(5, 'Ravi', 'Hyderabad', '2024-05-11');


-- Inserting sample posts with specific post_date values
INSERT INTO post_fact (post_id, user_id, post_text, post_date, sentiment_score, platform)
VALUES
(101, 1, 'Excited about the new festival!', '2024-06-10 09:15:00', 0.9, 'Twitter'),
(102, 2, 'Not satisfied with the current services.', '2024-06-10 11:30:00', -0.7, 'Facebook'),
(103, 1, 'Attended an amazing cultural event!', '2024-06-11 14:45:00', 0.8, 'Instagram'),
(104, 3, 'Traffic is so frustrating today.', '2024-06-12 08:20:00', -0.5, 'Twitter'),
(105, 4, 'Had a great dinner with family!', '2024-06-12 19:00:00', 0.7, 'Facebook'),
(106, 5, 'The new software update is not working well.', '2024-06-13 10:10:00', -0.6, 'Instagram'),
(107, 2, 'Looking forward to the weekend fun!', '2024-06-14 17:25:00', 0.5, 'Twitter'),
(108, 3, 'Shocked by today’s news.', '2024-06-15 12:45:00', -0.8, 'Facebook'),
(109, 1, 'Perfect weather for a long drive!', '2024-06-15 09:30:00', 0.6, 'Instagram'),
(110, 5, 'Feeling neutral about today’s tasks.', '2024-06-16 14:00:00', 0.0, 'Twitter');


-- Inserting sentiment categories (optional)
INSERT INTO sentiment_dim (sentiment_id, sentiment_label, sentiment_score)
VALUES
(1, 'Positive', 1.0),
(2, 'Neutral', 0.0),
(3, 'Negative', -1.0);

-- Some Querry

---To calculate average sentiment per day:--
SELECT CONVERT(DATE, post_date) AS post_day, 
       AVG(sentiment_score) AS avg_sentiment
FROM post_fact
GROUP BY CONVERT(DATE, post_date)
ORDER BY post_day;

---To retrieve the users who posted the most:

SELECT TOP 10 u.user_name, COUNT(p.post_id) AS total_posts
FROM user_data u
JOIN post_fact p ON u.user_id = p.user_id
GROUP BY u.user_name
ORDER BY total_posts DESC;

---To track how sentiment varies across social media platforms:

SELECT platform, 
       COUNT(CASE WHEN sentiment_score > 0 THEN 1 END) AS positive_posts,
       COUNT(CASE WHEN sentiment_score < 0 THEN 1 END) AS negative_posts,
       COUNT(CASE WHEN sentiment_score = 0 THEN 1 END) AS neutral_posts
FROM post_fact
GROUP BY platform;

---To calculate the percentage of positive and negative sentiment over time:


SELECT CONVERT(DATE, post_date) AS post_day,
       (SUM(CASE WHEN sentiment_score > 0 THEN 1 ELSE 0 END) * 100.0) / COUNT(*) AS positive_percentage,
       (SUM(CASE WHEN sentiment_score < 0 THEN 1 ELSE 0 END) * 100.0) / COUNT(*) AS negative_percentage
FROM post_fact
GROUP BY CONVERT(DATE, post_date)
ORDER BY post_day;






