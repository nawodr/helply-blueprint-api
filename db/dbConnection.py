import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

def create_con():
    db = mysql.connector.connect(
        database="helply",
        host="127.0.0.1",
        user="root",
        password="12345678"
    )
    return db


def create_con_pandas():
    db_connection_str = 'mysql+mysqlconnector://root:12345678@127.0.0.1/helply'
    db = create_engine(db_connection_str)
    return db


def insert_data_pandas_df(pd_df, table_name):
    db = create_con_pandas()
    pd_df.to_sql(name=table_name, con=db, if_exists='append', index=False)


def get_data_sql(sql):
    db = create_con_pandas()
    return pd.read_sql_query(sql=sql, con=db)


def insert_data_json(sql_query):
    db = create_con()
    cursor = db.cursor()
    cursor.execute(sql_query)
    db.commit()
    db.close()
    return "INFO: insert successful"


def insert_data(sql_query):
    db = create_con()
    cursor = db.cursor()

    try:
        cursor.execute(sql_query)
        db.commit()
        db.close()
        return 1
    except Exception as e:
        db.rollback()
        db.close()
        print(e)
        return e


def insert_data_get_id(sql_query):
    db = create_con()
    cursor = db.cursor()

    try:
        cursor.execute(sql_query)
        id = cursor.lastrowid
        db.commit()
        db.close()
        return 1, id

    except Exception as e:
        db.rollback()
        db.close()
        print(e)
        return e


def insert_data_main_response(trip_info_sql, trip_df):
    db = create_con()
    cursor = db.cursor()

    try:
        cursor.execute(trip_info_sql)
        insert_data_pandas_df(trip_df, 'trip')
        db.commit()
        db.close()
        return 1
    except Exception as e:
        db.rollback()
        db.close()
        return e


def get_data(sql_query):
    db = create_con()
    cursor = db.cursor()
    cursor.execute(sql_query)
    results = cursor.fetchall()
    db.close()
    return results


def get_data_list(sql_query):
    db = create_con()
    cursor = db.cursor()
    cursor.execute(sql_query)
    results = list(cursor.fetchall())
    db.close()
    return results


def update_data(sql_query):
    db = create_con()
    cursor = db.cursor()

    try:
        cursor.execute(sql_query)
        db.commit()
        db.close()
        return 1
    except Exception as e:
        db.rollback()
        db.close()
        print(e)
        return e
