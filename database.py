import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, inspect

def create_db():
    df = pd.read_csv('data.csv')
    # Create an engine that stores data in the local directory's
    temp_db = create_engine('sqlite:///:memory:', echo=True)
    # Create a table from the dataframe
    df.to_sql('data', con=temp_db)
    return temp_db

def get_column_names():
    temp_db = create_db()
    inspector = inspect(temp_db)
    columns = inspector.get_columns('data')
    column_names = [column['name'] for column in columns]
    column_names = ', '.join(column_names)
    return column_names


if __name__ == "__main__":
    print(get_column_names())
