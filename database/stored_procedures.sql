DELIMITER //

-- VIEWING
CREATE PROCEDURE `v_students` ()
BEGIN
    SELECT
        p.pers_id,
        s.stud_id,
        p.first_name,
        p.last_name,
        p.DoB,
        p.town,
        p.address,
        p.phone,
        p.email
    FROM Students s
    JOIN People p ON s.pers_id=p.pers_id;
END //

CREATE PROCEDURE `v_teachers` ()
BEGIN
    SELECT
        p.pers_id,
        t.teacher_id,
        p.first_name,
        p.last_name,
        p.DoB,
        p.town,
        p.address,
        p.phone,
        p.email
    FROM Teachers t
    JOIN People p ON t.pers_id=p.pers_id;
END //


CREATE PROCEDURE `v_admins` ()
BEGIN
    SELECT
        p.pers_id,
        a.admin_id,
        p.first_name,
        p.last_name,
        p.DoB,
        p.town,
        p.address,
        p.phone,
        p.email
    FROM Administration a
    JOIN People p ON a.pers_id=p.pers_id;
END //


CREATE PROCEDURE `v_courses` ()
BEGIN
    SELECT * FROM Courses;
END //


CREATE PROCEDURE `v_rooms` ()
BEGIN
    SELECT
        rt.type_id,
        r.room_id,
        r.room_label,
        r.floor,
        r.capacity,
        rt.type_name AS type
    FROM Rooms r
    JOIN Room_Types rt ON r.type_id=rt.type_id;
END //


CREATE PROCEDURE `v_room_types` ()
BEGIN
    SELECT
        type_id,
        type_name
    FROM Room_Types;
END //


CREATE PROCEDURE `v_teaching` ()
BEGIN
    SELECT
        tch.teach_course_id AS teaching_ID,
        p.first_name,
        p.last_name,
        c.course_name
    FROM Teaching tch
    JOIN Teachers t ON tch.teacher_id=t.teacher_id
    JOIN People p ON t.pers_id=p.pers_id
    JOIN Courses c ON tch.course_id=c.course_id;
END //


CREATE PROCEDURE `v_registration` ()
BEGIN
    SELECT
        r.reg_id AS registration_ID,
        ps.first_name AS student_first_name,
        ps.last_name AS student_last_name,
        pt.first_name AS teacher_first_name,
        pt.last_name AS teacher_last_name,
        c.course_name,
        r.reg_date as date_registered
    FROM Registration r
    JOIN Students s ON r.stud_id=s.stud_id
    JOIN People ps ON s.pers_id=ps.pers_id -- people-student
    JOIN Teaching tch ON r.teach_course_id=tch.teach_course_id
    JOIN Courses c ON tch.course_id=c.course_id
    JOIN Teachers t ON tch.teacher_id=t.teacher_id
    JOIN People pt ON t.pers_id=pt.pers_id; -- people-teacher
END //


CREATE PROCEDURE `v_schedule` ()
BEGIN
    SELECT
        sch.schedule_id,
        p.first_name AS teacher_first_name,
        p.last_name AS teacher_last_name,
        c.course_name,
        r.room_label,
        r.floor,
        r.capacity,
        rt.type_name AS room_type,
        sch.date_class
    FROM Schedule sch
    JOIN Teaching tch ON sch.teach_course_id=tch.teach_course_id
    JOIN Teachers t ON tch.teacher_id=t.teacher_id
    JOIN People p ON t.pers_id=p.pers_id
    JOIN Courses c ON tch.course_id=c.course_id
    JOIN Rooms r ON sch.room_id=r.room_id
    JOIN Room_Types rt ON r.type_id=rt.type_id;
END //


CREATE PROCEDURE `v_attendance` ()
BEGIN
    SELECT
        c.course_name,
        sch.date_class,
        p.first_name AS student_first_name,
        p.last_name AS student_last_name,
        CASE
            WHEN att.status = 0 THEN 'Absent'
            WHEN att.status = 1 THEN 'Late'
            WHEN att.status = 2 THEN 'Present'
        END AS attendance_status
    FROM Attendance att
    JOIN Students s ON att.stud_id=s.stud_id
    JOIN People p ON s.pers_id=p.pers_id
    JOIN Schedule sch ON att.schedule_id=sch.schedule_id
    JOIN Teaching tch ON sch.teach_course_id=tch.teach_course_id
    JOIN Courses c ON tch.course_id=c.course_id;
END //

CREATE PROCEDURE `v_grades` ()
BEGIN
    SELECT
        p.first_name AS student_first_name,
        p.last_name AS student_last_name,
        c.course_name,
        gr.final_grade
    FROM Grades gr
    JOIN Registration r ON gr.reg_id=r.reg_id
    JOIN Students s ON r.stud_id=s.stud_id
    JOIN People p ON s.pers_id=p.pers_id
    JOIN Teaching tch ON r.teach_course_id=tch.teach_course_id
    JOIN Courses c ON tch.course_id=c.course_id;
