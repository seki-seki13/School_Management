DELIMITER //

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
    JOIN Courses c ON tch.course_id = c.course_id
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
IN your_pers_id INT
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
    AND (sch.date_class = entered_date OR entered_date IS NULL);
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
    AND (sch.date_class = entered_date OR entered_date IS NULL);
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
		r.reg_id,
        p.first_name as student_first_name,
        p.last_name as student_last_name,
        c.course_id,
        c.course_name,
        gr.final_grade
    FROM Grades gr
    JOIN Registration r ON gr.reg_id = r.reg_id
    JOIN Students s ON r.stud_id = s.stud_id
    JOIN People p ON s.pers_id = p.pers_id
    JOIN Teaching tch ON r.teach_course_id = tch.teach_course_id
    JOIN Teachers t ON tch.teacher_id = t.teacher_id
    JOIN Courses c ON tch.course_id = c.course_id
    WHERE t.pers_id = your_pers_id
    AND (c.course_id = entered_course_id OR entered_course_id IS NULL);
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

DELIMITER ;