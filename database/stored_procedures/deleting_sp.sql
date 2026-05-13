-----------------------------------------------
-- DELETING: Stored procedures dedicated to deleting records
-- Procedures accept IN parameters
-- Full CRUD is applied mainly to most meaningful and system-relevant
-- entities specified in the assignment and chosen in requirement
-- elicitation process
-----------------------------------------------

DELIMITER //

CREATE PROCEDURE `delete_student` (
IN s_id INT
)
BEGIN
    SET @p_id = (
    SELECT pers_id FROM Students
    WHERE stud_id = s_id);
    DELETE FROM People
    WHERE pers_id = @p_id;
END //
-----------------------

CREATE PROCEDURE `delete_teacher` (
IN t_id INT
)
BEGIN
    SET @p_id = (
    SELECT pers_id FROM Teachers
    WHERE teacher_id = t_id);
    DELETE FROM People
    WHERE pers_id = @p_id;
END //
-----------------------

CREATE PROCEDURE `delete_course` (
IN c_id VARCHAR(15)
)
BEGIN
    DELETE FROM Courses
    WHERE course_id = c_id;
END //
-----------------------

CREATE PROCEDURE `delete_teaching` (
IN tc_id INT
)
BEGIN
    DELETE FROM Teaching
    WHERE teach_course_id = tc_id;
END //
-----------------------

CREATE PROCEDURE `delete_registration` (
IN r_id INT
)
BEGIN
    DELETE FROM Registration
    WHERE reg_id = r_id;
END //

DELIMITER ;