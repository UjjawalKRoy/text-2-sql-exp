from langchain.chains.sql_database.prompt import PROMPT_SUFFIX
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.prompts.prompt import PromptTemplate
from langchain.utilities.sql_database import SQLDatabase
from langchain_community.vectorstores import Chroma
from langchain_experimental.sql import SQLDatabaseChain
from langchain_google_genai import GoogleGenerativeAI

import system_prompt
from examples import emp_profile_few_shots
from ques import ques

import langchain

langchain.verbose = True

api_key = 'AIzaSyA5npGkRSAWoCt4P93ztBzl0o2lIk8GOnI'
llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key)

# callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
# llm = LlamaCpp(
#     model_path="C:/Users/admin/.cache/lm-studio/models/TheBloke/nsql-llama-2-7B-GGUF/nsql-llama-2-7b.Q8_0.gguf",
#     n_ctx=8000,
#     n_gpu_layers=40,
#     n_threads=8,
#     n_batch=512,
#     max_tokens=200,
#     temperature=0.8,
#     top_p=0.1,
#     callback_manager=callback_manager
# )


# print(db.table_info)
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
to_vectorize = [" ".join(example.values()) for example in emp_profile_few_shots]
vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=emp_profile_few_shots)
example_selector = SemanticSimilarityExampleSelector(
    vectorstore=vectorstore,
    k=2,
)

example_prompt = PromptTemplate(
    input_variables=["Question", "SQLQuery", "SQLResult", "Answer", ],
    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
)

few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=system_prompt.DEFAULT_PROMPT,
    suffix=PROMPT_SUFFIX,
    input_variables=["input", "table_info", "top_k"],  # These variables are used in the prefix and suffix
)


def create_db_chain(tables: list[str], query: str):
    db = SQLDatabase.from_uri("mysql://root:password@localhost/mrms", include_tables=tables)
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt, return_direct=True)
    # for q in ques:
    #     db_chain.invoke({"query": q})
    qns1 = db_chain.invoke({"query": query})
    res = qns1["result"]
    if not res:
        return None
    return {"result": res}


if __name__ == "__main__":
    tabs = ['employee', 'leave_application', 'wfh_application', 'employee_occupancy', 'department_type',
            'issue_work_log',
            'attendance_event', 'lunch_menu', 'leave_balance']
    create_db_chain(tables=tabs, query="Who has not filled their logs today?")