END //


-- FINDING SELECTED

CREATE PROCEDURE `f_user_data`
(
IN your_pers_id INT
)
BEGIN
    SELECT
        pers_id,
        first_name,
        last_name,
        DoB AS birth_date,
        town,
        address,
        phone,
        email
    FROM People
    WHERE pers_id = your_pers_id;
END //

CREATE PROCEDURE `f_course_by_teacher`
(
IN your_pers_id INT
)
BEGIN
    SELECT
        tch.teach_course_id AS teaching_ID,
        c.course_name
    FROM Teaching tch
    JOIN Teachers t ON tch.teacher_id = t.teacher_id
    JOIN Courses c ON tch.course_id=c.course_id
    WHERE t.pers_id = your_pers_id;
END //

CREATE PROCEDURE `f_registration`
(
IN entered_stud_id INT
)
BEGIN
    SELECT
        r.reg_id AS registration_ID,
        ps.first_name AS student_first_name,
        ps.last_name AS student_last_name,
        pt.first_name AS teacher_first_name,
        pt.last_name AS teacher_last_name,
        c.course_name,
        r.reg_date
    FROM Registration r
    JOIN Students s ON r.stud_id = s.stud_id
    JOIN People ps ON s.pers_id = ps.pers_id
    JOIN Teaching tch ON r.teach_course_id = tch.teach_course_id
    JOIN Courses c ON tch.course_id = c.course_id
    JOIN Teachers t ON tch.teacher_id = t.teacher_id
    JOIN People pt ON t.pers_id = pt.pers_id
    WHERE s.stud_id = entered_stud_id OR entered_stud_id IS NULL;
END //

CREATE PROCEDURE `f_teacher_schedule`
(
IN your_pers_id INT,
IN entered_date DATE
)
BEGIN
    SELECT
        sch.schedule_id,
        c.course_name,
        r.room_label,
        r.floor,
        rt.type_name AS room_type,
        sch.date_class
    FROM Schedule sch
    JOIN Teaching tch ON sch.teach_course_id = tch.teach_course_id
    JOIN Teachers t ON tch.teacher_id = t.teacher_id
    JOIN Courses c ON tch.course_id = c.course_id
    JOIN Rooms r ON sch.room_id = r.room_id
    JOIN Room_Types rt ON r.type_id = rt.type_id
    WHERE t.pers_id = your_pers_id
    AND (sch.date_class = entered_date OR entered_date IS NULL)
    ORDER BY sch.date_class ASC;
END //

CREATE PROCEDURE `f_stud_schedule`
(
IN your_pers_id INT,
IN entered_date DATE
)
BEGIN
    SELECT
        sch.schedule_id,
        p.first_name AS teacher_first_name,
        p.last_name AS teacher_last_name,
        c.course_name,
        r.room_label,
        r.floor,
        rt.type_name AS room_type,
        sch.date_class
    FROM Schedule sch
    JOIN Teaching tch ON sch.teach_course_id = tch.teach_course_id
    JOIN Teachers t ON tch.teacher_id = t.teacher_id
    JOIN People p ON t.pers_id = p.pers_id
    JOIN Courses c ON tch.course_id = c.course_id
    JOIN Rooms r ON sch.room_id = r.room_id
    JOIN Room_Types rt ON r.type_id = rt.type_id
    JOIN Registration reg ON tch.teach_course_id = reg.teach_course_id
    JOIN Students s ON reg.stud_id = s.stud_id
    WHERE s.pers_id = your_pers_id
    AND (sch.date_class = entered_date OR entered_date IS NULL)
    ORDER BY sch.date_class ASC;
END //

CREATE PROCEDURE `f_attendance_for_teacher`
(
IN your_pers_id INT,
IN entered_sch_id VARCHAR(50)
)
BEGIN
    SELECT
        c.course_name,
        sch.date_class,
        p.first_name AS student_first_name,
        p.last_name AS student_last_name,
        CASE
            WHEN att.status = 0 THEN 'Absent'
            WHEN att.status = 1 THEN 'Late'
            WHEN att.status = 2 THEN 'Present'
        END AS attendance_status
    FROM Attendance att
    JOIN Students s ON att.stud_id = s.stud_id
    JOIN People p ON s.pers_id = p.pers_id
    JOIN Schedule sch ON att.schedule_id = sch.schedule_id
    JOIN Teaching tch ON sch.teach_course_id = tch.teach_course_id
    JOIN Teachers t ON tch.teacher_id = t.teacher_id
    JOIN Courses c ON tch.course_id = c.course_id
    WHERE t.pers_id = your_pers_id AND
    (sch.schedule_id = entered_sch_id OR entered_sch_id IS NULL);
END //

