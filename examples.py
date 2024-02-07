emp_profile_few_shots = [
    {
        'Question': "I need Vatsal Gamit's contact details?",
        'SQLQuery': "SELECT email_id FROM employee_profile WHERE employee_name = 'Vatsal Gamit'",
        'SQLResult': "[('vatsal.gamit@mailinator.com',)]",
        'Answer': "vatsal.gamit@mailinator.com"
    },
    {
        'Question': "How many leaves does Hasmukh Suthar have?",
        'SQLQuery': "SELECT total_leave_balance FROM employee_profile WHERE employee_name = 'Hasmukh Suthar'",
        'SQLResult': "[(10.0,)]",
        'Answer': "10"
    },
    {
        'Question': "How many people with more than 800 days of experience report to Samar Patel?",
        'SQLQuery': "SELECT count(*) FROM employee_profile WHERE reporting_manager = 'Samar Patel' AND total_experience > 800",
        'SQLResult': "[(3,)]",
        'Answer': "3"
    },
    {
        'Question': "List all people with more than 800 days of experience report to Samar Patel",
        'SQLQuery': "SELECT employee_name, total_experience FROM employee_profile WHERE total_experience > 800 AND reporting_manager = 'Samar Patel'",
        'SQLResult': "Beant Duggal, Anish Panchal, Dhruv Mevada",
        'Answer': "3"
    },
    {
        'Question': "Brief me about Beant Duggal",
        'SQLQuery': "SELECT * FROM employee_profile WHERE employee_name = 'Beant Duggal'",
        'SQLResult': "[(14, 'Beant Duggal', 'MI-160', 'beant.duggal@mailinator.com', datetime.datetime(1989, 2, 24, 0, 0), None, 'Sales', 'VP', 50.0, 'Samar Patel', 953)]",
        'Answer': "Beant Duggal is a VP in Sales, with total experience of 953 days. He has been with the "
                  "company "
                  "for 838 days, and has a total leave balance of 50 days. His manager is Samar Patel."
    },
    {
        'Question': "How many people with more than 500 days of experience work under Mehul Rajput or Asha Rajput?",
        'SQLQuery': "SELECT COUNT(*) FROM employee_profile WHERE reporting_manager IN ('Mehul Rajput', 'Asha Rajput') AND total_experience > 500",
        'SQLResult': "[(6,)]",
        'Answer': "6"
    },
    {
        'Question': "How many years of experience does Ujjawal Roy have?",
        'SQLQuery': "SELECT total_experience FROM employee_profile WHERE employee_name = 'Ujjawal Roy'",
        'SQLResult': "[(137,)]",
        'Answer': "137 days"
    },
    {
        'Question': "Who is the reporting manager of Nency Patel?",
        'SQLQuery': "SELECT reporting_manager FROM employee_profile WHERE employee_name = 'Nency Patel'",
        'SQLResult': "[('Kumar Pal Nagar',)]",
        'Answer': "Kumar Pal Nagar"
    },
    {
        'Question': "Who is Tirth Shah?",
        'SQLQuery': "SELECT * FROM employee_profile WHERE employee_name = 'Tirth Shah'",
        'SQLResult': "[(53, 'Tirth Shah', 'MI-510', 'tirth.shah@mailinator.com', datetime.datetime(1999, 5, 28, 0, 0), None, 'Web', 'Associate Software Engineer', 23.5, 'Nilesh Patel', 793)]",
        'Answer': "Tirth Shah is an Associate Software Engineer in the Web department. His employee code is "
                  "MI-510 "
                  "and his email address is tirth.shah@mailinator.com."
    },
    {
        'Question': "What is the average experience of employees working in the web department?",
        'SQLQuery': "SELECT AVG(total_experience) FROM employee_profile WHERE department_name = 'Web'",
        'SQLResult': "[(Decimal('635.1282'),)]",
        'Answer': "635.1282"
    },
    {
        'Question': "How many people work in marketing?",
        'SQLQuery': "SELECT COUNT(*) FROM employee_profile WHERE department_name = 'Marketing'",
        'SQLResult': "[(16,)]",
        'Answer': "16"
    },
    {
        'Question': "Whose birthday is it today?",
        'SQLQuery': "SELECT employee_name, [dob] FROM TABLE WHERE DAY([dob]) = DAY(GETDATE()) AND MONTH([dob]) = MONTH(GETDATE())",
        'SQLResult': "[(Khushali Patel,)]",
        'Answer': "Khushali Patel"
    },
    {
        'Question': "Total strength of Mobile department",
        'SQLQuery': "SELECT COUNT(*) AS total_strength FROM employee_profile WHERE department_name = 'Mobile'",
        'SQLResult': "[(66,)]",
        'Answer': "66"
    },
    {
        'Question': "Is Vismit Suvagya working in Mobile department",
        'SQLQuery': "SELECT department_name FROM employee_profile WHERE employee_name='Vismit Suvagya'",
        'SQLResult': "[('Web',)]",
        'Answer': "no"
    },
    {
        'Question': "What is the total strength of sales and marketing",
        'SQLQuery': "SELECT count(employee_id) FROM employee_profile WHERE department_name = 'Sales' OR department_name = 'Marketing'",
        'SQLResult': "[(41,)]",
        'Answer': "41"
    },
    {
        'Question': "List all employees under Mehul Rajput who have not filled their time sheet",
        'SQLQuery': "SELECT employee_name FROM employee_profile WHERE reporting_manager = 'Mehul Rajput' AND timesheet_filling_status = 'not filled' LIMIT 5",
        'SQLResult': "[('Mehul Rajput',), ('Samar Patel',), ('Kalpesh Thakar',), ('Asha Rajput',)]",
        'Answer': "Mehul Rajput, Samar Patel, Kalpesh Thakar, Asha Rajput"
    },
    {
        'Question': "Employees working under which reporting managers have not filled their time sheets",
        'SQLQuery': "SELECT reporting_manager FROM employee_profile WHERE timesheet_filling_status = 'not filled'",
        'SQLResult': "[('System Admin',), ('Mehul Rajput',), ('Mehul Rajput',), ('Mehul Rajput',), ('Mehul Rajput',), ('Bhumi Goklani',)]",
        'Answer': "System Admin, Mehul Rajput, Bhumi Goklani"
    },
    {
        'Question': "I need 5 devs who know mysql",
        'SQLQuery': "SELECT employee_name FROM employee_profile WHERE employee_skill LIKE '%mysql%' LIMIT 5",
        'SQLResult': "[('Rahul Gauswami',), ('Hitesh Darji',), ('Mohammadtufel Jerawala',), ('Kamalrajsinh Sodha',), ('Arati Bhadani',)]",
        'Answer': "Rahul Gauswami, Hitesh Darji, Mohammadtufel Jerawala, Kamalrajsinh Sodha, Arati Bhadani"
    },
    {
        'Question': "Is Krishna Thakkar skilled in python?",
        'SQLQuery': "SELECT employee_skill FROM employee_profile WHERE employee_name = 'Krishna Thakkar'",
        'SQLResult': "[('MongoDB, Data Analysis, FastAPI - Python,)]",
        'Answer': "Yes"
    },
    {
        'Question': "Which department does Ujjawal Roy works in?",
        'SQLQuery': "SELECT department_name FROM employee_profile WHERE employee_name = 'Ujjawal Roy'",
        'SQLResult': "[('Data Science & AI/ML',)]",
        'Answer': "Data Science & AI/ML"
    },
    {
        'Question': "Brief me about MI-516",
        'SQLQuery': "SELECT * FROM employee_profile WHERE employee_code = 'MI-516'",
        'SQLResult': "[('MI-516', 'Ujjawal Roy', 'ujjawal.roy@mailinator.com', datetime.datetime(1997, 12, 12, 0, 0), 'B+', None, 'https://github.com/UjjawalKRoy', 'Mindinventory', 'on probation', 'Data Science & AI/ML', 'Data Scientist', 0.0, 'Samar Patel', 138, 'Artificial Intelligence, Computer Vision, Neural Network Architectures, Python for Data Science CNN, LLM, LLM, 'filled')]",
        'Answer': "Data Science & AI/ML"
    },
    {
        'Question': "How many Python devs do we have?",
        'SQLQuery': "SELECT COUNT(*) FROM employee_profile WHERE employee_skill LIKE '%Python%'",
        'SQLResult': "[(9,)]",
        'Answer': "9"
    },
    {
        'Question': "Has Nency Patel filled her logs?",
        'SQLQuery': "SELECT timesheet_filling_status FROM employee_profile WHERE employee_name = 'Nency Patel'",
        'SQLResult': "[('filled',)]",
        'Answer': "filled"
    },
    {
        'Question': "Who is the CEO of MindInventory?",
        'SQLQuery': "SELECT employee_name FROM employee_profile WHERE job_title = 'CEO' AND business_unit_name = 'MindInventory'",
        'SQLResult': "[('Mehul Rajput',),]",
        'Answer': "Mehul Rajput"
    },
    {
        'Question': "I need 3 devs who are proficient in python and sql",
        'SQLQuery': "SELECT employee_name FROM employee_profile WHERE employee_skill LIKE '%python%' AND employee_skill LIKE '%sql%' LIMIT 3",
        'SQLResult': "[('Hasmukh Suthar',)]",
        'Answer': "Hasmukh Suthar"
    },
    {
        'Question': "Who all are in probation?",
        'SQLQuery': "SELECT employee_name FROM employee_profile WHERE employment_status = 'on probation'",
        'SQLResult': "",
        'Answer': "None"
    },
    {
        'Question': "Who is on leave today?",
        'SQLQuery': "SELECT e.first_name, e.last_name FROM employee e JOIN leave_application l ON e.id = l.employee_id WHERE l.from_date <= CURDATE() AND l.to_date >= CURDATE() AND l.leave_status = 2;",
        'SQLResult': "[(Ujjawal, Roy,), (Siddhant, Pandey, )]",
        'Answer': "Ujjawal Roy and Siddhant Pandey are on leave today."
    },
    {
        'Question': "Who is on leave this week?",
        'SQLQuery': "SELECT e.first_name, e.last_name FROM employee e JOIN leave_application l ON e.id = l.employee_id WHERE l.from_date BETWEEN DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) AND DATE_ADD(DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY), INTERVAL 7 DAY) AND   l.to_date   BETWEEN DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) AND DATE_ADD(DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY), INTERVAL 7 DAY) AND    l.leave_status =2;",
        'SQLResult': "[(Ujjawal, Roy,), (Siddhant, Pandey, ), (Vatsal, Gamit, )]",
        'Answer': "Ujjawal Roy, Siddhant Pandey and Vatsal Gamit are on leave this week."
    },
    {
        'Question': "Who is on WFH today?",
        'SQLQuery': "SELECT e.first_name, e.last_name FROM employee e JOIN wfh_application wfh ON e.id = wfh.employee_id WHERE wfh.from_date <= CURDATE() AND wfh.to_date >= CURDATE() AND wfh.status = 2;",
        'SQLResult': "",
        'Answer': "No one is on WFH today"
    },
    {
        'Question': "Who is on WFH this week?",
        'SQLQuery': "SELECT e.first_name, e.last_name FROM employee e JOIN wfh_application wfh ON e.id = wfh.employee_id WHERE wfh.from_date BETWEEN DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) AND DATE_ADD(DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY), INTERVAL 7 DAY) AND   wfh.to_date   BETWEEN DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) AND DATE_ADD(DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY), INTERVAL 7 DAY) AND   wfh.status =2;",
        'SQLResult': "[(Krishna, Thakkar,), (Siddhant, Pandey,), (Sanskar, Mehta,)]",
        'Answer': "Krishna Thakkar, Siddhant Pandey and Sanskar Mehta are on WFH this week"
    },
    {
        'Question': "How many people are free for from each department?",
        'SQLQuery': "SELECT d.name AS department, COUNT(*) AS num_free_employees FROM employee e JOIN employee_occupancy o ON e.id = o.employee_id AND o.occupancy_status IN (0, 1) JOIN department_type d ON e.department_id = d.id GROUP BY d.id;",
        'SQLResult': "[('Design', 11), ('Mobile', 8), ('Game', 8), ('Web', 22), ('Business Analysis', 2), ('DevOps', 1), ('Management', 2)]",
        'Answer': "There are 11 people from Design, 8 from Mobile, 8 from Game, 22 from Web, 2 from Business "
                  "Analysis, 1 from DevOps and 2 from management who are free today"
    },
    {
        'Question': "Who did not fill the logs yesterday?",
        'SQLQuery': "select ae.employee_id, COUNT(*) AS count, ae.event_date_time, e.first_name, e.last_name from attendance_event ae JOIN employee e ON ae.employee_id = e.id LEFT JOIN issue_work_log iwl ON ae.employee_id = iwl.employee_id AND DATE(iwl.spent_date) = DATE_SUB(CURDATE(), INTERVAL 1 DAY) where DATE(ae.event_date_time) = DATE_SUB(CURDATE(), INTERVAL 1 DAY) AND ae.event_type = 0 AND iwl.employee_id IS null GROUP by ae.employee_id;",
        'SQLResult': "[('Mehul', 'Rajput'), ('Samar', 'Patel'), ('Kalpesh', 'Thakar'), ('Kiran', 'Malvi')]",
        'Answer': "The following employee did not fill their daily log yesterday:"
                  "1. Mehul rajput"
                  "2. Samar Patel"
                  "3. Kalpesh Thakkar"
                  "4. Kiran Malvi"
    },
    {
        'Question': "Whats for lunch today?",
        'SQLQuery': "SELECT menu FROM lunch_menu LIMIT 1;",
        'SQLResult': "[(\'<p>Refill your plate again if you want but please do not waste food "
                     "🙏🏻😇</p><p><strong><u>WEEKLY FOOD MENU</u></strong></p><ul><li><strong>Monday</strong></li"
                     "></ul><ol type='1'><li>Flawer vatana tameta </li><li>White chaula </li><li>Magani...',)]",
        'Answer': ""
    },
    {
        'Question': "Whose birthday is it today?",
        'SQLQuery': "SELECT employee_code, first_name, last_name FROM employee WHERE Day(dob) = Day(Curdate()) AND "
                    "Month(dob) = Month(Curdate());",
        'SQLResult': "[('MI-197', 'Faiyaz', 'Meghreji'), ('MI-475', 'Yash', 'Malaviya'), ('MI-489', 'Rita', 'Chauhan')]",
        'Answer': "Faiyaz Meghreji, Yash Malaviya and Rita Chauhan's birthday is today."
    },
    {
        'Question': "Whose birthday was yesterday?",
        'SQLQuery': "SELECT employee_code, first_name, last_name FROM   employee WHERE  Date_add(dob, INTERVAL Year("
                    "CURRENT_DATE()) - Year(dob) YEAR) =        DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY);",
        'SQLResult': "[('MI-433', 'Khushali', 'Patel')]",
        'Answer': "Khushali Patel's birthday was yesterday."
    },
    {
        'Question': "Whose birthday was last week?",
        'SQLQuery': "SELECT employee_code, first_name, last_name FROM employee WHERE  Date_add(dob, INTERVAL Year(CURRENT_DATE()) - Year(dob)YEAR) BETWEEN Date_sub(CURRENT_DATE(), INTERVAL 7 DAY) AND CURRENT_DATE();",
        'SQLResult': "[('MI-270', 'Kalpesh', 'Thakar'), ('MI-512', 'Ashutosh', 'Kaushik'), ('MI-341', 'Jagdish', 'Paryani'), ('MI-447', 'Priyanka', 'Vasant'), ('MI-499', 'Ubbad', 'Mansuri')]",
        'Answer': "The following employees had their birthday last week:- Kalpesh Thakar- Ashutosh Kaushik- Jagdish Paryani- Priyanka Vasant- Ubbad Mansuri"
    },
    {
        'Question': "Whose birthday is next week?",
        'SQLQuery': "SELECT employee_code, first_name, last_name FROM employee WHERE Date_add(dob, INTERVAL Year(CURRENT_DATE()) - Year(dob) year) between CURRENT_DATE() AND Date_add(CURRENT_DATE(), INTERVAL 7 day);",
        'SQLResult': "[('MI-354', 'Deep', 'Bhavsar'), ('MI-512', 'Ashutosh', 'Kaushik'), ('MI-197', 'Faiyaz','Meghreji'), ('MI-243', 'Keval', 'Senghani')]",
        'Answer': "The following employees have their birthday next week:- Deep Bhavsar- Ashutosh Kaushik- Faiyaz Meghreji- Keval Senghani"
    },
    {
        'Question': "Whose birthday is tomorrow?",
        'SQLQuery': "SELECT employee_code, first_name, last_name FROM employee WHERE Date_add(dob, INTERVAL Year(CURRENT_DATE()) - Year(dob) YEAR) = DATE_ADD(CURRENT_DATE(), INTERVAL 1 DAY);",
        'SQLResult': "[('MI-354', 'Deep', 'Bhavsar'), ('MI-512', 'Ashutosh', 'Kaushik'), ('MI-197', 'Faiyaz','Meghreji'), ('MI-243', 'Keval', 'Senghani')]",
        'Answer': "The following employees have their birthday tomorrow:- Deep Bhavsar- Ashutosh Kaushik- Faiyaz Meghreji- Keval Senghani"
    },
    {
        'Question': "Whose Anniversary is today?",
        'SQLQuery': "SELECT employee_code, first_name,last_name from employee WHERE Day(join_date) = Day(Curdate()) AND Month(join_date) = Month(Curdate());",
        'SQLResult': "[('MI-516', 'Ujjawal', 'Roy'), ('MI-488', 'Vatsal', 'Gamit')]",
        'Answer': "The following employees had their work anniversaries today:- Ujjawal Roy- Vatsal Gamit"
    },
    {
        'Question': "Whose Anniversary was last week?",
        'SQLQuery': "SELECT employee_code, first_name, last_name, join_date from employee where Date_add(join_date, INTERVAL Year(CURRENT_DATE()) - Year(join_date) YEAR) between Date_sub(CURRENT_DATE(), INTERVAL 7 DAY) AND CURRENT_DATE();",
        'SQLResult': "[('MI-354', 'Deep', 'Bhavsar'), ('MI-512', 'Ashutosh', 'Kaushik'), ('MI-197', 'Faiyaz','Meghreji'), ('MI-243', 'Keval', 'Senghani')]",
        'Answer': "The following employees had their work anniversaries last week:- Deep Bhavsar- Ashutosh Kaushik- Faiyaz Meghreji- Keval Senghani"
    },
    {
        'Question': "How many leaves do I have? employee_code of user querying=MI-488",
        'SQLQuery': "SELECT sum(balance) FROM leave_balance WHERE employee_id IN (SELECT id FROM employee WHERE employee_code = 'MI-488');",
        'SQLResult': "[(11.0,)]",
        'Answer': "You have 11 total leaves."
    },
]
print(len(emp_profile_few_shots))
