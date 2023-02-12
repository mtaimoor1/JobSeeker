from fastapi import FastAPI, HTTPException, status
from utils.dynamodb.query_dynamo import DynamoQuery
import sys
import os
import logging

logging.basicConfig(
    stream=sys.stdout,
    level=os.environ.get('LOGLEVEL', 'INFO').upper(),
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

app = FastAPI()
dynamo = DynamoQuery()


@app.get('/list_tables')
def get_tables():
    return dynamo.list_tables()


@app.get("/records")
def get_filtered_record(table: str, job: str):
    result = dynamo.query_table(table, job)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with title {job} not found in the table {table}")
    if result[0].get("Code", "") == "ResourceNotFoundException":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Resource not found check the table name")
    return result


@app.get('/records/{table}')
def get_all_items(table: str):
    response = dynamo.get_all_records(table)
    if response[0].get("Code", "") == "ResourceNotFoundException":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Resource not found check the table name")
    return response
