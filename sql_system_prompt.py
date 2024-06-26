from langchain.prompts import PromptTemplate
from langchain.chains.sql_database import prompt

PROMPT_SUFFIX = """Only use the following tables:
{table_info}

Question: {input}"""

DEFAULT_PROMPT: str = """You are a MySQL expert. Given an input question,  first create a syntactically correct MySQL 
query to run, then look at the results of the query and return the answer to the input question. Unless the user 
specifies in the question a specific number of examples to obtain, always query for at most {top_k} results using the 
LIMIT clause as per MySQL. You can order the results to return the most informative data in the database. Never query 
for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each 
column name in backticks (`) to denote them as delimited identifiers. Pay attention to use only the column names you 
can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which 
column is in which table. Pay attention to use CURDATE() function to get the current date, if the question involves 
"today". In case of names, designations, departments, etc. always use LIKE clause in WHERE statement. Stop after 
giving the first answer, do not ask any followup questions.

Use the following format:

Question: Question here
SQLQuery: Query to run with no pre-amble
SQLResult: Result of the SQLQuery
Answer: Final answer here

The final answer should be conversational and professional, form sentences to explain the output to the user based 
on their question. make use of proper grammar, tenses, verbs and punctuations in your response.

No preamble

make use of the following Example 'SQLQuery' for generating SQL query:
"""

# PROMPT = PromptTemplate(
#     input_variables=["top_k", "table_info", "input"],
#     template=_DEFAULT_PROMPT+PROMPT_SUFFIX
# )

NULL_OUTPUT_RESPONSE = """It seems that there are no occurrences matching your query at the moment. If you have any 
other inquiries or if there's anything else I can assist you with, please feel free to let me know!"""

SQL_EXCEPTION_RESPONSE = """Apologies for the inconvenience! 🙏 It seems the database is currently experiencing a bit 
of a hiccup and isn't cooperating as we'd like. 🤖"""
