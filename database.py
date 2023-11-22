import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, inspect, text

def create_db():
    df = pd.read_csv('germany-cars.csv')
    # Create an engine that stores data in the local directory's
    temp_db = create_engine('sqlite:///:memory:', echo=False)
    # Create a table from the dataframe
    df.to_sql('cars', con=temp_db)
    print("\nCREATION DE LA BASE DE DONNEE TERMINEE!\n\n\n\n")
    return temp_db

def get_column_names(temp_db):
    inspector = inspect(temp_db)
    columns = inspector.get_columns('cars')
    column_names = [column['name'] for column in columns]
    column_names = ', '.join(column_names)
    return column_names

def execute_sql_query(temp_db, sql_query):
    with temp_db.connect() as connection:
        result = connection.execute(text(sql_query)).fetchall()
        return result


if __name__ == "__main__":
    print(get_column_names())
