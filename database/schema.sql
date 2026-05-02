CREATE database School_Management_System;
USE School_Management_System;

-- Base Tables --

CREATE TABLE People (
pers_id INT PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR (50) NOT NULL,
last_name VARCHAR (50) NOT NULL,
DoB DATE NOT NULL,
town VARCHAR(40) NOT NULL DEFAULT 'Astana',
address VARCHAR(50) NOT NULL,
phone VARCHAR(12) NOT NULL UNIQUE,
email VARCHAR(100) NOT NULL UNIQUE,

CONSTRAINT check_first_name CHECK (CHAR_LENGTH(first_name)>=3),
CONSTRAINT check_last_name CHECK (CHAR_LENGTH(last_name)>=3),
CONSTRAINT check_dob CHECK (DoB >= '1945-01-01'),
CONSTRAINT check_phone CHECK (phone REGEXP '^\\+7[0-9]{10}$'),
CONSTRAINT check_email CHECK (email LIKE '%@%.%')
);

CREATE TABLE Courses (
course_id VARCHAR(15) PRIMARY KEY,
course_name VARCHAR(50) NOT NULL,

CONSTRAINT check_course_name CHECK (CHAR_LENGTH(course_name) >= 3)
);

CREATE TABLE Room_Types (
type_id INT PRIMARY KEY AUTO_INCREMENT,
type_name VARCHAR(30) NOT NULL,

CONSTRAINT check_room_type_name CHECK (CHAR_LENGTH(type_name)>=4)
);

-- Related Tables --

-- People --
CREATE TABLE Authentication (
auth_id INT PRIMARY KEY AUTO_INCREMENT,
pers_id INT NOT NULL UNIQUE,
username VARCHAR(30) NOT NULL UNIQUE,
password VARCHAR(255) NOT NULL,

FOREIGN KEY (pers_id) REFERENCES People(pers_id) ON DELETE CASCADE,
CONSTRAINT check_username CHECK (CHAR_LENGTH(username) >= 5),
CONSTRAINT check_password CHECK (CHAR_LENGTH(password) >= 12)
);

CREATE TABLE Administration (
admin_id INT PRIMARY KEY AUTO_INCREMENT,
pers_id INT NOT NULL UNIQUE,

FOREIGN KEY (pers_id) REFERENCES People(pers_id) ON DELETE CASCADE
);

CREATE TABLE Teachers (
teacher_id INT PRIMARY KEY AUTO_INCREMENT,
pers_id INT NOT NULL UNIQUE,

FOREIGN KEY (pers_id) REFERENCES People(pers_id) ON DELETE CASCADE
);

CREATE TABLE Students (
stud_id INT PRIMARY KEY AUTO_INCREMENT,
pers_id INT NOT NULL UNIQUE,

FOREIGN KEY (pers_id) REFERENCES People(pers_id) ON DELETE CASCADE
);
-- Teacher and Course --

CREATE TABLE Teaching (
teach_course_id INT PRIMARY KEY AUTO_INCREMENT,
teacher_id INT NOT NULL,
course_id VARCHAR(15) NOT NULL,

FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id),
FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Student and Teacher+Course --

CREATE TABLE Registration (
reg_id INT PRIMARY KEY AUTO_INCREMENT,
stud_id INT NOT NULL,
teach_course_id INT NOT NULL,
reg_date DATE NOT NULL DEFAULT (CURRENT_DATE),

FOREIGN KEY (stud_id) REFERENCES Students(stud_id),
FOREIGN KEY (teach_course_id) REFERENCES Teaching(teach_course_id),
CONSTRAINT check_registration_date CHECK (reg_date >= '2000-09-01'),
UNIQUE (stud_id, teach_course_id)
);

-- Further Tables --

CREATE TABLE Rooms (
room_id INT PRIMARY KEY AUTO_INCREMENT,
room_label VARCHAR(20) NOT NULL UNIQUE,
floor TINYINT NOT NULL DEFAULT 1,
capacity TINYINT NOT NULL DEFAULT 15,
type_id INT NOT NULL,

FOREIGN KEY (type_id) REFERENCES Room_Types(type_id),

CONSTRAINT check_floor CHECK (floor BETWEEN 1 AND 5),
CONSTRAINT check_capacity CHECK (capacity BETWEEN 1 AND 200)
);

CREATE TABLE Schedule (
schedule_id INT PRIMARY KEY AUTO_INCREMENT,
teach_course_id INT NOT NULL,
room_id INT,
date_class DATE NOT NULL,

FOREIGN KEY (teach_course_id) REFERENCES Teaching(teach_course_id),
FOREIGN KEY (room_id) REFERENCES Rooms(room_id) ON DELETE SET NULL
);

CREATE TABLE Attendance (
attendance_id INT PRIMARY KEY AUTO_INCREMENT,
schedule_id INT NOT NULL,
stud_id INT NOT NULL,
status TINYINT NOT NULL,

FOREIGN KEY (schedule_id) REFERENCES Schedule(schedule_id),
FOREIGN KEY (stud_id) REFERENCES Students(stud_id),
CONSTRAINT check_attendance_status CHECK (status IN (0,1,2)),
-- 0 = absent, 1 = late, 2 = present --
UNIQUE (schedule_id, stud_id)
);

CREATE TABLE Grades (
grade_id INT PRIMARY KEY AUTO_INCREMENT,
reg_id INT NOT NULL UNIQUE,
final_grade DECIMAL(6,2),

FOREIGN KEY (reg_id) REFERENCES Registration(reg_id) ON DELETE CASCADE,
CONSTRAINT check_final_grade CHECK (final_grade BETWEEN 0 AND 100)
);

-- Indexes --

CREATE INDEX index_people_names ON People(last_name, first_name);
CREATE INDEX index_course_name ON Courses(course_name);
CREATE INDEX index_schedule_date ON Schedule(date_class);
CREATE INDEX index_grade ON Grades(final_grade);
