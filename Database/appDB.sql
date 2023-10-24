
Use appdb;

-- Create the User Role Entity
CREATE TABLE UserRole (
    UserRoleID INT NOT NULL,
    RoleName VARCHAR(30) NOT NULL,
    PRIMARY KEY (UserRoleID)
);

-- Create the User Entity
CREATE TABLE User (
    UserID INT NOT NULL,
    UserRoleID INT NOT NULL,
    Username VARCHAR(30) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    FirstName VARCHAR(30) NOT NULL,
    LastName VARCHAR(30) NOT NULL,
    Phone VARCHAR(15),
    PRIMARY KEY (UserID),
    FOREIGN KEY (UserRoleID) REFERENCES UserRole(UserRoleID)
);

-- Create the Bookable Area Entity
CREATE TABLE BookableArea (
    AreaID INT NOT NULL,
    AreaName VARCHAR(30) NOT NULL,
    Location VARCHAR(255) NOT NULL,
    Capacity INT NOT NULL,
    PRIMARY KEY (AreaID)
);

-- Create the Event Entity
CREATE TABLE Event (
    EventID INT NOT NULL,
    EventName VARCHAR(30) NOT NULL,
    EventDate DATETIME NOT NULL,
    EventType VARCHAR(20) NOT NULL,
    EventCategory VARCHAR(30) NOT NULL,
    Description TEXT NOT NULL,
    PRIMARY KEY (EventID)
);

-- Create the Availability Entity
CREATE TABLE Availability (
    AvailabilityID INT NOT NULL,
    AreaID INT NOT NULL,
    StartDateTime DATETIME NOT NULL,
    EndDateTime DATETIME NOT NULL,
    IsAvailable BOOLEAN NOT NULL DEFAULT 1,
    PRIMARY KEY (AvailabilityID),
    FOREIGN KEY (AreaID) REFERENCES BookableArea(AreaID)
);

-- Create the Booking Entity
CREATE TABLE Booking (
    BookingID INT NOT NULL,
    UserID INT NOT NULL,
    EventID INT NOT NULL,
    AreaID INT NOT NULL,
    StartDateTime DATETIME NOT NULL,
    EndDateTime DATETIME NOT NULL,
    PRIMARY KEY (BookingID),
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (EventID) REFERENCES Event(EventID),
    FOREIGN KEY (AreaID) REFERENCES BookableArea(AreaID)
);

-- Insert data into User Role
INSERT INTO UserRole (UserRoleID, RoleName)
VALUES
    (1, 'Admin'),
    (2, 'User');
    
-- Insert data into User
INSERT INTO User (UserID, UserRoleID, Username, Password, Email, FirstName, LastName, Phone)
VALUES
    (10, 1, 'admin1', 'adminpass', 'admin1@email.com', 'Admin', 'Smith', '987-654-3210'),
    (12, 2, 'user1', 'password1', 'user1@email.com', 'John', 'Doe', '123-456-7890'),
    (13, 2, 'user2', 'password2', 'user2@email.com', 'Alice', 'Johnson', '555-123-4567'),
    (14, 2, 'user3', 'password3', 'user3@email.com', 'Emma', 'Wilson', '111-222-3333'),
    (15, 2, 'user4', 'password4', 'user4@email.com', 'Liam', 'Brown', '444-555-6666');

-- Insert data into Bookable Area
INSERT INTO BookableArea (AreaID, AreaName, Location, Capacity)
VALUES
    (21, 'Open Play Area', 'Zone 1', 50),
    (22, 'Tennis Court', 'Zone 2', 80),
    (23, 'Basketball Court', 'Zone 3', 80),
    (24, 'Backstop Ball Diamond', 'Zone 4', 80),
    (25, 'Tennis Wall', 'Zone 5', 2),
    (26, 'Outdoor Volleyball Courts 2', 'Zone 6', 12),
    (27, 'Splash Pad', 'Zone 7', 15),
    (28, 'Walking and Running Trail', 'Zone 8', 300),
    (29, 'Pavilion1', 'Zone 9', 30),
    (30, 'Pavillion2', 'Zone 11', 350),
    (31, 'Pavillion3', 'Zone 12', 150),
    (32, 'Outdoor Pool', 'Zone 13', 10);

