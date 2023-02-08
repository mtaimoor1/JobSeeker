from fastapi import FastAPI
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
    logging.info(f"Table Name: {table} Job Title {job}")
    return dynamo.query_table(table, job)


@app.get('/records/{table}')
def get_all_items(table: str):
    return dynamo.get_all_records(table)

