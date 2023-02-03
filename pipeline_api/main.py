import uvicorn
from fastapi import FastAPI
from utils.dynamodb.query_dynamo import DynamoQuery

app = FastAPI()
dynamo = DynamoQuery()


@app.get('/list_tables')
def get_tables():
    return dynamo.list_tables()


@app.get('/records_all/{table}')
def get_all_items(table: str):
    return dynamo.get_all_records(table)