-- Insert data into Event
INSERT INTO Event (EventID, EventName, EventDate, EventType, EventCategory, Description)
VALUES
    (1002, 'Tech Conference', '2023-10-15 09:00:00', 'Featured', 'Tech', 'A conference about the latest technology trends.'),
    (1150, 'Team Building Workshop', '2023-11-20 14:00:00', 'User Booking', 'Team Building', 'A workshop for team-building exercises.'),
    (3589, 'Music Festival', '2023-12-05 17:00:00', 'Featured', 'Music', 'A music festival with various artists.'),
    (4268, 'Basketball Tournament', '2024-01-20 10:00:00', 'Featured', 'Sports', 'A tournament for basketball enthusiasts.'),
    (2747, 'Open Play', '2024-02-10 11:00:00', 'User Booking', 'Recreation', 'Open play for families and kids.'),
    (2576, 'Tennis Clinic', '2024-03-15 15:30:00', 'User Booking', 'Sports', 'Tennis clinic for all skill levels.'),
    (3587, 'Picnic Day', '2024-04-25 12:00:00', 'User Booking', 'Recreation', 'A day for picnicking and outdoor fun.');

-- Insert data into Booking
INSERT INTO Booking (BookingID, UserID, EventID, AreaID, StartDateTime, EndDateTime)
VALUES
    (501, 10, 1002, 31, '2023-10-15 09:00:00', '2023-10-15 17:00:00'), -- Admin1 books Pavillion3 for Tech Conference
    (502, 12, 1150, 29, '2023-11-20 14:00:00', '2023-11-20 16:00:00'), -- User1 books Pavillion1 for Team Building Workshop
    (503, 13, 3589, 30, '2023-12-05 17:00:00', '2023-12-05 23:00:00'), -- User2 books Pavillion2 for Music Festival
    (504, 10, 4268, 23, '2024-01-20 10:00:00', '2024-01-20 18:00:00'), -- Admin1 books Basketball Court for Basketball Tournament
    (505, 12, 2747, 25, '2024-02-10 11:00:00', '2024-02-10 14:00:00'), -- User1 books Tennis Wall for Open Play
    (506, 13, 2576, 26, '2024-03-15 15:30:00', '2024-03-15 17:30:00'), -- User2 books Outdoor Volleyball Courts 2 for Tennis Clinic
    (507, 14, 3587, 27, '2024-04-25 12:00:00', '2024-04-25 14:00:00'); -- User3 books Splash Pad for Picnic Day

-- Insert data into Availability
INSERT INTO Availability (AvailabilityID, AreaID, StartDateTime, EndDateTime, IsAvailable)
VALUES
    (101, 31, '2023-10-15 09:00:00', '2023-10-15 17:00:00', 0), -- Pavillion3 is not available during Tech Conference
    (102, 29, '2023-11-20 14:00:00', '2023-11-20 16:00:00', 0), -- Pavillion1 is not available during Team Building Workshop
    (103, 30, '2023-12-05 17:00:00', '2023-12-05 23:00:00', 0), -- Pavillion2 is not available during Music Festival
    (104, 23, '2024-01-20 10:00:00', '2024-01-20 18:00:00', 0), -- Basketbal Court is not available during Basketball Tournament
    (105, 25, '2024-02-10 11:00:00', '2024-02-10 14:00:00', 0), -- Tennis Wall is not available during Open Play
    (106, 26, '2024-03-15 15:30:00', '2024-03-15 17:30:00', 0), -- Outdoor Volleyball Courts 2 are not available during Tennis Clinic
    (107, 27, '2024-04-25 12:00:00', '2024-04-25 14:00:00', 0); -- Splash Pad is not available during Picnic Day

select * from BookableArea;