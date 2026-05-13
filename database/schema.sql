-----------------------------------------------
-- A MySQL database and tables creation schema
-- Normalised to 3rd Normal Form (3NF)
-- Constraints are set for entering data validation
-- They are specified with names for easier debugging
-- ON DELETE CASCADE is used for automatic deletion of a record
-- Activates if a corresponding parent table record is deleted
-----------------------------------------------

-- Create and initialise the database
CREATE DATABASE IF NOT EXISTS School_Management_System;
USE School_Management_System;

-----------------------------------------------
-- 1. Base Tables with no foreign keys (FK) dependencies
-----------------------------------------------

-- PEOPLE: A future 'Parent' class in OOP structure
-- Contains personal details of all people existing in the system
CREATE TABLE People (
pers_id INT PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR (50) NOT NULL,
last_name VARCHAR (50) NOT NULL,
DoB DATE NOT NULL,
town VARCHAR(40) NOT NULL DEFAULT 'Astana', -- default value
address VARCHAR(50) NOT NULL,
phone VARCHAR(12) NOT NULL UNIQUE, -- no duplicates
email VARCHAR(100) NOT NULL UNIQUE, -- no duplicates
-- Constraints for names, date of birth, phone and email validation
CONSTRAINT check_first_name CHECK (CHAR_LENGTH(first_name)>=3),
CONSTRAINT check_last_name CHECK (CHAR_LENGTH(last_name)>=3),
CONSTRAINT check_dob CHECK (DoB >= '1945-01-01'),
CONSTRAINT check_phone CHECK (phone REGEXP '^\\+7[0-9]{10}$'),
CONSTRAINT check_email CHECK (email LIKE '%@%.%')
);

-----------------------------------------------
-- COURSES: A table containing courses IDs and names
-- IDs are not auto_increment-ed for more meaningful keys
-- e.g., not [1] but [001ALG]
CREATE TABLE Courses (
course_id VARCHAR(15) PRIMARY KEY,
course_name VARCHAR(50) NOT NULL,
-- Constraint for course_name
CONSTRAINT check_course_name CHECK (CHAR_LENGTH(course_name) >= 3)
);

-----------------------------------------------
-- ROOM_TYPES: A table for room types
-- e.g. 'Laboratory', 'Lecture' etc.
-- Separated from future 'Room' table for normalisation
CREATE TABLE Room_Types (
type_id INT PRIMARY KEY AUTO_INCREMENT,
type_name VARCHAR(30) NOT NULL,
-- Constraint for type_name
CONSTRAINT check_room_type_name CHECK (CHAR_LENGTH(type_name)>=4)
);

-----------------------------------------------
-- 2. Related Tables extending the People table
-----------------------------------------------

-- AUTHENTICATION: A table for login details (username, password)
-- FK pers_id references People table
CREATE TABLE Authentication (
auth_id INT PRIMARY KEY AUTO_INCREMENT,
pers_id INT NOT NULL UNIQUE, -- no duplicate people
username VARCHAR(30) NOT NULL UNIQUE, -- unique
password VARCHAR(255) NOT NULL,

FOREIGN KEY (pers_id) REFERENCES People(pers_id) ON DELETE CASCADE,
-- Constraints for username and password
CONSTRAINT check_username CHECK (CHAR_LENGTH(username) >= 5),
CONSTRAINT check_password CHECK (CHAR_LENGTH(password) >= 12)
);

-----------------------------------------------
-- ADMINISTRATION: A table for administration staff
-- FK pers_id references People table
CREATE TABLE Administration (
admin_id INT PRIMARY KEY AUTO_INCREMENT,
pers_id INT NOT NULL UNIQUE,

FOREIGN KEY (pers_id) REFERENCES People(pers_id) ON DELETE CASCADE
);

-----------------------------------------------
-- TEACHERS: A table for teachers
-- FK pers_id references People table
CREATE TABLE Teachers (
teacher_id INT PRIMARY KEY AUTO_INCREMENT,
pers_id INT NOT NULL UNIQUE,

FOREIGN KEY (pers_id) REFERENCES People(pers_id) ON DELETE CASCADE
);

