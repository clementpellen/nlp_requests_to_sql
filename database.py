import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

def create_db():
    df = pd.read_csv('data.csv')
    # Create an engine that stores data in the local directory's
    temp_db = create_engine('sqlite:///:memory:', echo=True)
    # Create a table from the dataframe
    df.to_sql('data', con=temp_db)
    return temp_db

if __name__ == "__main__":
    create_db()
