-----------------------------------------------
-- REPORTING: Stored procedures dedicated to creating reports across tables
-- and utilities assisting authentication and user role identification
-----------------------------------------------
DELIMITER //

-- The procedure counts and displays course name alongside
-- the number of students registered on it by joining
-- Registration table with Teaching and Courses tables.
-- The results are organised in descending order and
-- grouped by course name
CREATE PROCEDURE `r_students_per_course` ()
BEGIN
    SELECT
        c.course_name,
        COUNT(r.reg_id) AS total_students
    FROM Registration r
    JOIN Teaching t ON r.teach_course_id = t.teach_course_id
    JOIN Courses c ON t.course_id = c.course_id
    GROUP BY c.course_name
    ORDER BY total_students DESC;
END //

-----------------------------------------------
-- The procedure calculates the average grades associated with courses.
-- This is performed by connecting Grades table with Registration,
-- Teaching and Courses tables; the results are organised
-- in a descending order and grouped by course name
CREATE PROCEDURE `r_average_grade_per_course` ()
BEGIN
    SELECT
        c.course_name,
        AVG(g.final_grade) AS average_grade
    FROM Grades g
    JOIN Registration r ON g.reg_id = r.reg_id
    JOIN Teaching t ON r.teach_course_id = t.teach_course_id
    JOIN Courses c ON t.course_id = c.course_id
    GROUP BY c.course_name
    ORDER BY average_grade DESC;
END //

-----------------------------------------------
-- The procedure produces a report of the amount of “Present” (2)
-- students and then calculates the presence percentage against
-- total records.
-- The operation is performed by utilising:
-- aggregate functions (ROUND, SUM),
-- conditional expression (CASE WHEN)
-- and arithmetical operators (*, /);
-- Attendance is joined with Schedule, Teaching and Courses tables.
-- The results are grouped by course name and organised in a
-- descending attendance percentage order
CREATE PROCEDURE `r_attendance_summary` ()
BEGIN
    SELECT
        c.course_name,
        COUNT(*) AS total_records,

        SUM(CASE WHEN a.status = 2 THEN 1 ELSE 0 END)
        AS present_count,

        ROUND(
            (SUM(CASE WHEN a.status = 2 THEN 1 ELSE 0 END)
            / COUNT(*)) * 100, 2

        ) AS attendance_percentage

    FROM Attendance a
    JOIN Schedule s ON a.schedule_id = s.schedule_id
    JOIN Teaching t ON s.teach_course_id = t.teach_course_id
    JOIN Courses c ON t.course_id = c.course_id

    GROUP BY c.course_name
    ORDER BY attendance_percentage DESC;
END //

-----------------------------------------------
-- USER ROLE
-----------------------------------------------
-- The procedure accepts a username as a parameter (IN)
-- and on its basis finds corresponding person ID and password
-- in Authentication table
CREATE PROCEDURE `get_auth_by_username`
(IN e_username VARCHAR(30))
BEGIN
    SELECT
        pers_id,
        password
    FROM Authentication
    WHERE username = e_username;
END //

-----------------------------------------------
-- The procedure accepts person ID as a parameter (IN) and
-- identifies the role of the person with such an ID by
-- searching for match in Administration, Teachers and Students tables
CREATE PROCEDURE `get_user_role`
(
IN p_id INT
)
BEGIN
    IF EXISTS (SELECT 1 FROM Administration WHERE pers_id=p_id) THEN
        SELECT 'Admin' AS role;
    ELSEIF EXISTS (SELECT 1 FROM Teachers WHERE pers_id=p_id) THEN
        SELECT 'Teacher' AS role;
    ELSEIF EXISTS (SELECT 1 FROM Students WHERE pers_id=p_id) THEN
        SELECT 'Student' AS role;
    ELSE
        SELECT 'None' AS role;
    END IF;
END //

DELIMITER ;