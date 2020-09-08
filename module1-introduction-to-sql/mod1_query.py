import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

cursorObj = conn.cursor()

# cursorObj.execute('SELECT name FROM sqlite_master where type= "table"')

# for x in cursorObj.fetchall():
    
#     print(x[0])

# How many total Characters are there?

query = 'SELECT COUNT(*) FROM charactercreator_character'
cursorObj.execute(query)
print(f'Total Characters:\t{cursorObj.fetchall()[0][0]} characters\n')

# How many of each specific subclass?

# Get subclass table names
cursorObj.execute('SELECT name FROM sqlite_master where type= "table"')

classes = [x[0] for x in cursorObj.fetchall() if (('charactercreator_' in x[0]) & 
                                                ('character' not in x[0].split('_')[1]))]
                                                
for rpg_class in classes:
    query = 'SELECT COUNT(*) FROM ' + rpg_class
    cursorObj.execute(query)
    print('class count: {}\t{}'.format(rpg_class.split('_')[1], cursorObj.fetchall()[0][0]))

# How many total Items?

query = 'SELECT COUNT(*) FROM armory_item'
cursorObj.execute(query)
itemCount = cursorObj.fetchall()[0][0]
print(f'\nTotal items:\t{itemCount}')

# How many of the Items are weapons? How many are not?

query = 'SELECT COUNT(*) FROM armory_weapon'
cursorObj.execute(query)
weaponCount = cursorObj.fetchall()[0][0]
print(f'\nTotal weapons:\t{weaponCount}\n')

print(f'Items that are not weapons: {itemCount - weaponCount}')

# How many Items does each character have? (Return first 20 rows)

itemquery = '''SELECT COUNT(*) FROM charactercreator_character_inventory 
            GROUP BY character_id 
            LIMIT 20'''
cursorObj.execute(itemquery)
results = [x[0] for x in cursorObj.fetchall()]
print(f'\nTotal items per character (top 20):\t{results}')

# print(f'columns: {cursorObj.description}')

# How many Weapons does each character have? (Return first 20 rows)

query = '''SELECT COUNT(*) 
            FROM charactercreator_character_inventory CCI
            INNER JOIN armory_weapon AW
            ON CCI.item_ID = AW.item_ptr_id
            GROUP BY character_id 
            LIMIT 20'''
cursorObj.execute(query)
results = [x[0] for x in cursorObj.fetchall()]
print(f'\nTotal weapons per character (top 20):\t{results}')

# On average, how many Items does each Character have?

query = ''.join(['SELECT AVG("COUNT(*)") FROM (',
            '''SELECT COUNT(*) FROM charactercreator_character_inventory 
            GROUP BY character_id ''',
            ')'])

# print(query)
cursorObj.execute(query)
print(f'\nAverage items per character:\t{cursorObj.fetchall()[0][0]}')

# On average, how many Weapons does each character have?

query = ''.join(['SELECT AVG("COUNT(*)") FROM (',
            '''SELECT COUNT(*) 
            FROM charactercreator_character_inventory CCI
            INNER JOIN armory_weapon AW
            ON CCI.item_ID = AW.item_ptr_id
            GROUP BY character_id ''',
            ')'])
cursorObj.execute(query)
print(f'\nAverage weapons per character:\t{cursorObj.fetchall()[0][0]}')

