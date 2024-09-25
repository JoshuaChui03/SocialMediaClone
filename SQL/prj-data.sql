PRAGMA foreign_keys=ON;

-- inserting into users table
-- insert into users values (113, 'admin', 'dsada', 'root@hahao.com', 'Edmonton', 3.0);
-- insert into users values (2232, 'admin', 'anna', 'root@hahao.com', 'Edmonton', 3.0);
-- insert into users values (33, 'admin', 'kama', 'root@hahao.com', 'Edmonton', 3.0);
-- insert into users values (234, 'admin', 'baba', 'root@hahao.com', 'Frankfurt', 3.0);
-- insert into users values (1234, 'admin', 'weweqwe', 'root@hahao.com', 'Calgary', 3.0);
-- insert into users values (34, 'admin', 'weewqwe', 'root@hahao.com', 'Edmonton', 3.0);
-- insert into users values (122134, 'admin', 'wqe', 'root@hahao.com', 'Edmonton', 3.0);
-- insert into users values (123434, 'admin', 'weewrwe', 'root@hahao.com', 'Edmonton', 3.0);
-- insert into users values (123242, 'admin', 'werwrwe', 'root@hahao.com', 'Manitiba', 3.0);
-- insert into users values (12354, 'admin', 'weqewqwe', 'root@hahao.com', 'Edmonton', 3.0);
-- insert into users values (12324, 'admin', 'weqweewe', 'root@hahao.com', 'Kuala Lumpur', 3.0);
-- insert into users values (1237, 'admin', 'weqwewe', 'root@hahao.com', 'Edmonton', 3.0);


-- --inserting into tweets tables
-- insert into tweets values (1, 113, '2012-05-03', 'today is a #great day hihi', NULL);
-- insert into tweets values (2, 113, '2012-02-03', 'now is a #great time hihi', NULL);
-- insert into tweets values (3, 113, '2012-07-03', 'what is a #chill day huh', 55);
-- insert into tweets values (4, 113, '2012-07-03', 'today is a #weary', NULL);
-- insert into tweets values (5, 113, '2012-03-03', 'today is a #great day hihi', NULL);
-- insert into tweets values (6, 113, '2012-02-03', 'today is a #great day hihi', NULL);
-- insert into tweets values (7, 113, '2012-06-03', 'today is a #great day hihi', 141);
-- insert into tweets values (9, 113, '2012-04-03', 'today is a #great day hihi', NULL);
-- insert into tweets values (55, 113, '2012-06-03', 'today is a #great day hihi', NULL);
-- insert into tweets values (24, 1234, '2017-07-03', 'today is a #great day hihi', NULL);
-- insert into tweets values (41, 113, '2017-03-03', 'today is a #great day hihi', NULL);
-- insert into tweets values (122, 113, '2017-06-03', 'today is a #great day hihi', NULL);
-- insert into tweets values (123, 113, '2016-07-03', 'today is a #great day hihi', 55);
-- insert into tweets values (134, 113, '2018-02-03', 'today is a #great day hihi', NULL);
-- insert into tweets values (165, 113, '2018-07-03', 'today is a #great day hihi', NULL);
-- insert into tweets values (557, 1234, '2018-02-03', 'today is a #great day hihi', NULL);
-- insert into tweets values (117, 113, '2018-01-03', 'today is a #great day hihi', NULL);
-- insert into tweets values (128, 113, '2016-12-03', 'today is a #great day hihi', NULL);
-- insert into tweets values (139, 113, '2011-11-03', 'today is a #great day hihi', 141);
-- insert into tweets values (1312, 113, '2014-11-03', 'today is a #great day hihi', NULL);
-- insert into tweets values (1141, 113, '2012-12-03', 'today is a #great day hihi', 141);
-- insert into tweets values (1343, 113, '2014-12-03', 'today is a #great day hihi', 141);


