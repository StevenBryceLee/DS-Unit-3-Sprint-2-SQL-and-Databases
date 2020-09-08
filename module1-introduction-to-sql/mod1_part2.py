import pandas as pd
import sqlite3


df = pd.read_csv('buddymove_holidayiq.csv')
# print(df.head())


conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

cursorObj = conn.cursor()

type_dict = {'User Id': str, 'Sports': int, 
            'Religious': int, 'Nature': int,  
            'Theatre': int,  'Shopping': int,  
            'Picnic': int, }
df.to_sql('review', con = conn, if_exists = 'replace', index = False, )

# Count how many rows you have - it should be 249!
query = '''SELECT COUNT(*) 
            FROM review'''

cursorObj.execute(query)
print(f'Total rows:\t{cursorObj.fetchall()[0][0]}\n')

# How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?
query = '''SELECT COUNT(*)
            FROM review
            WHERE Nature >= 100 AND Shopping >= 100'''
cursorObj.execute(query)
print(f'Total users who reviewed > 100 in nature and shopping:\t{cursorObj.fetchall()[0][0]}\n')

# What are the average number of reviews for each category?
query = '''SELECT *
            FROM review'''
cursorObj.execute(query)
# Get column names

names = [description[0] for description in cursorObj.description if 'User Id' not in description]
# print(names)
for name in names:
    query = f'''SELECT AVG({name})
                FROM review'''
    # print(query)
    cursorObj.execute(query)
    print(f'Average reviews for {name}:\t{cursorObj.fetchall()[0][0]}\n')

print('results in Pandas')
result = len(df[((df['Nature'] >= 100) & (df['Shopping'] >= 100))])
print(f'Total users who reviewed > 100 in nature and shopping:\t{result}\n')

for col in df.drop('User Id',axis = 1).columns:
    print(f'Average reviews for {col}:\t{df[col].mean(axis=0)}\n')