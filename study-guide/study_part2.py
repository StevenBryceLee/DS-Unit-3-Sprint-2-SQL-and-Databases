import sqlite3

conn = sqlite3.connect('Chinook_Sqlite.sqlite')

cursorObj = conn.cursor()

query = '''SELECT CustomerId, AVG(Total) FROM Invoice 
        GROUP BY CustomerId
        LIMIT 5
        '''

cursorObj.execute(query)
print(f'Average Total? {cursorObj.fetchall()}')

query = '''SELECT * FROM Customer 
        LIMIT 5
        '''

cursorObj.execute(query)
print(f'\nCustomer 5\n? {cursorObj.fetchall()}')

query = '''SELECT * FROM Employee 
        WHERE ReportsTo IS NULL
        '''

cursorObj.execute(query)
print(f'\nNo Manager\n {cursorObj.fetchall()}')

query = '''SELECT DISTINCT COUNT(Name) from Artist
        '''

cursorObj.execute(query)
print(f'\nNumber of Composers\n {cursorObj.fetchall()}')

query = '''SELECT COUNT(*) from Track
        '''

cursorObj.execute(query)
print(f'\nNumber of rows in Track\n {cursorObj.fetchall()}')
