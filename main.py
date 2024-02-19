import ast

import langchain
import pandas as pd
from loguru import logger
from langchain.chains import LLMChain
from langchain.callbacks import FileCallbackHandler
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.prompts.prompt import PromptTemplate
from langchain.utilities.sql_database import SQLDatabase
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_experimental.sql import SQLDatabaseChain
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from pandas import DataFrame

import sql_system_prompt
from examples import emp_profile_few_shots
from prompts import RESPONDER_PROMPT
import os

logfile = "output.log"
load_dotenv(dotenv_path=".env")
logger.add(logfile, colorize=True, enqueue=True)
handler = FileCallbackHandler(logfile)
langchain.verbose = True

api_key = os.getenv("API_KEY")

sqllm = GoogleGenerativeAI(
    model="models/text-bison-001", google_api_key=api_key, temperature=0.1, max_output_tokens=2000
)

llm = GoogleGenerativeAI(
    model="models/text-bison-001", google_api_key=api_key, temperature=0.8, max_output_tokens=5000
)

embeddings = HuggingFaceEmbeddings(model_name="WhereIsAI/UAE-Large-V1")
to_vectorize = [" ".join(example.values()) for example in emp_profile_few_shots]
vectorstore = Chroma.from_texts(
    to_vectorize, embeddings, metadatas=emp_profile_few_shots
)
example_selector = SemanticSimilarityExampleSelector(
    vectorstore=vectorstore,
    k=2,
)

example_prompt = PromptTemplate(
    input_variables=[
        "Question",
        "SQLQuery",
        "SQLResult",
        "Answer",
    ],
    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
)

few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=sql_system_prompt.DEFAULT_PROMPT,
    suffix=PROMPT_SUFFIX,
    input_variables=[
        "input",
        "table_info",
        "top_k",
    ],  # These variables are used in the prefix and suffix
)
final_prompt = PromptTemplate(
    input_variables=["context", "query"], template=RESPONDER_PROMPT
)
final_chain = LLMChain(llm=llm, prompt=final_prompt, callbacks=[handler])


def respond(query: str, context: list):
    p = final_prompt.format(query=query, context=context)
    logger.info(p)
    try:
        ans = final_chain.predict(query=query, context=context)
        logger.info(ans)
        return ans
    except Exception as e:
        logger.info(f'Exception raised in respond() function: {e}')
        data = ast.literal_eval(str(context))
        columns = [f'column{i}' for i in range(len(data[0]))]
        context_df: DataFrame = pd.DataFrame(data=data, columns=columns, index=None)
        return str(context_df.to_dict())


def create_db_chain(tables: list[str], query: str):
    db = SQLDatabase.from_uri(
        "mysql://langchain:password@localhost/mrms", include_tables=tables
    )
    db_chain = SQLDatabaseChain.from_llm(
        sqllm,
        db,
        verbose=True,
        prompt=few_shot_prompt,
        return_direct=True,
        callbacks=[handler],
        top_k=8
    )

    try:
        qns1 = db_chain.invoke({"query": query})
    except Exception as e:
        logger.info(e)
        qns1 = {"result": [sql_system_prompt.SQL_EXCEPTION_RESPONSE]}
    res = qns1["result"]
    logger.info(res)
    if not res:
        res = sql_system_prompt.NULL_OUTPUT_RESPONSE
    result = respond(query=query, context=res)
    print(result)
    return {"result": result}


if __name__ == "__main__":
    tabs = [
        "employee",
        "leave_application",
        "wfh_application",
        "employee_occupancy",
        "department_type",
        "issue_work_log",
        "attendance_event",
        "lunch_menu",
        "leave_balance",
    ]
    create_db_chain(tables=tabs, query="Who has not filled their logs today?")
