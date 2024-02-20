from typing import Optional, List
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
async def root() -> object:
    """

    :return: 
    """
    return "The API is running!"


@app.post("/ask")
async def ask(user_query: UserQuery) -> object:
    """

    :rtype: object
    :return: 
    :type user_query: object
    """
    user: str = user_query.user
    query: str = user_query.query
    table_names: Optional[list[str]] = user_query.tables
    role: str = user_query.role
    intent: str = user_query.intent
    entities: Optional[list[dict]] = user_query.entities
    is_generic: Optional[bool] = user_query.is_generic
    print("entities==============================>", entities)
    if is_generic is None:
        is_generic = False
    logger.info(
        f"NEW CHAIN STARTS HERE"
        f"{'='*150}\nQuery: {query} | Intent: {intent} | is_generic: {is_generic}")
    if is_generic:
        res = get_generic_response(query=query)
        return {"result": res}
    else:
        if entities:
            for doc in entities:
                if doc['entity'].lower() == 'person' and (doc['value'].lower() in {"my", 'i', 'myself', 'me', 'mine',
                                                                                   "i'm"}):
                    query = f"{query} Remember, my employee_code='{user}'"
        if role.lower() == "own":
            return create_db_chain(
                tables=table_names, query=f"{query} employee_code of user querying={user}"
            )
        return create_db_chain(tables=table_names, query=query)
