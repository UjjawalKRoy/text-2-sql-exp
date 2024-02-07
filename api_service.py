from fastapi import FastAPI, HTTPException, status, Body, Response
from pydantic import BaseModel

app = FastAPI()

class UserQuery(BaseModel):
    user: str
    query: str
    intent: str
    role: str
    tables: list[str]
@app.get("/")
async def root():
    return "The API is running!"

@app.post("/ask")
async def ask(user_query: UserQuery):
    user = user_query.user
    query = user_query.query
    table_names = user_query.tables
    role = user_query.role
