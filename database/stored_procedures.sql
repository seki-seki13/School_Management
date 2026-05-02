DELIMITER //

-- VIEWING
CREATE PROCEDURE `v_students` ()
BEGIN
    SELECT
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
        r.room_id,
        r.room_label,
        r.floor,
        r.capacity,
        rt.type_name AS type
    FROM Rooms r
    JOIN Room_Types rt ON r.type_id=rt.type_id;
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
IN your_id INT
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
    WHERE pers_id=your_id;
END //

CREATE PROCEDURE `f_course_by_teacher`
(
IN entered_last_name VARCHAR(50),
IN entered_first_name VARCHAR(50)
)
BEGIN
    SELECT
        tch.teach_course_id AS teaching_ID,
        p.first_name,
        p.last_name,
        c.course_name
    FROM Teaching tch
    JOIN Teachers t ON tch.teacher_id=t.teacher_id
    JOIN People p ON t.pers_id=p.pers_id
    JOIN Courses c ON tch.course_id=c.course_id
    WHERE (p.last_name=entered_last_name OR entered_last_name = '')
    AND (entered_first_name = '' OR p.first_name=entered_first_name);
END //

CREATE PROCEDURE `f_registration`
(
IN entered_stud_id INT,
IN entered_last_name VARCHAR(50),
IN entered_first_name VARCHAR(50)
)
BEGIN
    SELECT
        r.reg_id AS registration_ID,
        ps.first_name AS student_first_name,
        ps.last_name AS student_last_name,
        pt.first_name AS teacher_first_name,
        pt.last_name AS teacher_last_name,
        c.course_name,
        r.reg_date AS date_registered
    FROM Registration r
    JOIN Students s ON r.stud_id=s.stud_id
    JOIN People ps ON s.pers_id=ps.pers_id -- people-student
    JOIN Teaching tch ON r.teach_course_id=tch.teach_course_id
    JOIN Courses c ON tch.course_id=c.course_id
    JOIN Teachers t ON tch.teacher_id=t.teacher_id
    JOIN People pt ON t.pers_id=pt.pers_id -- people-teacher
    WHERE (s.stud_id=entered_stud_id OR (entered_last_name = '' AND entered_first_name = ''))
    AND (entered_stud_id='' OR (ps.last_name=entered_last_name AND ps.first_name=entered_first_name));
END //

