import sqlite3

conn = sqlite3.connect('study_part1.sqlite3')

cursorObj = conn.cursor()

query = '''DROP TABLE IF EXISTS test;'''
cursorObj.execute(query)
query = '''CREATE TABLE test 
            (student varchar(255),
            studied varchar(255),
            grade int,
            age int,
            sex varchar(2))'''

cursorObj.execute(query)

query = '''INSERT INTO test VALUES
            ('Lion-O', 'True', 85, 24, 'Male'),
    ('Cheetara', 'True', 95, 22, 'Female'),
    ('Mumm-Ra', 'False', 65, 153, 'Male'),
    ('Snarf', 'False', 70, 15, 'Male'),
    ('Panthro', 'True', 80, 30, 'Male')'''

cursorObj.execute(query)

query = '''SELECT AVG(age) FROM test'''

cursorObj.execute(query)
print(f'What is the average age? {cursorObj.fetchall()[0][0]}')

query = '''SELECT student FROM test 
        WHERE sex = 'Female'
        '''

cursorObj.execute(query)
print(f'What are the name of the female students? {cursorObj.fetchall()}')

query = '''SELECT COUNT(*) FROM test 
        WHERE studied = "True"
        '''
cursorObj.execute(query)

print(f'How many students studied? {cursorObj.fetchall()}')

query = '''SELECT * FROM test
            ORDER BY student'''
            
cursorObj.execute(query)

print(f'''all students and all columns, 
        sorted by student names in alphabetical order.
        {cursorObj.fetchall()}''')