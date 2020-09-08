import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd
# from sqlalchemy import create_engine
from psycopg2.extras import execute_values


load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

# print(DB_NAME, DB_USER,DB_PASSWORD,DB_HOST)
# exit()
## Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, 
                        host=DB_HOST)

cur = conn.cursor()
## An example query
cur.execute('SELECT * from test_table;')

# print(cur.fetchone())

df = pd.read_csv('titanic.csv')
df['Age'] = df['Age'].astype(int)
df = df.rename({'Siblings/Spouses Aboard': 'Sibs',
                'Parents/Children Aboard': 'Pars'}, axis=1)


print(df.head())
create_query = '''
DROP TABLE IF EXISTS titanic;
CREATE TABLE titanic (
    Survived INT,
    Pclass INT,
    Name VARCHAR(100),
    Sex VARCHAR(7),
    Age INT,
    Sibs INT,
    Pars INT,
    Fare DECIMAL
);
'''
cur.execute(create_query)
print([str(col) for col in df.columns])
insert_query = ''.join(['''
INSERT INTO titanic (''', ', '.join(df.columns), ") VALUES %s"])
print(insert_query)

# Convert all rows to tuples of strings
rows = [tuple([str(value) for value in row]) for index, row in df.iterrows()]
for row in rows[:5]:
    print(row)

execute_values(cur, insert_query, rows)
# Actually save transactions
conn.commit()

cur.close()
conn.close()