CREATE PROCEDURE `f_attendance_for_student`
(
IN your_pers_id INT
)
BEGIN
    SELECT
        c.course_name,
        sch.date_class,
        CASE
            WHEN att.status = 0 THEN 'Absent'
            WHEN att.status = 1 THEN 'Late'
            WHEN att.status = 2 THEN 'Present'
        END AS attendance_status
    FROM Attendance att
    JOIN Students s ON att.stud_id = s.stud_id
    JOIN Schedule sch ON att.schedule_id = sch.schedule_id
    JOIN Teaching tch ON sch.teach_course_id = tch.teach_course_id
    JOIN Courses c ON tch.course_id = c.course_id
    WHERE s.pers_id = your_pers_id;
END //

CREATE PROCEDURE `f_grades_teacher`
(
IN your_pers_id INT,
IN entered_course_id VARCHAR(15)
)
BEGIN
    SELECT
        p.first_name,
        p.last_name,
        c.course_name,
        gr.final_grade
    FROM Grades gr
    JOIN Registration r ON gr.reg_id = r.reg_id
    JOIN Students s ON r.stud_id = s.stud_id
    JOIN People p ON s.pers_id = p.pers_id
    JOIN Teaching tch ON r.teach_course_id = tch.teach_course_id
    JOIN Teachers t ON tch.teacher_id = t.teacher_id
    JOIN Courses c ON tch.course_id = c.course_id
    WHERE t.pers_id = your_pers_id AND
    (c.course_id = entered_course_id OR entered_course_id IS NULL);
END //

CREATE PROCEDURE `f_grades_student`
(
IN your_pers_id INT
)
BEGIN
    SELECT
        c.course_name,
        gr.final_grade
    FROM Grades gr
    JOIN Registration r ON gr.reg_id = r.reg_id
    JOIN Students s ON r.stud_id = s.stud_id
    JOIN Teaching tch ON r.teach_course_id = tch.teach_course_id
    JOIN Courses c ON tch.course_id = c.course_id
    WHERE s.pers_id = your_pers_id;
END //

-- ADDING

CREATE PROCEDURE `add_student` (
IN f_name VARCHAR(50),
IN l_name VARCHAR(50),
IN dob DATE,
IN e_town VARCHAR(40),
IN e_address VARCHAR(50),
IN e_phone VARCHAR(12),
IN e_email VARCHAR(100)
)
BEGIN
    INSERT INTO People
    (first_name, last_name, DoB, town, address, phone, email)
    VALUES (f_name, l_name, dob, e_town, e_address, e_phone, e_email);

    SET @new_id = LAST_INSERT_ID();

    INSERT INTO Students (pers_id)
    VALUES (@new_id);
END //


CREATE PROCEDURE `add_teacher` (
IN f_name VARCHAR(50),
IN l_name VARCHAR(50),
IN dob DATE,
IN e_town VARCHAR(40),
IN e_address VARCHAR(50),
IN e_phone VARCHAR(12),
IN e_email VARCHAR(100)
)
BEGIN
    INSERT INTO People
    (first_name, last_name, DoB, town, address, phone, email)
    VALUES (f_name, l_name, dob, e_town, e_address, e_phone, e_email);

    SET @new_id = LAST_INSERT_ID();

    INSERT INTO Teachers (pers_id)
    VALUES (@new_id);
END //


CREATE PROCEDURE `add_admin` (
IN f_name VARCHAR(50),
IN l_name VARCHAR(50),
IN dob DATE,
IN e_town VARCHAR(40),
IN e_address VARCHAR(50),
IN e_phone VARCHAR(12),
IN e_email VARCHAR(100)
)
BEGIN
    INSERT INTO People
    (first_name, last_name, DoB, town, address, phone, email)
    VALUES (f_name, l_name, dob, e_town, e_address, e_phone, e_email);

    SET @new_id = LAST_INSERT_ID();

    INSERT INTO Administration (pers_id)
    VALUES (@new_id);
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


-- UPDATING

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


CREATE PROCEDURE `update_course` (
IN c_id VARCHAR(15),
IN c_name VARCHAR(50)
)
BEGIN
    UPDATE Courses
    SET course_name = c_name
    WHERE course_id = c_id;
END //


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


CREATE PROCEDURE `update_password` (
IN e_username VARCHAR(30),
IN new_pass VARCHAR(255)
)
BEGIN
    UPDATE Authentication
    SET password = new_pass
    WHERE username = e_username;
END //


CREATE PROCEDURE `update_grade` (
IN r_id INT,
IN grade DECIMAL(6,2)
)
BEGIN
    UPDATE Grades
    SET final_grade = grade
    WHERE reg_id = r_id;
END //

-- DELETING

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


CREATE PROCEDURE `delete_course` (
IN c_id VARCHAR(15)
)
BEGIN
    DELETE FROM Courses
    WHERE course_id = c_id;
END //


CREATE PROCEDURE `delete_teaching` (
IN tc_id INT
)
BEGIN
    DELETE FROM Teaching
    WHERE teach_course_id = tc_id;
END //


CREATE PROCEDURE `delete_registration` (
IN r_id INT
)
BEGIN
    DELETE FROM Registration
    WHERE reg_id = r_id;
END //

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