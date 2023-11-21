-- Use this file to populate the database
-- This should be done after running makemigrations and migrate.

Use appdb;

-- Insert data into User
INSERT INTO auth_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, last_login)
VALUES
    ('admin', 1, 'admin', 'Admin', 'User', 'admin@example.com', 1, 1, '2023-10-26 10:00:00', '2023-10-26 10:00:00'),
    ('password1', 0, 'user1', 'John', 'Doe', 'john.doe@example.com', 0, 1, '2023-10-26 10:05:00', '2023-10-26 10:05:00'),
    ('password2', 0, 'user2', 'Jane', 'Smith', 'jane.smith@example.com', 0, 1, '2023-10-26 10:10:00', '2023-10-26 10:10:00'),
    ('password3', 0, 'user3', 'Alice', 'Johnson', 'alice.johnson@example.com', 0, 1, '2023-10-26 10:15:00', '2023-10-26 10:15:00'),
    ('password4', 0, 'user4', 'Bob', 'Williams', 'bob.williams@example.com', 0, 1, '2023-10-26 10:20:00', '2023-10-26 10:20:00'),
    ('password5', 0, 'user5', 'Eva', 'Brown', 'eva.brown@example.com', 0, 1, '2023-10-26 10:25:00', '2023-10-26 10:25:00');

-- Insert data into Bookable Area
INSERT INTO Area (name, location, capacity)
VALUES
    ('Open Play Area', 'Zone 1', 50), -- AreaId = 1
    ('Tennis Court', 'Zone 2', 80), -- AreaId = 2
    ('Basketball Court', 'Zone 3', 80), -- AreaId = 3
    ('Backstop Ball Diamond', 'Zone 4', 80), -- AreaId = 4
    ('Tennis Wall', 'Zone 5', 2), -- AreaId = 5
    ('Outdoor Volleyball Courts 2', 'Zone 6', 12), -- AreaId = 6
    ('Splash Pad', 'Zone 7', 15), -- AreaId = 7
    ('Walking and Running Trail', 'Zone 8', 300), -- AreaId = 8
    ('Pavilion 1', 'Zone 9', 30), -- AreaId = 9
    ('Pavilion 2', 'Zone 11', 350), -- AreaId = 10
    ('Pavilion 3', 'Zone 12', 150), -- AreaId = 11
    ('Outdoor Pool', 'Zone 13', 10); -- AreaId = 12

-- Insert data into Event
INSERT INTO Event (name, date, is_public, category, description)
VALUES
    ('Tech Conference', '2023-10-15 09:00:00', 1, 'Tech', 'A conference about the latest technology trends.'), -- EventId = 1
    ('Team Building Workshop', '2023-11-20 14:00:00', 0, 'Team Building', 'A workshop for team-building exercises.'), -- EventId = 2
    ('Music Festival', '2023-12-05 17:00:00', 1, 'Music', 'A music festival with various artists.'), -- EventId = 3
    ('Basketball Tournament', '2024-01-20 10:00:00', 1, 'Sports', 'A tournament for basketball enthusiasts.'), -- EventId = 4
    ('Open Play', '2024-02-10 11:00:00', 0, 'Recreation', 'Open play for families and kids.'), -- EventId = 5
    ('Tennis Clinic', '2024-03-15 15:30:00', 0, 'Sports', 'Tennis clinic for all skill levels.'), -- EventId = 6
    ('Picnic Day', '2024-04-25 12:00:00', 0, 'Recreation', 'A day for picnicking and outdoor fun.'); -- EventId = 7

-- Insert data into Booking
INSERT INTO Booking (user_id, event_id, area_id, start_time, end_time, attendance, status)
VALUES
    (1, 1, 11, '2023-10-15 09:00:00', '2023-10-15 17:00:00', 125, 'Approved'), -- Admin books Pavillion 3 for Tech Conference
    (2, 2, 9, '2023-11-20 14:00:00', '2023-11-20 16:00:00', 27, 'Approved'), -- User1 books Pavillion 1 for Team Building Workshop
    (3, 3, 10, '2023-12-05 17:00:00', '2023-12-05 23:00:00', 320, 'Approved'), -- User2 books Pavillion 2 for Music Festival
    (1, 4, 3, '2024-01-20 10:00:00', '2024-01-20 18:00:00', 65, 'Approved'), -- Admin books Basketball Court for Basketball Tournament
    (2, 5, 5, '2024-02-10 11:00:00', '2024-02-10 14:00:00', 2, 'Approved'), -- User1 books Tennis Wall for Open Play
    (3, 6, 6, '2024-03-15 15:30:00', '2024-03-15 17:30:00', 12, 'Approved'), -- User2 books Outdoor Volleyball Courts 2 for Tennis Clinic
    (4, 7, 7, '2024-04-25 12:00:00', '2024-04-25 14:00:00', 10, 'Approved'); -- User3 books Splash Pad for Picnic Day