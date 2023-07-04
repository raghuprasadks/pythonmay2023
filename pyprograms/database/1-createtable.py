# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('ecomdb.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE CATEGORIES 
         (CategoryID INT PRIMARY KEY,
         CategoryName   TEXT    NOT NULL,
         Description    TEXT     NOT NULL
         )''')
print("Table created successfully")
conn.close()