from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

from main import create_db_chain, logger
from generic_chain import get_generic_response

app = FastAPI()


class UserQuery(BaseModel):
    user: str
    query: str
    intent: str
    role: str
    tables: Optional[list[str]]
    entities: Optional[list[dict]]
    is_generic: Optional[bool]


@app.get("/")
async def root():
    return "The API is running!"


@app.post("/ask")
async def ask(user_query: UserQuery):
    user = user_query.user
    query = user_query.query
    table_names = user_query.tables
    role = user_query.role
    intent = user_query.intent
    entities = user_query.entities
    is_generic = user_query.is_generic
    print("entities==============================>", entities)
    if is_generic is None:
        is_generic = False
    print(f"Query: {query} | Intent: {intent}")
    logger.info(f"Query: {query} | Intent: {intent} | is_generic: {is_generic}")
    if is_generic:
        res = get_generic_response(query=query)
        return {"result": res}
    else:
        if entities:
            for doc in entities:
                if doc['entity'].lower() == 'person' and (doc['value'].lower() in ['my', 'i', 'myself', 'me', 'mine']):
                    query = query + f" Remember, my employee_code='{user}'"
        if role.lower() == "own":
            return create_db_chain(
                tables=table_names, query=f"{query} employee_code of user querying={user}"
            )
        return create_db_chain(tables=table_names, query=query)
