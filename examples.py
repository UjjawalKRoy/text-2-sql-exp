emp_profile_few_shots = [
    {
        "Question": "Who is on leave today?",
        "SQLQuery": "SELECT e.first_name, e.last_name FROM employee e JOIN leave_application l ON e.id = l.employee_id WHERE l.from_date <= CURDATE() AND l.to_date >= CURDATE() AND l.leave_status = 2;",
        "SQLResult": "[(Ujjawal, Roy,), (Siddhant, Pandey, )]",
        "Answer": "Ujjawal Roy and Siddhant Pandey are on leave today.",
    },
    {
        "Question": "Who all are on leave today?",
        "SQLQuery": "SELECT e.first_name, e.last_name FROM employee e JOIN leave_application l ON e.id = l.employee_id WHERE l.from_date <= CURDATE() AND l.to_date >= CURDATE() AND l.leave_status = 2;",
        "SQLResult": "[(Ujjawal, Roy,), (Siddhant, Pandey, )]",
        "Answer": "Ujjawal Roy and Siddhant Pandey are on leave today.",
    },
    {
        "Question": "Who is on leave this week?",
        "SQLQuery": "SELECT e.first_name, e.last_name FROM employee e JOIN leave_application l ON e.id = l.employee_id WHERE l.from_date BETWEEN DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) AND DATE_ADD(DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY), INTERVAL 7 DAY) AND   l.to_date   BETWEEN DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) AND DATE_ADD(DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY), INTERVAL 7 DAY) AND    l.leave_status =2;",
        "SQLResult": "[(Ujjawal, Roy,), (Siddhant, Pandey, ), (Vatsal, Gamit, )]",
        "Answer": "Ujjawal Roy, Siddhant Pandey and Vatsal Gamit are on leave this week.",
    },
    {
        "Question": "Who is on WFH today?",
        "SQLQuery": "SELECT e.employee_code, e.first_name, e.last_name FROM employee e JOIN wfh_application wfh ON e.id = wfh.employee_id WHERE wfh.from_date <= CURDATE() AND wfh.to_date >= CURDATE() AND wfh.status = 2;",
        "SQLResult": "",
        "Answer": "No one is on WFH today",
    },
    {
        "Question": "How many devs are on work from home today?",
        "SQLQuery": "SELECT COUNT(e.id) AS num_devs_on_wfh FROM employee e JOIN wfh_application wfh ON e.id = wfh.employee_id WHERE e.designation_id = 2 AND wfh.from_date <= CURDATE() AND wfh.to_date >= CURDATE() AND wfh.status = 2;",
        "SQLResult": "",
        "Answer": "No one is on WFH today",
    },
    {
        "Question": "Which employees are on work form home?",
        "SQLQuery": "SELECT e.employee_code, e.first_name, e.last_name FROM employee e JOIN wfh_application wfh ON e.id = wfh.employee_id WHERE wfh.from_date <= CURDATE() AND wfh.to_date >= CURDATE() AND wfh.status = 2;",
        "SQLResult": "",
        "Answer": "No one is on WFH today",
    },
    {
        "Question": "Who is on WFH this week?",
        "SQLQuery": "SELECT e.first_name, e.last_name FROM employee e JOIN wfh_application wfh ON e.id = wfh.employee_id WHERE wfh.from_date BETWEEN DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) AND DATE_ADD(DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY), INTERVAL 7 DAY) AND   wfh.to_date   BETWEEN DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) AND DATE_ADD(DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY), INTERVAL 7 DAY) AND   wfh.status =2;",
        "SQLResult": "[(Krishna, Thakkar,), (Siddhant, Pandey,), (Sanskar, Mehta,)]",
        "Answer": "Krishna Thakkar, Siddhant Pandey and Sanskar Mehta are on WFH this week",
    },
    {
        "Question": "How many people are free for from each department?",
        "SQLQuery": "SELECT d.name AS department, COUNT(*) AS num_free_employees FROM employee e JOIN employee_occupancy o ON e.id = o.employee_id AND o.occupancy_status IN (0, 1) JOIN department_type d ON e.department_id = d.id GROUP BY d.id;",
        "SQLResult": "[('Design', 11), ('Mobile', 8), ('Game', 8), ('Web', 22), ('Business Analysis', 2), ('DevOps', 1), ('Management', 2)]",
        "Answer": "There are 11 people from Design, 8 from Mobile, 8 from Game, 22 from Web, 2 from Business Analysis, 1 from DevOps and 2 from management who are free today",
    },
    {
        "Question": "Who all are fully free today?",
        "SQLQuery": "SELECT e.first_name, e.last_name FROM employee e JOIN employee_occupancy o ON e.id = o.employee_id AND o.occupancy_status IN (0, 1) ORDER BY e.first_name;",
        "SQLResult": "[('Aditya', 'Jani'), ('Archit', 'Patel'), ('Ebrahim', 'Sakir'), ('Fahad', 'Mansuri'), ('Honey', 'Chavda'), ('Jay', 'Soni'), ('Khetpal', 'Charan')]",
        "Answer": "[('Aditya', 'Jani'), ('Archit', 'Patel'), ('Ebrahim', 'Sakir'), ('Fahad', 'Mansuri'), ('Honey', 'Chavda'), ('Jay', 'Soni'), ('Khetpal', 'Charan')]",
    },
    {
        "Question": "How many employees are occupied or partially free today?",
        "SQLQuery": "SELECT COUNT(*) FROM employee_occupancy o JOIN employee e ON e.id = o.employee_id WHERE o.occupancy_status IN (0, 3);",
        "SQLResult": "[(59,)]",
        "Answer": "Today, there are 59 employees who are occupied or partially free.",
    },
    {
        "Question": "How many employees are occupied or partially free today from the Web department?",
        "SQLQuery": "SELECT COUNT(*) FROM employee e JOIN employee_occupancy o ON e.id = o.employee_id AND o.occupancy_status IN (0, 1) JOIN department_type d ON e.department_id = d.id WHERE d.name LIKE '%Web%';",
        "SQLResult": "[(22,)]",
        "Answer": "There are 22 employees who are occupied or partially free today from the Web department.",
    },
    {
        "Question": "Who are the managers of employees currently on notice?",
        "SQLQuery": "SELECT DISTINCT m.first_name, m.last_name FROM employee e JOIN employee m ON e.reporting_to = m.id WHERE e.status = 3;",
        "SQLResult": "[(Bipin,Mishra)]",
        "Answer": "The managers of the employees currently on notice are: Bipin Mishra",
    },
    {
        "Question": "Which department has the highest number of employees on probation?",
        "SQLQuery": "SELECT d.name AS department, COUNT(*) AS num_on_probation FROM employee e JOIN department_type d ON e.department_id = d.id WHERE e.status = 1 GROUP BY d.id ORDER BY num_on_probation DESC LIMIT 1;",
        "SQLResult": "[(Web,5)]",
        "Answer": "The department with the highest number of employees on probation is department Web with 5 employees.",
    },
    {
        "Question": "How many hours did Ankit Prajapati worked on 21th December 2023?",
        "SQLQuery": "SELECT e.first_name, e.last_name, SUM(iwl.spent / 60) AS total_hours_worked FROM employee e JOIN issue_work_log iwl ON e.id = iwl.employee_id WHERE DATE(iwl.spent_date) = '2023-12-21' AND e.first_name = 'Ankit' AND e.last_name = 'Prajapati' GROUP BY e.id;",
        "SQLResult": "[(Ankit ,Prajapati, 8)]",
        "Answer": "Ankit worked for 8hrs on 21st of December 2023.",
    },
    {
        "Question": "Who did not fill the logs yesterday?",
        "SQLQuery": "select ae.employee_id, COUNT(*) AS count, ae.event_date_time, e.first_name, e.last_name from attendance_event ae JOIN employee e ON ae.employee_id = e.id LEFT JOIN issue_work_log iwl ON ae.employee_id = iwl.employee_id AND DATE(iwl.spent_date) = DATE_SUB(CURDATE(), INTERVAL 1 DAY) where DATE(ae.event_date_time) = DATE_SUB(CURDATE(), INTERVAL 1 DAY) AND ae.event_type = 0 AND iwl.employee_id IS null GROUP by ae.employee_id;",
        "SQLResult": "[('Mehul', 'Rajput'), ('Samar', 'Patel'), ('Kalpesh', 'Thakar'), ('Kiran', 'Malvi')]",
        "Answer": "The following employee did not fill their daily log yesterday: 1. Mehul rajput, 2. Samar Patel, 3. Kalpesh Thakkar, 4. Kiran Malvi",
    },
    {
        "Question": "Who have not filled logs for the last two days?",
        "SQLQuery": "SELECT e.first_name, e.last_name, e.employee_code FROM employee e LEFT JOIN attendance_event ae ON e.id = ae.employee_id LEFT JOIN issue_work_log iwl ON e.id = iwl.employee_id AND DATE(iwl.spent_date) = DATE_SUB(CURDATE(), INTERVAL 2 DAY) WHERE DATE(ae.event_date_time) = DATE_SUB(CURDATE(), INTERVAL 2 DAY) AND ae.event_type = 0 AND iwl.employee_id IS null GROUP BY e.employee_code ORDER BY e.first_name;",
        "SQLResult": "[('Mehul', 'Rajput'), ('Samar', 'Patel'), ('Kalpesh', 'Thakar'), ('Kiran', 'Malvi')]",
        "Answer": "The following employee did not fill their daily log in last 2 days: 1. Mehul rajput, 2. Samar Patel, 3. Kalpesh Thakkar, 4. Kiran Malvi",
    },
    {
        "Question": "Which projects have less than 20hrs bucket hours today?",
        "SQLQuery": "SELECT pb.id AS id, pb.name AS name, ( SELECT CAST( SUM(pcr.hours) AS UNSIGNED ) FROM project_change_request pcr WHERE pcr.project_id = pb.id ) AS total_hours, ( SELECT CAST( SUM(bb.billed_mins) AS UNSIGNED ) / 60 FROM bucket_billing bb WHERE bb.project_id = pb.id ) AS billed_hours, ( ( SELECT CAST( SUM(pcr.hours) AS UNSIGNED ) FROM project_change_request pcr WHERE pcr.project_id = pb.id ) - ( SELECT CAST( SUM(bb.billed_mins) AS UNSIGNED ) / 60 FROM bucket_billing bb WHERE bb.project_id = pb.id ) ) AS remain_hours FROM project_basic pb WHERE pb.type = 'Hourly bucket' AND (pb.status != 'Signed off' OR pb.status != 'Paused') AND ( ( SELECT CAST( SUM(pcr.hours) AS UNSIGNED ) FROM project_change_request pcr WHERE pcr.project_id = pb.id ) - ( SELECT CAST( SUM(bb.billed_mins) AS UNSIGNED ) / 60 FROM bucket_billing bb WHERE bb.project_id = pb.id ) ) < 20;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Show projects having less than 20 hours remaining in hourly buckets today.",
        "SQLQuery": "SELECT pb.id AS id, pb.name AS name, ( SELECT CAST( SUM(pcr.hours) AS UNSIGNED ) FROM project_change_request pcr WHERE pcr.project_id = pb.id ) AS total_hours, ( SELECT CAST( SUM(bb.billed_mins) AS UNSIGNED ) / 60 FROM bucket_billing bb WHERE bb.project_id = pb.id ) AS billed_hours, ( ( SELECT CAST( SUM(pcr.hours) AS UNSIGNED ) FROM project_change_request pcr WHERE pcr.project_id = pb.id ) - ( SELECT CAST( SUM(bb.billed_mins) AS UNSIGNED ) / 60 FROM bucket_billing bb WHERE bb.project_id = pb.id ) ) AS remain_hours FROM project_basic pb WHERE pb.type = 'Hourly bucket' AND (pb.status != 'Signed off' OR pb.status != 'Paused') AND ( ( SELECT CAST( SUM(pcr.hours) AS UNSIGNED ) FROM project_change_request pcr WHERE pcr.project_id = pb.id ) - ( SELECT CAST( SUM(bb.billed_mins) AS UNSIGNED ) / 60 FROM bucket_billing bb WHERE bb.project_id = pb.id ) ) < 20;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Which projects do we need to send invoice to in hire today?",
        "SQLQuery": "SELECT pb.id AS id, pb.name AS name, pr.est_release_date, e.first_name AS first_name, e.last_name AS last_name, DATEDIFF(pr.est_release_date, CURDATE()) AS remain_days FROM project_basic pb LEFT JOIN project_resource pr ON pr.project_id = pb.id LEFT JOIN employee e ON pr.employee_id = e.id WHERE pb.type = 'Dedicated' AND pr.billable = 1 AND (pb.status != 'Signed off' AND pb.status != 'Paused') AND DATEDIFF(pr.est_release_date, CURDATE()) <= 7 GROUP BY pr.project_id, pr.employee_id ORDER BY pb.name ASC;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Which projects require invoices for employees under hire within the next week?",
        "SQLQuery": "SELECT pb.id AS project_id, pb.name AS project_name, pr.est_release_date, e.first_name, e.last_name, DATEDIFF(pr.est_release_date, CURDATE()) AS remain_days FROM project_basic pb LEFT JOIN project_resource pr ON pr.project_id = pb.id LEFT JOIN employee e ON pr.employee_id = e.id WHERE pb.type = 'Dedicated' AND pr.billable = 1 AND (pb.status != 'Signed off' AND pb.status != 'Paused') AND DATEDIFF(pr.est_release_date, CURDATE()) <= 7 GROUP BY pr.project_id, pr.employee_id ORDER BY pb.name ASC;",
        "SQLResult": "",
        "Answer": "",
    },
    {
        "Question": "Whats for lunch today?",
        "SQLQuery": "SELECT menu FROM lunch_menu LIMIT 1;",
        "SQLResult": "[('<p>Refill your plate again if you want but please do not waste food "
        "🙏🏻😇</p><p><strong><u>WEEKLY FOOD MENU</u></strong></p><ul><li><strong>Monday</strong></li"
        "></ul><ol type='1'><li>Flawer vatana tameta </li><li>White chaula </li><li>Magani...',)]",
        "Answer": "",
    },
    {
        "Question": "Whats for lunch tomorrow?",
        "SQLQuery": "SELECT menu FROM lunch_menu LIMIT 1;",
        "SQLResult": "[('<p>Refill your plate again if you want but please do not waste food "
        "🙏🏻😇</p><p><strong><u>WEEKLY FOOD MENU</u></strong></p><ul><li><strong>Monday</strong></li"
        "></ul><ol type='1'><li>Flawer vatana tameta </li><li>White chaula </li><li>Magani...',)]",
        "Answer": "",
    },
    {
        "Question": "Whose birthday is it today?",
        "SQLQuery": "SELECT employee_code, first_name, last_name FROM employee WHERE Day(dob) = Day(Curdate()) AND "
        "Month(dob) = Month(Curdate());",
        "SQLResult": "[('MI-197', 'Faiyaz', 'Meghreji'), ('MI-475', 'Yash', 'Malaviya'), ('MI-489', 'Rita', 'Chauhan')]",
        "Answer": "Faiyaz Meghreji, Yash Malaviya and Rita Chauhan's birthday is today.",
    },
    {
        "Question": "Whose birthday was yesterday?",
        "SQLQuery": "SELECT employee_code, first_name, last_name FROM   employee WHERE  Date_add(dob, INTERVAL Year("
        "CURRENT_DATE()) - Year(dob) YEAR) =        DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY);",
        "SQLResult": "[('MI-433', 'Khushali', 'Patel')]",
        "Answer": "Khushali Patel's birthday was yesterday.",
    },
    {
        "Question": "Whose birthday was last week?",
        "SQLQuery": "SELECT employee_code, first_name, last_name FROM employee WHERE  Date_add(dob, INTERVAL Year(CURRENT_DATE()) - Year(dob)YEAR) BETWEEN Date_sub(CURRENT_DATE(), INTERVAL 7 DAY) AND CURRENT_DATE();",
        "SQLResult": "[('MI-270', 'Kalpesh', 'Thakar'), ('MI-512', 'Ashutosh', 'Kaushik'), ('MI-341', 'Jagdish', 'Paryani'), ('MI-447', 'Priyanka', 'Vasant'), ('MI-499', 'Ubbad', 'Mansuri')]",
        "Answer": "The following employees had their birthday last week:- Kalpesh Thakar- Ashutosh Kaushik- Jagdish Paryani- Priyanka Vasant- Ubbad Mansuri",
    },
    {
        "Question": "Whose birthday is next week?",
        "SQLQuery": "SELECT employee_code, first_name, last_name FROM employee WHERE Date_add(dob, INTERVAL Year(CURRENT_DATE()) - Year(dob) year) between CURRENT_DATE() AND Date_add(CURRENT_DATE(), INTERVAL 7 day);",
        "SQLResult": "[('MI-354', 'Deep', 'Bhavsar'), ('MI-512', 'Ashutosh', 'Kaushik'), ('MI-197', 'Faiyaz','Meghreji'), ('MI-243', 'Keval', 'Senghani')]",
        "Answer": "The following employees have their birthday next week:- Deep Bhavsar- Ashutosh Kaushik- Faiyaz Meghreji- Keval Senghani",
    },
    {
        "Question": "Whose birthday is tomorrow?",
        "SQLQuery": "SELECT employee_code, first_name, last_name FROM employee WHERE Date_add(dob, INTERVAL Year(CURRENT_DATE()) - Year(dob) YEAR) = DATE_ADD(CURRENT_DATE(), INTERVAL 1 DAY);",
        "SQLResult": "[('MI-354', 'Deep', 'Bhavsar'), ('MI-512', 'Ashutosh', 'Kaushik'), ('MI-197', 'Faiyaz','Meghreji'), ('MI-243', 'Keval', 'Senghani')]",
        "Answer": "The following employees have their birthday tomorrow:- Deep Bhavsar- Ashutosh Kaushik- Faiyaz Meghreji- Keval Senghani",
    },
    {
        "Question": "Whose Anniversary is today?",
        "SQLQuery": "SELECT employee_code, first_name,last_name from employee WHERE Day(join_date) = Day(Curdate()) AND Month(join_date) = Month(Curdate());",
        "SQLResult": "[('MI-516', 'Ujjawal', 'Roy'), ('MI-488', 'Vatsal', 'Gamit')]",
        "Answer": "The following employees had their work anniversaries today:- Ujjawal Roy- Vatsal Gamit",
    },
    {
        "Question": "Whose Anniversary was last week?",
        "SQLQuery": "SELECT employee_code, first_name, last_name, join_date from employee where Date_add(join_date, INTERVAL Year(CURRENT_DATE()) - Year(join_date) YEAR) between Date_sub(CURRENT_DATE(), INTERVAL 7 DAY) AND CURRENT_DATE();",
        "SQLResult": "[('MI-354', 'Deep', 'Bhavsar'), ('MI-512', 'Ashutosh', 'Kaushik'), ('MI-197', 'Faiyaz','Meghreji'), ('MI-243', 'Keval', 'Senghani')]",
        "Answer": "The following employees had their work anniversaries last week:- Deep Bhavsar- Ashutosh Kaushik- Faiyaz Meghreji- Keval Senghani",
    },
    {
        "Question": "How many leaves do I have? employee_code of user querying=MI-488",
        "SQLQuery": "SELECT sum(balance) FROM leave_balance WHERE employee_id IN (SELECT id FROM employee WHERE employee_code = 'MI-488');",
        "SQLResult": "[(11.0,)]",
        "Answer": "You have 11 total leaves.",
    },
    {
        "Question": "Whose Anniversary is in the next week?",
        "SQLQuery": "SELECT employee_code, first_name, last_name, join_date FROM   employee WHERE  Date_add(join_date, INTERVAL Year(CURRENT_DATE()) - Year(join_date) year) BETWEEN CURRENT_DATE() AND Date_add(CURRENT_DATE(), INTERVAL 7 day);",
        "SQLResult": "[('MI-354', 'Deep', 'Bhavsar'), ('MI-512', 'Ashutosh', 'Kaushik'), ('MI-197', 'Faiyaz','Meghreji'), ('MI-243', 'Keval', 'Senghani')]",
        "Answer": "The following employees had their work anniversaries next week:- Deep Bhavsar- Ashutosh Kaushik- Faiyaz Meghreji- Keval Senghani",
    },
    {
        "Question": "Whose Anniversary is tomorrow?",
        "SQLQuery": "SELECT employee_code, first_name, last_name, join_date FROM   employee WHERE  Date_add(join_date, INTERVAL Year(CURRENT_DATE()) - Year(join_date) YEAR) = DATE_ADD(CURRENT_DATE(), INTERVAL 1 DAY);",
        "SQLResult": "[('MI-354', 'Deep', 'Bhavsar'), ('MI-512', 'Ashutosh', 'Kaushik'), ('MI-197', 'Faiyaz','Meghreji'), ('MI-243', 'Keval', 'Senghani')]",
        "Answer": "The following employees had their work anniversaries tomorrow:- Deep Bhavsar- Ashutosh Kaushik- Faiyaz Meghreji- Keval Senghani",
    },
]

print(len(emp_profile_few_shots))
