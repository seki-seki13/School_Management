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
    JOIN People p ON s.pers_id = p.pers_id;
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
    JOIN People p ON t.pers_id = p.pers_id;
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
    JOIN People p ON a.pers_id = p.pers_id;
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
    JOIN Room_Types rt ON r.type_id = rt.type_id;
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
    JOIN Teachers t ON tch.teacher_id = t.teacher_id
    JOIN People p ON t.pers_id = p.pers_id
    JOIN Courses c ON tch.course_id = c.course_id;
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
    JOIN Students s ON r.stud_id = s.stud_id
    JOIN People ps ON s.pers_id = ps.pers_id -- people-student
    JOIN Teaching tch ON r.teach_course_id = tch.teach_course_id
    JOIN Courses c ON tch.course_id = c.course_id
    JOIN Teachers t ON tch.teacher_id = t.teacher_id
    JOIN People pt ON t.pers_id = pt.pers_id; -- people-teacher
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
    JOIN Teaching tch ON sch.teach_course_id = tch.teach_course_id
    JOIN Teachers t ON tch.teacher_id = t.teacher_id
    JOIN People p ON t.pers_id = p.pers_id
    JOIN Courses c ON tch.course_id = c.course_id
    JOIN Rooms r ON sch.room_id = r.room_id
    JOIN Room_Types rt ON r.type_id = rt.type_id;
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
    JOIN Students s ON att.stud_id = s.stud_id
    JOIN People p ON s.pers_id = p.pers_id
    JOIN Schedule sch ON att.schedule_id = sch.schedule_id
    JOIN Teaching tch ON sch.teach_course_id = tch.teach_course_id
    JOIN Courses c ON tch.course_id = c.course_id;
END //

CREATE PROCEDURE `v_grades` ()
BEGIN
    SELECT
        r.reg_id,
        p.first_name AS student_first_name,
        p.last_name AS student_last_name,
        c.course_name,
        gr.final_grade
    FROM Grades gr
    JOIN Registration r ON gr.reg_id = r.reg_id
    JOIN Students s ON r.stud_id = s.stud_id
    JOIN People p ON s.pers_id = p.pers_id
    JOIN Teaching tch ON r.teach_course_id = tch.teach_course_id
    JOIN Courses c ON tch.course_id = c.course_id;
END //

DELIMITER ;