import sqlite3

conn = sqlite3.connect('ecomdb.db')
print("Opened database successfully")

conn.execute("INSERT INTO CATEGORIES (CategoryID,CategoryName,Description) \
      VALUES (1, 'Beverages','Soft drinks, coffees, teas, beers, and ales')");
"""
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
"""
conn.commit()
print ("Records created successfully")
conn.close()# -*- coding: utf-8 -*-
