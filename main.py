import sqlite3
import pandas as pd

con = sqlite3.connect("getraenke.db")

cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS getraenke
                (name text, preis text, bestand text)''')
con.commit()


def display():
    with sqlite3.connect("getraenke.db") as db:
        c = db.cursor()
        c.execute("CREATE VIEW IF NOT EXISTS test_VIEW AS SELECT name, preis, bestand FROM data")
        db.commit()
        data_pd = pd.read_sql('SELECT * FROM test_VIEW', db)
        print(data_pd)


option = input("Was möchtest du machen? \n1: Getränk kaufen. \n2: Admin Panel")

if option == "1":
    print("Getränkeautomat")

if option == "2":
    print("Admin panel")


else:
    print("Ungültige eingabe")
