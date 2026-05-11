DELIMITER //

-- ADDING

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


CREATE PROCEDURE `add_course` (
IN c_id VARCHAR(15),
IN c_name VARCHAR(50)
)
BEGIN
    INSERT INTO Courses (course_id, course_name)
    VALUES (c_id, c_name);
END //


CREATE PROCEDURE `add_teaching` (
IN t_id INT,
IN c_id VARCHAR(15)
)
BEGIN
    INSERT INTO Teaching (teacher_id, course_id)
    VALUES (t_id, c_id);
END //


CREATE PROCEDURE `add_registration` (
IN s_id INT,
IN tc_id INT
)
BEGIN
    INSERT INTO Registration (stud_id, teach_course_id)
    VALUES (s_id, tc_id);
END //


CREATE PROCEDURE `add_auth` (
IN p_id INT,
IN u_name VARCHAR(30),
IN pass VARCHAR(255)
)
BEGIN
    INSERT INTO Authentication (pers_id, username, password)
    VALUES (p_id, u_name, pass);
END //


CREATE PROCEDURE `add_room_type` (
IN t_name VARCHAR(30)
)
BEGIN
    INSERT INTO Room_Types (type_name)
    VALUES (t_name);
END //


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


CREATE PROCEDURE `add_schedule` (
IN tc_id INT,
IN room_id INT,
IN class_date DATE
)
BEGIN
    INSERT INTO Schedule (teach_course_id, room_id, date_class)
    VALUES (tc_id, room_id, class_date);
END //


CREATE PROCEDURE `add_attendance` (
IN sch_id INT,
IN s_id INT,
IN status TINYINT
)
BEGIN
    INSERT INTO Attendance (schedule_id, stud_id, status)
    VALUES (sch_id, s_id, status);
END //


CREATE PROCEDURE `add_grade` (
IN r_id INT,
IN f_gr DECIMAL(6,2)
)
BEGIN
    INSERT INTO Grades (reg_id, final_grade)
    VALUES (r_id, f_gr);
END //

DELIMITER ;