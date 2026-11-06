from fastapi import FastAPI, status
from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    query: str = Field(
        min_length=1,
        max_length=300,
    )


app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "welcome to the world server"}

@app.get("/health")
async def health():
    return {"message" : "Good Condition", "status" : status.HTTP_200_OK}


@app.post("/query")
async def query(item : QueryRequest):
    return {
        "query" : item.query,
        "message" : "query recieved"
    }
