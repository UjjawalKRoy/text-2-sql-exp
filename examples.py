emp_profile_few_shots = [
    {
        "Question": "Who is on leave today?",
        "SQLQuery": "SELECT e.first_name, e.last_name FROM employee e JOIN leave_application l ON e.id = "
                    "l.employee_id WHERE l.from_date <= CURDATE() AND l.to_date >= CURDATE() AND l.leave_status = 2 "
                    "LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Who is absent today?",
        "SQLQuery": "SELECT e.first_name, e.last_name FROM employee e JOIN leave_application l ON e.id = "
                    "l.employee_id WHERE l.from_date <= CURDATE() AND l.to_date >= CURDATE() AND l.leave_status = 2 "
                    "LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Who all are on leave today?",
        "SQLQuery": "SELECT e.first_name, e.last_name FROM employee e JOIN leave_application l ON e.id = "
                    "l.employee_id WHERE l.from_date <= CURDATE() AND l.to_date >= CURDATE() AND l.leave_status = 2 "
                    "LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Who is on leave this week?",
        "SQLQuery": "SELECT e.first_name, e.last_name FROM employee e JOIN leave_application l ON e.id = "
                    "l.employee_id WHERE l.from_date BETWEEN DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) AND DATE_ADD(DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY), INTERVAL 7 DAY) AND   l.to_date   BETWEEN DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) AND DATE_ADD(DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY), INTERVAL 7 DAY) AND    l.leave_status =2 LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Who is on WFH today?",
        "SQLQuery": "SELECT e.employee_code, e.first_name, e.last_name FROM employee e JOIN wfh_application wfh ON "
                    "e.id = wfh.employee_id WHERE wfh.from_date <= CURDATE() AND wfh.to_date >= CURDATE() AND "
                    "wfh.status = 2 LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "How many devs are on work from home today?",
        "SQLQuery": "SELECT COUNT(e.id) AS num_devs_on_wfh FROM employee e JOIN wfh_application wfh ON e.id = "
                    "wfh.employee_id WHERE e.designation_id = 2 AND wfh.from_date <= CURDATE() AND wfh.to_date >= "
                    "CURDATE() AND wfh.status = 2 LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Which employees are on work form home?",
        "SQLQuery": "SELECT e.employee_code, e.first_name, e.last_name FROM employee e JOIN wfh_application wfh ON "
                    "e.id = wfh.employee_id WHERE wfh.from_date <= CURDATE() AND wfh.to_date >= CURDATE() AND "
                    "wfh.status = 2 LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Who is on WFH this week?",
        "SQLQuery": "SELECT e.first_name, e.last_name FROM employee e JOIN wfh_application wfh ON e.id = "
                    "wfh.employee_id WHERE wfh.from_date BETWEEN DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) AND DATE_ADD(DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY), INTERVAL 7 DAY) AND   wfh.to_date   BETWEEN DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) AND DATE_ADD(DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY), INTERVAL 7 DAY) AND   wfh.status =2 LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "List all employees who are working from home this week",
        "SQLQuery": "SELECT e.first_name, e.last_name FROM employee e JOIN wfh_application wfh ON e.id = "
                    "wfh.employee_id WHERE wfh.from_date BETWEEN DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) AND DATE_ADD(DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY), INTERVAL 7 DAY) AND   wfh.to_date   BETWEEN DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) AND DATE_ADD(DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY), INTERVAL 7 DAY) AND   wfh.status =2 LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "How many people are free for from each department?",
        "SQLQuery": "SELECT d.name AS department, COUNT(*) AS num_free_employees FROM employee e JOIN "
                    "employee_occupancy o ON e.id = o.employee_id AND o.occupancy_status IN (0, "
                    "1) JOIN department_type d ON e.department_id = d.id GROUP BY d.id LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Who all are fully free today?",
        "SQLQuery": "SELECT e.first_name, e.last_name FROM employee e JOIN employee_occupancy o ON e.id = "
                    "o.employee_id AND o.occupancy_status IN (0, 1) ORDER BY e.first_name LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "How many employees are occupied or partially free today?",
        "SQLQuery": "SELECT COUNT(*) FROM employee_occupancy o JOIN employee e ON e.id = o.employee_id WHERE "
                    "o.occupancy_status IN (0, 3) LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "How many employees are occupied or partially free today from the Web department?",
        "SQLQuery": "SELECT COUNT(*) FROM employee e JOIN employee_occupancy o ON e.id = o.employee_id AND "
                    "o.occupancy_status IN (0, 3) JOIN department_type d ON e.department_id = d.id WHERE d.name LIKE "
                    "'%Web%' LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "List all employees who are free in the Mobile team?",
        "SQLQuery": "SELECT COUNT(*) FROM employee e JOIN employee_occupancy o ON e.id = o.employee_id AND "
                    "o.occupancy_status IN (0, 1) JOIN department_type d ON e.department_id = d.id WHERE d.name LIKE "
                    "'%Mobile%' LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Who are the managers of employees currently on notice?",
        "SQLQuery": "SELECT DISTINCT m.first_name, m.last_name FROM employee e JOIN employee m ON e.reporting_to = "
                    "m.id WHERE e.status = 3 LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "How many people came late today?",
        "SQLQuery": "SELECT COUNT(DISTINCT ae.employee_id) AS came_late_today FROM attendance_event ae LEFT JOIN ( "
                    "SELECT employee_id FROM attendance_event WHERE event_type = 0 AND DATE(event_date_time) = "
                    "CURDATE() AND TIME(event_date_time) <= '10:30:00' ) AS early_entries ON ae.employee_id = "
                    "early_entries.employee_id WHERE ae.event_type = 0 AND DATE(ae.event_date_time) = CURDATE() AND "
                    "TIME(ae.event_date_time) > '10:30:00' AND early_entries.employee_id IS NULL LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Which department has the highest number of employees on probation?",
        "SQLQuery": "SELECT d.name AS department, COUNT(*) AS num_on_probation FROM employee e JOIN department_type d ON e.department_id = d.id WHERE e.status = 1 GROUP BY d.id ORDER BY num_on_probation DESC LIMIT 1;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "How many hours did Ankit Prajapati worked on 21th December 2023?",
        "SQLQuery": "SELECT e.first_name, e.last_name, SUM(iwl.spent / 60) AS total_hours_worked FROM employee e JOIN issue_work_log iwl ON e.id = iwl.employee_id WHERE DATE(iwl.spent_date) = '2023-12-21' AND e.first_name = 'Ankit' AND e.last_name = 'Prajapati' GROUP BY e.id LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Who did not fill the logs yesterday?",
        "SQLQuery": "SELECT ae.employee_id, COUNT(*) AS count, ae.event_date_time, e.* FROM attendance_event ae JOIN "
                    "employee e ON ae.employee_id = e.id LEFT JOIN issue_work_log iwl ON ae.employee_id = "
                    "iwl.employee_id AND DATE(iwl.spent_date) = DATE_SUB(CURDATE(), INTERVAL 1 DAY) WHERE DATE("
                    "ae.event_date_time) = DATE_SUB(CURDATE(), INTERVAL 1 DAY) AND ae.event_type = 0 AND "
                    "iwl.employee_id IS NULL GROUP BY ae.employee_id LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Who have not filled logs for the last two days?",
        "SQLQuery": "SELECT e.first_name, e.last_name, e.employee_code FROM employee e LEFT JOIN attendance_event ae "
                    "ON e.id = ae.employee_id LEFT JOIN issue_work_log iwl ON e.id = iwl.employee_id AND DATE("
                    "iwl.spent_date) = DATE_SUB(CURDATE(), INTERVAL 2 DAY) WHERE DATE(ae.event_date_time) = DATE_SUB("
                    "CURDATE(), INTERVAL 2 DAY) AND ae.event_type = 0 AND iwl.employee_id IS null GROUP BY "
                    "e.employee_code ORDER BY e.first_name LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Which projects have less than 20hrs bucket hours today?",
        "SQLQuery": "SELECT pb.id AS id, pb.name AS name, ( SELECT CAST( SUM(pcr.hours) AS UNSIGNED ) FROM "
                    "project_change_request pcr WHERE pcr.project_id = pb.id ) AS total_hours, ( SELECT CAST( SUM("
                    "bb.billed_mins) AS UNSIGNED ) / 60 FROM bucket_billing bb WHERE bb.project_id = pb.id ) AS "
                    "billed_hours, ( ( SELECT CAST( SUM(pcr.hours) AS UNSIGNED ) FROM project_change_request pcr "
                    "WHERE pcr.project_id = pb.id ) - ( SELECT CAST( SUM(bb.billed_mins) AS UNSIGNED ) / 60 FROM "
                    "bucket_billing bb WHERE bb.project_id = pb.id ) ) AS remain_hours FROM project_basic pb WHERE "
                    "pb.type = 'Hourly bucket' AND (pb.status != 'Signed off' OR pb.status != 'Paused') AND ( ( "
                    "SELECT CAST( SUM(pcr.hours) AS UNSIGNED ) FROM project_change_request pcr WHERE pcr.project_id = pb.id ) - ( SELECT CAST( SUM(bb.billed_mins) AS UNSIGNED ) / 60 FROM bucket_billing bb WHERE bb.project_id = pb.id ) ) < 20 LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Show projects having less than 20 hours remaining in hourly buckets today.",
        "SQLQuery": "SELECT pb.id AS id, pb.name AS name, ( SELECT CAST( SUM(pcr.hours) AS UNSIGNED ) FROM "
                    "project_change_request pcr WHERE pcr.project_id = pb.id ) AS total_hours, ( SELECT CAST( SUM("
                    "bb.billed_mins) AS UNSIGNED ) / 60 FROM bucket_billing bb WHERE bb.project_id = pb.id ) AS "
                    "billed_hours, ( ( SELECT CAST( SUM(pcr.hours) AS UNSIGNED ) FROM project_change_request pcr "
                    "WHERE pcr.project_id = pb.id ) - ( SELECT CAST( SUM(bb.billed_mins) AS UNSIGNED ) / 60 FROM "
                    "bucket_billing bb WHERE bb.project_id = pb.id ) ) AS remain_hours FROM project_basic pb WHERE "
                    "pb.type = 'Hourly bucket' AND (pb.status != 'Signed off' OR pb.status != 'Paused') AND ( ( "
                    "SELECT CAST( SUM(pcr.hours) AS UNSIGNED ) FROM project_change_request pcr WHERE pcr.project_id = pb.id ) - ( SELECT CAST( SUM(bb.billed_mins) AS UNSIGNED ) / 60 FROM bucket_billing bb WHERE bb.project_id = pb.id ) ) < 20 LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Which projects do we need to send invoice to in hire today?",
        "SQLQuery": "SELECT pb.id AS id, pb.name AS name, pr.est_release_date, e.first_name AS first_name, "
                    "e.last_name AS last_name, DATEDIFF(pr.est_release_date, CURDATE()) AS remain_days FROM "
                    "project_basic pb LEFT JOIN project_resource pr ON pr.project_id = pb.id LEFT JOIN employee e ON "
                    "pr.employee_id = e.id WHERE pb.type = 'Dedicated' AND pr.billable = 1 AND (pb.status != 'Signed "
                    "off' AND pb.status != 'Paused') AND DATEDIFF(pr.est_release_date, CURDATE()) <= 7 GROUP BY "
                    "pr.project_id, pr.employee_id ORDER BY pb.name ASC LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Which projects require invoices for employees under hire within the next week?",
        "SQLQuery": "SELECT pb.id AS project_id, pb.name AS project_name, pr.est_release_date, e.first_name, "
                    "e.last_name, DATEDIFF(pr.est_release_date, CURDATE()) AS remain_days FROM project_basic pb LEFT "
                    "JOIN project_resource pr ON pr.project_id = pb.id LEFT JOIN employee e ON pr.employee_id = e.id "
                    "WHERE pb.type = 'Dedicated' AND pr.billable = 1 AND (pb.status != 'Signed off' AND pb.status != "
                    "'Paused') AND DATEDIFF(pr.est_release_date, CURDATE()) <= 7 GROUP BY pr.project_id, "
                    "pr.employee_id ORDER BY pb.name ASC LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Give me a list of upcoming milestones for Fixed cost projects",
        "SQLQuery": "SELECT pb.name AS name, pb.status AS status, pm.name AS milestone_name, pm.status AS "
                    "milestone_status, pm.est_date_completion AS est_date_completion FROM project_basic pb LEFT JOIN "
                    "project_milestone pm ON pm.project_id = pb.id WHERE pb.type = 'Fixed cost' AND ( pb.status != "
                    "'Signed off' AND pb.status != 'Paused' ) AND pm.est_date_completion >= CURDATE() LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Did we send invoice for Project1?",
        "SQLQuery": "SELECT i.title AS invoice_title, i.invoice_no AS invoice_number, i.createdAt AS invoice_created, pb.name AS project_name, pb.id AS project_id FROM invoice i LEFT JOIN project_basic pb ON i.project_id = pb.id WHERE pb.name LIKE '%Project1%' AND DATE(i.createdAt) >= DATE_SUB( CURDATE(), INTERVAL 15 DAY ) AND email_sent = 1 LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "How many interviews do i have to take today and at what time? My employeee_code is MI-264",
        "SQLQuery": "SELECT c.first_name, c.last_name, ji.start_date_time, ji.interview_mode, ji.result FROM "
                    "job_interview ji LEFT JOIN candidates c ON ji.candidate = c.id WHERE FIND_IN_SET((SELECT id from employee WHERE employee_code='MI-264') , ji.interviewers) > 0 AND DATE(ji.start_date_time) = CURDATE() LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Whats for lunch today?",
        "SQLQuery": "SELECT menu FROM lunch_menu LIMIT 1;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Who has the Realme-C3?",
        "SQLQuery": "SELECT a.name AS name, a.description AS description, a.assetId as assetId, di.status AS status, "
                    "CONCAT(e.first_name, ' ', e.last_name) AS device_with FROM device_information di LEFT JOIN asset a ON a.id = di.device_id LEFT JOIN employee e ON di.employee_id = e.id WHERE a.name LIKE '%Realme-C3%' LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Whats for lunch tomorrow?",
        "SQLQuery": "SELECT menu FROM lunch_menu LIMIT 1;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Did I check for lunch today? My employee_code is MI-516",
        "SQLQuery": "SELECT COUNT(*) > 0 AS did_check_for_lunch FROM lunch_report lr JOIN employee e ON "
                    "lr.employee_id = e.id WHERE e.employee_code = 'MI-516' AND DATE(lr.date) = CURDATE() LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "How many offline and online interviews are there today?",
        "SQLQuery": "SELECT COUNT(*) AS total_interviews, SUM(CASE WHEN interview_mode LIKE '%online%' THEN 1 ELSE 0 "
                    "END) AS online_interviews, SUM(CASE WHEN interview_mode NOT LIKE '%online%' THEN 1 ELSE 0 END) "
                    "AS offline_interviews FROM job_interview WHERE start_date_time >= NOW() AND start_date_time < "
                    "NOW() + INTERVAL 1 DAY LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Whose birthday is it today?",
        "SQLQuery": "SELECT employee_code, first_name, last_name FROM employee WHERE Day(dob) = Day(Curdate()) AND "
                    "Month(dob) = Month(Curdate()) LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Whose birthday was yesterday?",
        "SQLQuery": "SELECT employee_code, first_name, last_name FROM   employee WHERE  Date_add(dob, INTERVAL Year("
                    "CURRENT_DATE()) - Year(dob) YEAR) = DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY) LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Whose birthday was last week?",
        "SQLQuery": "SELECT employee_code, first_name, last_name FROM employee WHERE  Date_add(dob, INTERVAL Year("
                    "CURRENT_DATE()) - Year(dob)YEAR) BETWEEN Date_sub(CURRENT_DATE(), INTERVAL 7 DAY) AND "
                    "CURRENT_DATE() LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Whose birthday is next week?",
        "SQLQuery": "SELECT employee_code, first_name, last_name FROM employee WHERE Date_add(dob, INTERVAL Year("
                    "CURRENT_DATE()) - Year(dob) year) between CURRENT_DATE() AND Date_add(CURRENT_DATE(), "
                    "INTERVAL 7 day) LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Whose birthday is tomorrow?",
        "SQLQuery": "SELECT employee_code, first_name, last_name FROM employee WHERE Date_add(dob, INTERVAL Year("
                    "CURRENT_DATE()) - Year(dob) YEAR) = DATE_ADD(CURRENT_DATE(), INTERVAL 1 DAY) LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Whose Anniversary is today?",
        "SQLQuery": "SELECT employee_code, first_name,last_name from employee WHERE Day(join_date) = Day(Curdate()) "
                    "AND Month(join_date) = Month(Curdate()) LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Whose Anniversary was last week?",
        "SQLQuery": "SELECT employee_code, first_name, last_name, join_date from employee where Date_add(join_date, "
                    "INTERVAL Year(CURRENT_DATE()) - Year(join_date) YEAR) between Date_sub(CURRENT_DATE(), "
                    "INTERVAL 7 DAY) AND CURRENT_DATE() LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "How many leaves do I have? employee_code of user querying=MI-488",
        "SQLQuery": "SELECT sum(balance) FROM leave_balance WHERE employee_id IN (SELECT id FROM employee WHERE "
                    "employee_code = 'MI-488') LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Whose Anniversary is in the next week?",
        "SQLQuery": "SELECT employee_code, first_name, last_name, join_date FROM   employee WHERE  Date_add("
                    "join_date, INTERVAL Year(CURRENT_DATE()) - Year(join_date) year) BETWEEN CURRENT_DATE() AND "
                    "Date_add(CURRENT_DATE(), INTERVAL 7 day) LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Whose Anniversary is tomorrow?",
        "SQLQuery": "SELECT employee_code, first_name, last_name, join_date FROM   employee WHERE  Date_add("
                    "join_date, INTERVAL Year(CURRENT_DATE()) - Year(join_date) YEAR) = DATE_ADD(CURRENT_DATE(), "
                    "INTERVAL 1 DAY) LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Need b positive blood group",
        "SQLQuery": "SELECT e.employee_code, e.first_name, e.last_name FROM employee e WHERE e.blood_group = 'B+' "
                    "LIMIT 8 LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Who is reporting manager of Ujjawal Roy?",
        "SQLQuery": "SELECT m.first_name AS manager_first_name, m.last_name AS manager_last_name FROM employee e JOIN employee m ON e.reporting_to = m.id WHERE e.first_name = 'Ujjawal' AND e.last_name = 'Roy' LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Who all work under Samar Patel?",
        "SQLQuery": "SELECT e.first_name, e.last_name FROM employee e WHERE e.reporting_to = (SELECT id FROM employee WHERE first_name = 'Samar' AND last_name = 'Patel') LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Which job openings we have right now?",
        "SQLQuery": "SELECT * FROM jobs WHERE status LIKE '%open%' LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Show me the emergency number of MI-488",
        "SQLQuery": "SELECT eec.mobile_no, e.employee_code FROM employee e JOIN employee_emergency_contact eec ON "
                    "e.id = eec.employee_id WHERE e.employee_code = 'MI-488' LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "What are the details of candidates who have interviews scheduled for tomorrow?",
        "SQLQuery": "SELECT c.first_name, c.last_name, ji.start_date_time FROM job_interview ji LEFT JOIN candidates "
                    "c ON ji.candidate = c.id WHERE DATE(ji.start_date_time) = CURDATE() + INTERVAL 1 DAY LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "How many interviews have been conducted by the employee with employee_code 'MI-516'?",
        "SQLQuery": "SELECT COUNT(*) AS total_interviews FROM job_interview ji WHERE ji.scheduled_by = (SELECT id "
                    "FROM employee WHERE employee_code = 'MI-516') LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Which candidate has the highest technical rating in interviews conducted so far?",
        "SQLQuery": "SELECT c.first_name, c.last_name, ji.technical_rating FROM job_interview ji LEFT JOIN candidates c ON ji.candidate = c.id ORDER BY ji.technical_rating DESC LIMIT 1;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "How many interviews are scheduled for candidates from the city 'Ahmedabad'?",
        "SQLQuery": "SELECT COUNT(*) AS total_interviews FROM job_interview ji LEFT JOIN candidates c ON ji.candidate"
                    " = c.id WHERE c.city LIKE '%Ahmedabad%' LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "What are the details of employees who have scheduled job interviews and their corresponding candidate details?",
        "SQLQuery": "SELECT e.first_name AS employee_first_name, e.last_name AS employee_last_name, c.first_name AS "
                    "candidate_first_name, c.last_name AS candidate_last_name, ji.start_date_time FROM job_interview "
                    "ji INNER JOIN employee e ON ji.scheduled_by = e.id INNER JOIN candidates c ON ji.candidate = "
                    "c.id LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "For each employee, what is the count of interviews they have conducted and the count of interviews they have attended as interviewers?",
        "SQLQuery": "SELECT e.first_name, e.last_name, COUNT(DISTINCT ji1.id) AS conducted_interviews, COUNT(DISTINCT ji2.id) AS attended_interviews FROM employee e LEFT JOIN job_interview ji1 ON e.id = ji1.scheduled_by LEFT JOIN job_interview ji2 ON FIND_IN_SET(e.id, ji2.interviewers) > 0 GROUP BY e.first_name, e.last_name LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "What are the details of candidates who have interviews scheduled but have not yet been attended by any interviewer?",
        "SQLQuery": "SELECT c.first_name, c.last_name, ji.start_date_time FROM job_interview ji LEFT JOIN candidates "
                    "c ON ji.candidate = c.id LEFT JOIN employee e ON FIND_IN_SET(e.id, ji.interviewers) > 0 WHERE "
                    "e.id IS NULL LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "For each job, what are the names of interviewers scheduled for interviews and their corresponding email addresses?",
        "SQLQuery": "SELECT j.job_title, e.first_name, e.last_name, e.email_id FROM job_interview ji INNER JOIN "
                    "employee e ON FIND_IN_SET(e.id, ji.interviewers) > 0 INNER JOIN jobs j ON ji.job = j.id LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Who is Vatsal's reporting manager?",
        "SQLQuery": "SELECT m.first_name AS manager_first_name, m.last_name AS manager_last_name FROM employee e JOIN employee m ON e.reporting_to = m.id WHERE e.first_name = 'Vatsal' LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "How many invoices were sent in the last month?",
        "SQLQuery": "SELECT COUNT(*) AS total_invoices_sent FROM invoice WHERE DATE_FORMAT(createdAt, '%Y-%m') = "
                    "DATE_FORMAT(CURDATE() - INTERVAL 1 MONTH, '%Y-%m') LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "What is the total amount of all invoices sent for projects in development?",
        "SQLQuery": "SELECT SUM(total_amount) AS total_amount_sent FROM invoice i LEFT JOIN project_basic pb ON "
                    "i.project_id = pb.id WHERE pb.status LIKE '%development%' AND email_sent = 1 LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Which projects have invoices that are still unpaid?",
        "SQLQuery": "SELECT DISTINCT pb.name AS project_name FROM invoice i LEFT JOIN project_basic pb ON "
                    "i.project_id = pb.id WHERE i.status != 3 LIMIT 8; -- 3 indicates fully paid",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "How many invoices were sent for each project in the last week?",
        "SQLQuery": "SELECT pb.name AS project_name, COUNT(*) AS total_invoices_sent FROM invoice i LEFT JOIN "
                    "project_basic pb ON i.project_id = pb.id WHERE DATEDIFF(CURDATE(), i.createdAt) <= 7 GROUP BY "
                    "pb.name LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "What are the details of the most recent invoice sent?",
        "SQLQuery": "SELECT i.title AS invoice_title, i.invoice_no AS invoice_number, i.createdAt AS invoice_created, pb.name AS project_name, pb.id AS project_id FROM invoice i LEFT JOIN project_basic pb ON i.project_id = pb.id WHERE email_sent = 1 ORDER BY i.createdAt DESC LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "List all employees who worked on projects with overdue invoices.",
        "SQLQuery": "SELECT DISTINCT e.first_name, e.last_name FROM employee e INNER JOIN project_resource pr ON e.id = pr.employee_id INNER JOIN invoice i ON pr.project_id = i.project_id WHERE i.due_date < CURDATE() AND i.status != 3 LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Which projects have invoices that are partially paid and still have resources assigned to them?",
        "SQLQuery": "SELECT DISTINCT pb.name AS project_name FROM project_basic pb INNER JOIN invoice i ON pb.id = "
                    "i.project_id INNER JOIN project_resource pr ON pb.id = pr.project_id WHERE i.status = 2 LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "List all projects with invoices sent within the last month and the corresponding project resources.",
        "SQLQuery": "SELECT pb.name AS project_name, e.first_name AS resource_first_name, e.last_name AS "
                    "resource_last_name FROM project_basic pb INNER JOIN invoice i ON pb.id = i.project_id INNER JOIN project_resource pr ON pb.id = pr.project_id INNER JOIN employee e ON pr.employee_id = e.id WHERE DATE_FORMAT(i.createdAt, '%Y-%m') = DATE_FORMAT(CURDATE() - INTERVAL 1 MONTH, '%Y-%m') LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "List all employees who have worked on projects that are signed off and have invoices overdue.",
        "SQLQuery": "SELECT DISTINCT e.first_name, e.last_name FROM employee e INNER JOIN project_resource pr ON e.id = pr.employee_id INNER JOIN project_basic pb ON pr.project_id = pb.id INNER JOIN invoice i ON pb.id = i.project_id WHERE pb.status = 'Signed off' AND i.due_date < CURDATE() LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "List the employees who joined the company after '2022-01-01' and are currently active.",
        "SQLQuery": "SELECT first_name, last_name, join_date FROM employee WHERE join_date > '2022-01-01' AND status "
                    "= 2 LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "List the employees who have a leave balance greater than 5.",
        "SQLQuery": "SELECT e.first_name, e.last_name FROM employee e JOIN leave_balance l ON e.id = l.employee_id "
                    "WHERE l.balance > 5 LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Help me determine the average number of leaves taken by employees per month in the last quarter.",
        "SQLQuery": "SELECT AVG(leaves_taken) AS avg_leaves_per_month FROM ( SELECT COUNT(*) AS leaves_taken FROM "
                    "leave_application WHERE from_date >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH) GROUP BY MONTH("
                    "from_date) ) AS leaves_per_month LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Tell me the names of employees who have not taken any leave in the past year.",
        "SQLQuery": "SELECT e.first_name, e.last_name FROM employee e LEFT JOIN leave_application la ON e.id = "
                    "la.employee_id WHERE la.id IS NULL AND e.join_date <= DATE_SUB(CURDATE(), INTERVAL 1 YEAR) LIMIT"
                    " 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Give me names of the employees who have taken leave for more than 3 consecutive days and have a leave balance less than 5.",
        "SQLQuery": "SELECT e.first_name, e.last_name FROM employee e JOIN leave_application la ON e.id = "
                    "la.employee_id JOIN leave_balance lb ON e.id = lb.employee_id WHERE DATEDIFF(la.to_date, "
                    "la.from_date) > 3 AND lb.balance < 5 LIMIT 8;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Who is Hasmukh Suthar?",
        "SQLQuery": "SELECT JSON_OBJECT( 'first_name', e.first_name, 'last_name', e.last_name, 'department', dt.name, 'designation', d.name, 'years_in_company', TIMESTAMPDIFF(YEAR, e.join_date, NOW()), 'social_links', e.google_profile, 'email', e.email_id, 'mobile', e.mobile_no ) AS employee_info FROM "
                    "employee e JOIN designation_type d ON e.designation_id = d.id JOIN department_type dt ON "
                    "e.department_id = dt.id WHERE e.first_name = 'Hasmukh' AND e.last_name = 'Suthar';",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Tell me about Tirth Shah",
        "SQLQuery": "SELECT JSON_OBJECT( 'first_name', e.first_name, 'last_name', e.last_name, 'department', dt.name, 'designation', d.name, 'years_in_company', TIMESTAMPDIFF(YEAR, e.join_date, NOW()), 'social_links', e.google_profile, 'email', e.email_id, 'mobile', e.mobile_no ) AS employee_info FROM "
                    "employee e JOIN designation_type d ON e.designation_id = d.id JOIN department_type dt ON "
                    "e.department_id = dt.id WHERE e.first_name = 'Tirth' AND e.last_name = 'Shah';",
        "SQLResult": "",
        "Answer": "",
    },
]

print(len(emp_profile_few_shots))
