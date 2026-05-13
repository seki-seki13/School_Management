-----------------------------------------------
-- UPDATING: Stored procedures dedicated to updating existing records
-- Procedures accept IN parameters
-- Full CRUD is applied mainly to most meaningful and system-relevant
-- entities specified in the assignment and chosen in requirement
-- elicitation process
-----------------------------------------------

DELIMITER //

-- Updating people is handled separately for students and teachers
-- to clearly distinguish them and for clearer distinction
-- in admin_menu to reduce confusion and ease debugging
CREATE PROCEDURE `update_student` (
IN s_id INT,
IN f_name VARCHAR(50),
IN l_name VARCHAR(50),
IN dob DATE,
IN e_town VARCHAR(40),
IN e_address VARCHAR(50),
IN e_phone VARCHAR(12),
IN e_email VARCHAR(100)
)
BEGIN
    DECLARE p_id INT;
    SELECT pers_id INTO p_id FROM Students
    WHERE stud_id = s_id;
    UPDATE People
    SET first_name = f_name,
        last_name = l_name,
        DoB = dob,
        town = e_town,
        address = e_address,
        phone = e_phone,
        email = e_email
    WHERE pers_id = p_id;
END //
-----------------------

CREATE PROCEDURE `update_teacher` (
IN t_id INT,
IN f_name VARCHAR(50),
IN l_name VARCHAR(50),
IN dob DATE,
IN e_town VARCHAR(40),
IN e_address VARCHAR(50),
IN e_phone VARCHAR(12),
IN e_email VARCHAR(100)
)
BEGIN
    DECLARE p_id INT;
    SELECT pers_id INTO p_id FROM Teachers
    WHERE teacher_id = t_id;
    UPDATE People
    SET first_name = f_name,
        last_name = l_name,
        DoB = dob,
        town = e_town,
        address = e_address,
        phone = e_phone,
        email = e_email
    WHERE pers_id = p_id;
END //
----------------------------------------------

CREATE PROCEDURE `update_course` (
IN c_id VARCHAR(15),
IN c_name VARCHAR(50)
)
BEGIN
    UPDATE Courses
    SET course_name = c_name
    WHERE course_id = c_id;
END //
-----------------------

CREATE PROCEDURE `update_teaching` (
    IN tc_id INT,
    IN new_t_id INT,
    IN new_c_id VARCHAR(15)
)
BEGIN
    UPDATE Teaching
    SET teacher_id = new_t_id,
        course_id = new_c_id
    WHERE teach_course_id = tc_id;
END //
-----------------------

CREATE PROCEDURE `update_registration` (
    IN r_id INT,
    IN new_s_id INT,
    IN new_tc_id INT
)
BEGIN
    UPDATE Registration
    SET stud_id = new_s_id,
        teach_course_id = new_tc_id
    WHERE reg_id = r_id;
END //
-----------------------

CREATE PROCEDURE `update_password` (
IN e_username VARCHAR(30),
IN new_pass VARCHAR(255)
)
BEGIN
    UPDATE Authentication
    SET password = new_pass
    WHERE username = e_username;
END //
-----------------------

CREATE PROCEDURE `update_grade` (
IN r_id INT,
IN grade DECIMAL(6,2)
)
BEGIN
    UPDATE Grades
    SET final_grade = grade
    WHERE reg_id = r_id;
END //

DELIMITER ;