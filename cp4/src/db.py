import psycopg2
import pandas as pd

def connect():
    return psycopg2.connect(
        host = "codd04.research.northwestern.edu",
        database = "postgres",
        user = "cpdbstudent",
        password = "DataSci4AI",
        port = 5433,
    )

def tables():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    return pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

def download(tablename):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {tablename};")
    return pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
