from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from main import create_db_chain

app = FastAPI()


class UserQuery(BaseModel):
    user: str
    query: str
    intent: str
    role: str
    tables: Optional[list[str]]
    entities: Optional[list]


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
    print(f"Query: {query} | Intent: {intent}")
    if role.lower() == "own":
        return create_db_chain(
            tables=table_names, query=f"{query} employee_code of user querying={user}"
        )
    return create_db_chain(tables=table_names, query=query)
