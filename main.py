from langchain_google_genai import GoogleGenerativeAI
from langchain.utilities.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

api_key = 'AIzaSyA5npGkRSAWoCt4P93ztBzl0o2lIk8GOnI'

llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key)

db = SQLDatabase.from_uri("mysql://root:password@localhost/mrms", include_tables=['employee_profile'])

#print(db.table_info)

db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
qns1 = db_chain.invoke({"query": "List all people under Samar Patel along with their experience in years"})
