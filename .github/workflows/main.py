from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

@app.get("/")
def read_root():
    # Перевірка з'єднання з БД через змінні оточення
    dbname = os.getenv("POSTGRES_DB")
    return {"status": "API is running", "database": dbname}