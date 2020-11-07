import sqlite3
conn = sqlite3.connect('main.db') 
c = conn.cursor()
    
c.execute("CREATE TABLE IF NOT EXISTS login(name VARCHAR, age INTEGER,calss INTEGER)")
