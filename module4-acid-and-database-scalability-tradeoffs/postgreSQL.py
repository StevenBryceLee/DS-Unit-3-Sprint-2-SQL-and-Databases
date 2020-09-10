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

df = pd.read_csv('titanic.csv')
print(df.head())
# exit()
cur = conn.cursor()
# An example query
# cur.execute('SELECT * from titanic LIMIT 10;')

# print(cur.fetchall())

# How many passengers survived, and how many died?
query = '''
        SELECT COUNT(*) 
        FROM titanic
        WHERE Survived = 1
'''
cur.execute(query)
print(f'\nliving passengers: \t{cur.fetchall()[0][0]}')
print(f'Pandas answer:\t{len(df[df.Survived==1])}')

query = '''
        SELECT COUNT(*) 
        FROM titanic
        WHERE Survived = 0
'''
cur.execute(query)
print(f'Dead passengers: \t{cur.fetchall()[0][0]}')
print(f'Pandas answer:\t{len(df[df.Survived==0])}')

# How many passengers were in each class?
query = '''SELECT Pclass, COUNT(*) as count
            FROM titanic
            GROUP BY Pclass
            '''

cur.execute(query)
print(f'Passengers per class: \t{cur.fetchall()}')
print(f'Pandas answer:\t{[(col, len(df[df.Pclass == col])) for col in df.Pclass.unique()]}')

# How many passengers survived/died within each class?
query = '''SELECT Pclass, Survived, COUNT(*) as count
            FROM titanic
            GROUP BY Survived, Pclass
            '''

cur.execute(query)
print(f'Dead and living passengers per class: \t{cur.fetchall()}')
print(f'Pandas answer:\t{[(col, len(df[(df.Pclass == col) & (df.Survived == 0)]), len(df[(df.Pclass == col) & (df.Survived == 1)])) for col in df.Pclass.unique()]}')

# What was the average age of survivors vs nonsurvivors?
query = '''SELECT Survived, AVG(Age) as average
            FROM titanic
            GROUP BY Survived
            '''

cur.execute(query)
print(f'Age of passengers per Survived: \t{cur.fetchall()}')
print(f'Pandas answer:\t{[(col, df[df.Survived == 1].Age.mean(), df[df.Survived == 0].Age.mean()) for col in df.Survived.unique()]}')

# What was the average age of each passenger class?
query = '''SELECT Pclass, AVG(Age) as average
            FROM titanic
            GROUP BY Pclass
            '''

cur.execute(query)
print(f'Age of passengers per Pclass: \t{cur.fetchall()}')
print(f'Pandas answer:\t{[(col, df[df.Pclass == col].Age.mean()) for col in df.Pclass.unique()]}')

# What was the average fare by passenger class? By survival?
query = '''SELECT Pclass, AVG(Fare) as average
            FROM titanic
            GROUP BY Pclass
            '''

cur.execute(query)
print(f'Fare of passengers per Pclass: \t{cur.fetchall()}')
print(f'Pandas answer:\t{[(col, df[df.Pclass == col].Fare.mean()) for col in df.Pclass.unique()]}')

query = '''SELECT Survived, AVG(Fare) as average
            FROM titanic
            GROUP BY Survived
            '''

cur.execute(query)
print(f'Fare of passengers per Survival: \t{cur.fetchall()}')
print(f'Pandas answer:\t{[(col, df[df.Survived == col].Fare.mean()) for col in df.Survived.unique()]}')

# How many siblings/spouses aboard on average, by passenger class? By survival?
query = '''SELECT Pclass, AVG(sibs)
            FROM titanic
            GROUP BY Pclass
            '''

cur.execute(query)
print(f'Sibs/Spouses of passengers per Pclass: \t{cur.fetchall()}')
# print(f'Pandas answer:\t{[(col, df[df.Pclass == col]['Siblings/Spouses Aboard'].mean()) for col in df['Pclass'].unique()]}')

query = '''SELECT Survived, AVG(sibs)
            FROM titanic
            GROUP BY Survived
            '''

cur.execute(query)
print(f'Sibs/Spouses of passengers per Survived: \t{cur.fetchall()}')
# print(f'Pandas answer:\t{[(col, df[df['Survival'] == col]['Siblings/Spouses Aboard'].mean()) for col in df['Survival'].unique()]}')

# How many parents/children aboard on average, by passenger class? By survival?
query = '''SELECT Pclass, AVG(pars)
            FROM titanic
            GROUP BY Pclass
            '''

cur.execute(query)
print(f'Parents/Children of passengers per Pclass: \t{cur.fetchall()}')
# print(f'Pandas answer:\t{[(col, df[df['Pclass'] == col]['Parents/Children Aboard'].mean()) for col in df['Pclass'].unique()]}')

query = '''SELECT Survived, AVG(pars)
            FROM titanic
            GROUP BY Survived
            '''

cur.execute(query)
print(f'Parents/Children of passengers per Survived: \t{cur.fetchall()}')
# print(f'Pandas answer:\t{[(col, df[df['Survival'] == col]['Parents/Children Aboard'].mean()) for col in df['Survival'].unique()]}')

# Do any passengers have the same name?
query = '''SELECT Name, COUNT(*)
            FROM titanic
            GROUP BY Name
            HAVING COUNT(*) > 1
            '''

cur.execute(query)
print(f'Passengers with the same name: \t{cur.fetchall()}')
print(f'Pandas answer\t{df.Name.value_counts(ascending = False)}')

# Spouses aboard
# query = '''SELECT Name,
#             substring(Name from (LENGTH(Name) - RIGHT(POSITION(' ' in Name)))) as last, 
#             COUNT(*)
#             FROM titanic
#             WHERE sibs = 1
#             GROUP BY Name, last
#             '''

# cur.execute(query)
# print(f'Passengers with spouses: \t{cur.fetchall()}')