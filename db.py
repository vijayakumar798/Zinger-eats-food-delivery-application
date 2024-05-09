

# def create_tables():
#     conn = sqlite3.connect('Products.db')
#     cursor = conn.cursor
#     cursor.execute('''

# CREATE TABLE IF NOT EXISTS Meals ( id TEXT PRIMARY KEY, name TEXT, price INTEGER)''')

# cursor.execute('''

# CREATE TABLE IF NOT EXISTS Drinks ( 
#                id TEXT PRIMARY KEY,
#                name TEXT, 
#                price INTEGER)''')
               
#     cursor.execute ('''

# CREATE TABLE IF NOT EXISTS Drinks ( 
#          id TEXT PRIMARY KEY, 
#          name TEXT, 
#         price INTEGER)''')

# conn.commit() I
# conn.close()

# def insert_products():
#     conn = sqlite3.connect('Products.db')
#     cursor = conn.cursor()

#     meals_data[

# Cheeseburger', 10,

# ('M2', Chicken, 15),

# ('M3', 'Pizza', 12)

# cursor.executemany('INSERT OR IGNORE INTO Meals (1d, name, price) VALUES (?, ?, ?)', meals_data)

# drinks_data = [

# ('D1', 'Apple Juice', 5),
# ('D2',Orange Juice, 4),
# ('D3' ,'Grape Juice', 7)

# ]

# cursor.executemany('INSERT OR IGNORE INTO DRINKS (1d, name, price) VALUES (?, ?, ?)', drinks_data)

# conn.commit()

# conn.close()

# def get_product_prices():

# conn = sqlite3.connect('Products.db')

# cursor = conn.cursor()

# cursor.execute('SELECT price FROM Meals')

# meal_prices = [row[0] for row in cursor.fetchall()]

# cursor.execute('SELECT price FROM Drinks')

# drink_prices = [row[0] for row in cursor.fetchall()]

# conn.close()

# return meal_prices, drink_prices

# create_tables()
# insert_products()


import sqlite3

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Meals (
            id TEXT PRIMARY KEY,
            name TEXT,
            price INTEGER
        )''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Drinks (
            id TEXT PRIMARY KEY,
            name TEXT,
            price INTEGER
        )''')

    conn.commit()

def insert_products(conn):
    cursor = conn.cursor()

    meals_data = [
        ('M1', 'Cheeseburger', 10),
        ('M2', 'Chicken', 15),
        ('M3', 'Pizza', 12)
    ]

    cursor.executemany('INSERT OR IGNORE INTO Meals (id, name, price) VALUES (?, ?, ?)', meals_data)

    drinks_data = [
        ('D1', 'Apple Juice', 5),
        ('D2', 'Orange Juice', 4),
        ('D3', 'Grape Juice', 7)
    ]

    cursor.executemany('INSERT OR IGNORE INTO Drinks (id, name, price) VALUES (?, ?, ?)', drinks_data)

    conn.commit()

def get_product_prices(conn):
    cursor = conn.cursor()

    cursor.execute('SELECT price FROM Meals')
    meal_prices = [row[0] for row in cursor.fetchall()]

    cursor.execute('SELECT price FROM Drinks')
    drink_prices = [row[0] for row in cursor.fetchall()]

    return meal_prices, drink_prices

conn = sqlite3.connect('Products.db')
create_tables(conn)
insert_products(conn)
conn.close()

