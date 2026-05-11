DELIMITER //

-- REPORTING

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

-- USER ROLE

CREATE PROCEDURE `get_auth_by_username`
(IN e_username VARCHAR(30))
BEGIN
    SELECT
        pers_id,
        password
    FROM Authentication
    WHERE username = e_username;
END //


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