-- Insert data into the "users" table
INSERT INTO users (usr, pwd, name, email, city, timezone)
VALUES
(1, 'password1', 'John Doe', 'john.doe@example.com', 'New York', -5.0),
(2, 'mypassword', 'Alice Smith', 'alice.smith@example.com', 'Los Angeles', -8.0),
(3, 'securepass', 'Bob Johnson', 'bob.johnson@example.com', 'Chicago', -6.0),
(4, 'password123', 'Eva Brown', 'eva.brown@example.com', 'Houston', -6.0),
(5, 'pass1234', 'David Lee', 'david.lee@example.com', 'Miami', -5.0),
(6, 'qwerty123', 'Sarah Wilson', 'sarah.wilson@example.com', 'San Francisco', -8.0),
(7, 'letmein', 'Michael Davis', 'michael.davis@example.com', 'Seattle', -8.0),
(8, '123456', 'Emily White', 'emily.white@example.com', 'Boston', -5.0),
(9, 'passw0rd', 'Daniel Green', 'daniel.green@example.com', 'Dallas', -6.0),
(10, 'abcdef', 'Olivia Taylor', 'olivia.taylor@example.com', 'Atlanta', -5.0),
(11, 'p@$$w0rd', 'James Johnson', 'james.johnson@example.com', 'Chicago', -6.0),
(12, 'sunshine', 'Sophia Miller', 'sophia.miller@example.com', 'Los Angeles', -8.0),
(13, 'iloveyou', 'William Anderson', 'william.anderson@example.com', 'Denver', -7.0),
(14, 'welcome', 'Ava Harris', 'ava.harris@example.com', 'Miami', -5.0),
(15, '123abc', 'Liam Martinez', 'liam.martinez@example.com', 'New York', -5.0),
(16, 'admin123', 'Mia Thomas', 'mia.thomas@example.com', 'Houston', -6.0),
(17, 'password456', 'Ethan Lewis', 'ethan.lewis@example.com', 'San Diego', -8.0),
(18, 'letmein123', 'Chloe Clark', 'chloe.clark@example.com', 'Phoenix', -7.0),
(19, 'secure123', 'Harper Walker', 'harper.walker@example.com', 'San Antonio', -6.0),
(20, '1234abcd', 'Liam Scott', 'liam.scott@example.com', 'Philadelphia', -5.0);


-- Insert data into the "tweets" table
INSERT INTO tweets (tid, writer, tdate, text, replyto)
VALUES
(1, 1, '2023-10-28', 'Hello, Twitter! #FirstTweet', NULL),
(2, 2, '2023-10-29', 'Enjoying the sunny weather in LA. #Sunshine', NULL),
(3, 3, '2023-10-30', 'Chicago is a beautiful city! #CityLife', 1),
(4, 4, '2023-10-31', 'Houston, we have a problem. #Space', 2),
(5, 5, '2023-11-01', 'Miami nights are always amazing. #Nightlife', 1),
(6, 6, '2023-11-02', 'Just had the best coffee in SF. #CoffeeLovers', 2),
(7, 7, '2023-11-03', 'Seattle rain, as usual. #RainyDays', 3),
(8, 8, '2023-11-04', 'Boston is my new home! #NewBeginnings', NULL),
(9, 9, '2023-11-05', 'Dallas Cowboys are the best! #Football', 4),
(10, 10, '2023-11-06', 'Atlanta, here I come! #Travel', 5),
(11, 11, '2023-11-07', 'Winter in Chicago is cold! #WinterIsComing', 6),
(12, 12, '2023-11-08', 'LA traffic is crazy. #TrafficJam', NULL),
(13, 13, '2023-11-09', 'Denver Broncos for the win! #Sports', 8),
(14, 14, '2023-11-10', 'Miami''s beaches are a paradise. #BeachLife', NULL),
(15, 15, '2023-11-11', 'New York, the city that never sleeps. #NYC', 7),
(16, 16, '2023-11-12', 'Houston, we have a solution! #ProblemSolved', 2),
(17, 17, '2023-11-13', 'Phoenix sunsets are breathtaking. #SunsetViews', 11),
(18, 18, '2023-11-14', 'San Antonio''s fiestas are the best. #FiestaTime', 13),
(19, 19, '2023-11-15', 'Philadelphia Freedom! #LibertyBell', 12),
(20, 20, '2023-11-16', 'Las Vegas, a city of lights. #LasVegas', 8);
