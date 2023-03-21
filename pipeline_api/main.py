from fastapi import FastAPI, HTTPException, status
from utils.mongoDB.query_mongo import MongoQuery
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
mongo = MongoQuery()


@app.get('/list_tables')
def get_tables():
    return mongo.list_tables()


@app.get("/records")
def get_filtered_record(table: str, job: str):
    result = mongo.query_table(table, job)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with title {job} not found in the table {table}")
    return result


@app.get('/records/{table}')
def get_all_items(table: str):
    return mongo.get_all_records(table)
