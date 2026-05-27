-----------------------------------------------
-- ADDING: Stored procedures dedicated to adding new records
-- Procedures accept IN parameters
-- In complex tables additional checks are performed to ensure
-- correctness of addition
-----------------------------------------------

DELIMITER //

-- Addition in People table is followed by linking the new
-- record with Student/Teacher/Administration tables on newly
-- auto_incremented pers_id (SET @new_id = LAST_INSERT_ID();)
-- Authentication data (username, password) is added immediately
-- to avoid unauthenticated people
CREATE PROCEDURE `add_student` (
IN f_name VARCHAR(50),
IN l_name VARCHAR(50),
IN dob DATE,
IN e_town VARCHAR(40),
IN e_address VARCHAR(50),
IN e_phone VARCHAR(12),
IN e_email VARCHAR(100),
IN e_username VARCHAR(30),
IN e_password VARCHAR(255)
)
BEGIN
    INSERT INTO People
    (first_name, last_name, DoB, town, address, phone, email)
    VALUES (f_name, l_name, dob, e_town, e_address, e_phone, e_email);

    SET @new_id = LAST_INSERT_ID();

    INSERT INTO Students (pers_id)
    VALUES (@new_id);

    INSERT INTO Authentication (pers_id, username, password)
    VALUES (@new_id, e_username, e_password);
END //
-----------------------

CREATE PROCEDURE `add_teacher` (
IN f_name VARCHAR(50),
IN l_name VARCHAR(50),
IN dob DATE,
IN e_town VARCHAR(40),
IN e_address VARCHAR(50),
IN e_phone VARCHAR(12),
IN e_email VARCHAR(100),
IN e_username VARCHAR(30),
IN e_password VARCHAR(255)
)
BEGIN
    INSERT INTO People
    (first_name, last_name, DoB, town, address, phone, email)
    VALUES (f_name, l_name, dob, e_town, e_address, e_phone, e_email);

    SET @new_id = LAST_INSERT_ID();

    INSERT INTO Teachers (pers_id)
    VALUES (@new_id);

    INSERT INTO Authentication (pers_id, username, password)
    VALUES (@new_id, e_username, e_password);
END //
-----------------------

CREATE PROCEDURE `add_admin` (
IN f_name VARCHAR(50),
IN l_name VARCHAR(50),
IN dob DATE,
IN e_town VARCHAR(40),
IN e_address VARCHAR(50),
IN e_phone VARCHAR(12),
IN e_email VARCHAR(100),
IN e_username VARCHAR(30),
IN e_password VARCHAR(255)
)
BEGIN
    INSERT INTO People
    (first_name, last_name, DoB, town, address, phone, email)
    VALUES (f_name, l_name, dob, e_town, e_address, e_phone, e_email);

    SET @new_id = LAST_INSERT_ID();

    INSERT INTO Administration (pers_id)
    VALUES (@new_id);

    INSERT INTO Authentication (pers_id, username, password)
    VALUES (@new_id, e_username, e_password);
END //
-----------------------------------------------
-- Easy additions with no/little joins

CREATE PROCEDURE `add_course` (
IN c_id VARCHAR(15),
IN c_name VARCHAR(50)
)
BEGIN
    INSERT INTO Courses (course_id, course_name)
    VALUES (c_id, c_name);
END //
-----------------------

CREATE PROCEDURE `add_teaching` (
IN t_id INT,
IN c_id VARCHAR(15)
)
BEGIN
    INSERT INTO Teaching (teacher_id, course_id)
    VALUES (t_id, c_id);
END //
-----------------------

CREATE PROCEDURE `add_room_type` (
IN t_name VARCHAR(30)
)
BEGIN
    INSERT INTO Room_Types (type_name)
    VALUES (t_name);
END //
-----------------------

CREATE PROCEDURE `add_room` (
IN label VARCHAR(20),
IN floor TINYINT,
IN capacity TINYINT,
IN type_id INT
)
BEGIN
    INSERT INTO Rooms (room_label, floor, capacity, type_id)
    VALUES (label, floor, capacity, type_id);
END //
-----------------------------------------------
-- Complex addition with the necessity to
-- validate other records existence before proceeding
-- Handled with "IF NOT EXISTS...." and error signalling for
-- user-friendly error messages "SIGNAL SQLSTATE...SET MESSAGE_TEXT..."

CREATE PROCEDURE `add_registration` (
IN s_id INT,
IN tc_id INT
)
BEGIN
    -- check before assigning students to teaching combinations
    IF NOT EXISTS (SELECT 1 FROM Students WHERE stud_id = s_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Student ID not found.';

    ELSEIF NOT EXISTS
    (SELECT 1 FROM Teaching WHERE teach_course_id = tc_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Teaching assignment ID not found.';
    ELSE
        INSERT INTO Registration (stud_id, teach_course_id)
        VALUES (s_id, tc_id);
    END IF;
END //
-----------------------

CREATE PROCEDURE `add_schedule` (
IN tc_id INT,
IN room_id INT,
IN class_date DATE
)
BEGIN
    -- check before assigning teaching combinations to rooms
    IF NOT EXISTS
    (SELECT 1 FROM Teaching WHERE teach_course_id = tc_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Teaching ID not found.';

    ELSEIF NOT EXISTS
    (SELECT 1 FROM Rooms WHERE room_id = room_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Room ID not found.';
    ELSE
        INSERT INTO Schedule (teach_course_id, room_id, date_class)
        VALUES (tc_id, room_id, class_date);
    END IF;
END //
-----------------------

CREATE PROCEDURE `add_attendance` (
IN sch_id INT,
IN s_id INT,
IN a_status TINYINT
)
BEGIN
    -- check if students are registered for the course
    -- before assigning attendance
    DECLARE target_teach_id INT;
    SELECT teach_course_id INTO target_teach_id
    FROM Schedule
    WHERE schedule_id = sch_id;

    IF EXISTS (
        SELECT 1 FROM Registration
        WHERE stud_id = s_id AND teach_course_id = target_teach_id
    ) THEN
        INSERT INTO Attendance (schedule_id, stud_id, status)
        VALUES (sch_id, s_id, a_status);
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT =
        'Error: Student is not registered for this course.';
    END IF;
END //
-----------------------

CREATE PROCEDURE `add_grade` (
IN r_id INT,
IN f_gr DECIMAL(6,2)
)
BEGIN
    -- check before assigning grades to students (registration records)
    IF NOT EXISTS (SELECT 1 FROM Registration WHERE reg_id = r_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Registration ID not found.';
    ELSE
        INSERT INTO Grades (reg_id, final_grade) VALUES (r_id, f_gr);
    END IF;
END //

DELIMITER ;