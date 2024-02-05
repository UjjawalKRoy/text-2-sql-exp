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
        'Answer': "Beant Duggal is a VP in Sales, with total experience of 953 days. He has been with the company for 838 days, and has a total leave balance of 50 days. His manager is Samar Patel."
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
        'Answer': "Tirth Shah is an Associate Software Engineer in the Web department. His employee code is MI-510 and his email address is tirth.shah@mailinator.com."
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
]
print(len(emp_profile_few_shots))