CREATE PROCEDURE `f_teacher_schedule`
(
IN your_id INT,
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
    JOIN Teaching tch ON sch.teach_course_id=tch.teach_course_id
    JOIN Teachers t ON tch.teacher_id=t.teacher_id
    JOIN People p ON t.pers_id=p.pers_id
    JOIN Courses c ON tch.course_id=c.course_id
    JOIN Rooms r ON sch.room_id=r.room_id
    JOIN Room_Types rt ON r.type_id=rt.type_id
    WHERE t.teacher_id=your_id
    AND (sch.date_class = entered_date OR entered_date is null)
    ORDER BY sch.date_class ASC;
END //

CREATE PROCEDURE `f_stud_schedule`
(
IN your_id INT,
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
    JOIN Teaching tch ON sch.teach_course_id=tch.teach_course_id
    JOIN Teachers t ON tch.teacher_id=t.teacher_id
    JOIN People p ON t.pers_id=p.pers_id
    JOIN Courses c ON tch.course_id=c.course_id
    JOIN Rooms r ON sch.room_id=r.room_id
    JOIN Room_Types rt ON r.type_id=rt.type_id
    JOIN Registration reg ON tch.teach_course_id=reg.teach_course_id
    WHERE reg.stud_id=your_id
    AND (sch.date_class = entered_date OR entered_date is null)
    ORDER BY sch.date_class ASC;
END //

CREATE PROCEDURE `f_attendance_for_teacher`
(
IN your_id INT,
IN entered_course VARCHAR(50),
IN entered_date DATE
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
    JOIN Students s ON att.stud_id=s.stud_id
    JOIN People p ON s.pers_id=p.pers_id
    JOIN Schedule sch ON att.schedule_id=sch.schedule_id
    JOIN Teaching tch ON sch.teach_course_id=tch.teach_course_id
    JOIN Courses c ON tch.course_id=c.course_id
    WHERE (tch.teacher_id=your_id AND c.course_name=entered_course AND sch.date_class=entered_date);
END //

CREATE PROCEDURE `f_attendance_for_student`
(
IN your_id INT,
IN entered_course VARCHAR(50)
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
    JOIN Students s ON att.stud_id=s.stud_id
    JOIN People p ON s.pers_id=p.pers_id
    JOIN Schedule sch ON att.schedule_id=sch.schedule_id
    JOIN Teaching tch ON sch.teach_course_id=tch.teach_course_id
    JOIN Courses c ON tch.course_id=c.course_id
    WHERE s.stud_id=your_id
    AND (c.course_name=entered_course OR entered_course='');
END //

CREATE PROCEDURE `f_grades_teacher`
(
IN your_id INT,
IN entered_course VARCHAR(50)
)
BEGIN
    SELECT
        p.first_name AS student_first_name,
        p.last_name AS student_last_name,
        gr.final_grade
    FROM Grades gr
    JOIN Registration r ON gr.reg_id=r.reg_id
    JOIN Students s ON r.stud_id=s.stud_id
    JOIN People p ON s.pers_id=p.pers_id
    JOIN Teaching tch ON r.teach_course_id=tch.teach_course_id
    JOIN Courses c ON tch.course_id=c.course_id
    WHERE tch.teacher_id=your_id AND c.course_name=entered_course
    ORDER BY p.last_name ASC;
END //

CREATE PROCEDURE `f_grades_student`
(
IN your_id INT,
IN entered_course VARCHAR(50)
)
BEGIN
    SELECT
        c.course_name,
        gr.final_grade
    FROM Grades gr
    JOIN Registration r ON gr.reg_id=r.reg_id
    JOIN Teaching tch ON r.teach_course_id=tch.teach_course_id
    JOIN Courses c ON tch.course_id=c.course_id
    WHERE s.stud_id=your_id
    AND (c.course_name=entered_course OR entered_course='')
    ORDER BY c.course_name ASC;
END //

-- ADDING

CREATE PROCEDURE `add_student` (
IN e_f_name VARCHAR(50),
IN e_l_name VARCHAR(50),
IN dob DATE,
IN town VARCHAR(40),
IN phone VARCHAR(12),
IN email VARCHAR(100)
)
BEGIN
    INSERT INTO People
    (first_name, last_name, DoB, town, address, phone, email)
    values (e_f_name, e_l_name, dob, town, address, phone, email);

    INSERT INTO Students (pers_id)
    values (new_id);
END //


CREATE PROCEDURE `add_teacher` ()
BEGIN

END //


CREATE PROCEDURE `add_administrator` ()
BEGIN

END //


CREATE PROCEDURE `add_courses` ()
BEGIN

END //


CREATE PROCEDURE `name` ()
BEGIN

END //


CREATE PROCEDURE `add_courses` ()
BEGIN

END //


CREATE PROCEDURE `add_courses` ()
BEGIN

END //


CREATE PROCEDURE `add_courses` ()
BEGIN

END //


CREATE PROCEDURE `name` ()
BEGIN

END //


CREATE PROCEDURE `add_courses` ()
BEGIN

END //


CREATE PROCEDURE `add_courses` ()
BEGIN

END //


CREATE PROCEDURE `add_courses` ()
BEGIN

END //


CREATE PROCEDURE `name` ()
BEGIN

END //


CREATE PROCEDURE `add_courses` ()
BEGIN

END //


CREATE PROCEDURE `add_courses` ()
BEGIN

END //


CREATE PROCEDURE `add_courses` ()
BEGIN

END //


CREATE PROCEDURE `name` ()
BEGIN

END //


CREATE PROCEDURE `add_courses` ()
BEGIN

END //


CREATE PROCEDURE `add_courses` ()
BEGIN

END //


CREATE PROCEDURE `add_courses` ()
BEGIN

END //

DELIMITER;