-----------------------------------------------
-- STDUENTS: A table for students
-- FK pers_id references People table
CREATE TABLE Students (
stud_id INT PRIMARY KEY AUTO_INCREMENT,
pers_id INT NOT NULL UNIQUE,

FOREIGN KEY (pers_id) REFERENCES People(pers_id) ON DELETE CASCADE
);

-----------------------------------------------
-- 3. Related Tables
-----------------------------------------------
-- TEACHING: A table combining Teacher and Course tables
-- Defines which teacher is authorized to teach which course
CREATE TABLE Teaching (
teach_course_id INT PRIMARY KEY AUTO_INCREMENT,
teacher_id INT NOT NULL,
course_id VARCHAR(15) NOT NULL,

FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id),
FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-----------------------------------------------
-- REGISTRATION: A table combining Student and Teaching tables
-- Defines students' enrollment on different courses
CREATE TABLE Registration (
reg_id INT PRIMARY KEY AUTO_INCREMENT,
stud_id INT NOT NULL,
teach_course_id INT NOT NULL,
reg_date DATE NOT NULL DEFAULT (CURRENT_DATE),--default on current date

FOREIGN KEY (stud_id) REFERENCES Students(stud_id),
FOREIGN KEY (teach_course_id) REFERENCES Teaching(teach_course_id),
-- A constraint for ensuring student age is suitable for school
CONSTRAINT check_registration_date CHECK (reg_date >= '2000-09-01'),
UNIQUE (stud_id, teach_course_id) -- no duplicate registrations
);

-- ROOMS: A Room table using Room_Types (FK)
-- More detailed information about specific classrooms
CREATE TABLE Rooms (
room_id INT PRIMARY KEY AUTO_INCREMENT,
room_label VARCHAR(20) NOT NULL UNIQUE,
floor TINYINT NOT NULL DEFAULT 1,
capacity TINYINT NOT NULL DEFAULT 15,
type_id INT NOT NULL,

FOREIGN KEY (type_id) REFERENCES Room_Types(type_id),
-- Constraints for floor and capacity input validity
CONSTRAINT check_floor CHECK (floor BETWEEN 1 AND 5),
CONSTRAINT check_capacity CHECK (capacity BETWEEN 1 AND 200)
);

-----------------------------------------------
-- SCHEDULE: A table combining Teaching and Rooms tables
-- Represents a connection between Teaching and classroom and date
CREATE TABLE Schedule (
schedule_id INT PRIMARY KEY AUTO_INCREMENT,
teach_course_id INT NOT NULL,
room_id INT,
date_class DATE NOT NULL,

FOREIGN KEY (teach_course_id) REFERENCES Teaching(teach_course_id),
FOREIGN KEY (room_id) REFERENCES Rooms(room_id) ON DELETE SET NULL
);

-----------------------------------------------
-- ATTENDANCE: A table combining Schedule and Student tables
-- Connects schedule instances to students, tracks attendance (0/1/2)
CREATE TABLE Attendance (
attendance_id INT PRIMARY KEY AUTO_INCREMENT,
schedule_id INT NOT NULL,
stud_id INT NOT NULL,
status TINYINT NOT NULL,

FOREIGN KEY (schedule_id) REFERENCES Schedule(schedule_id),
FOREIGN KEY (stud_id) REFERENCES Students(stud_id),
-- 0 = absent, 1 = late, 2 = present
CONSTRAINT check_attendance_status CHECK (status IN (0,1,2)),
UNIQUE (schedule_id, stud_id) -- no duplicates
);

-----------------------------------------------
-- GRADES: A table assigning final grade value to a registration record
CREATE TABLE Grades (
grade_id INT PRIMARY KEY AUTO_INCREMENT,
reg_id INT NOT NULL UNIQUE,
final_grade DECIMAL(6,2),

FOREIGN KEY (reg_id) REFERENCES Registration(reg_id) ON DELETE CASCADE,
-- Constraint for grade value (0-100)
CONSTRAINT check_final_grade CHECK (final_grade BETWEEN 0 AND 100)
);

-----------------------------------------------
-- 4. Indexes: Search assistance
-- Optimises searching not based on IDs
-----------------------------------------------

CREATE INDEX index_people_names ON People(last_name, first_name);
CREATE INDEX index_course_name ON Courses(course_name);
CREATE INDEX index_schedule_date ON Schedule(date_class);
CREATE INDEX index_grade ON Grades(final_grade);
