import re
import sqlite3
import hashlib
import pandas as pd

m = hashlib.sha256()
con = sqlite3.connect("getraenke.db")

cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS getraenke
                (name text, preis text, bestand text)''')
con.commit()

option = input("Was möchtest du machen? \n1: Getränk kaufen. \n2: Admin Panel. \n3: Admin passwort erstellen")

if option == "1":
    print("Getränkeautomat")
    cur.execute("SELECT * FROM getraenke")
    dbOutput = cur.fetchall()
    dbOutputString = str(dbOutput)
    dbOutputStringLineBreak = re.sub(r'(\))', r'\1\n', dbOutputString)
    print(pd.read_sql_query("SELECT * FROM getraenke", con))
    inputAuswahl = input("Welches Getränk willst du? \n Name:")
    sql = '''SELECT * FROM getraenke WHERE name=\"''' + inputAuswahl + "\";"
    for row in cur.execute(sql):
        print(row)
    print("Dein Getränk wird ausgegeben")


elif option == "2":
    with open('password.txt', "r") as f:
        lines = f.read()
    passwortEingabe = input("Bitte gebe dein Admin passwort ein:")
    passwortEingabeHashed = hashlib.sha224(str.encode(passwortEingabe)).hexdigest()
    print(lines)
    if passwortEingabeHashed == lines:
        print("Admin panel")
        getraenkeName = input("Wie heißt das Getränk?")
        getraenkePreis = input("Wie viel kostet es?")
        getraenkeAnzahl = input("Wie viele Getränke werden nachgefüllt?")
        cur.execute("INSERT INTO getraenke (name, preis, bestand)VALUES (?, ?, ?)",
                    (getraenkeName, getraenkePreis, getraenkeAnzahl))
        con.commit()
    else:
        print("Passwort ist falsch")

elif option == "3":
    passwortNotHashed = input("Gebe ein neues Passwort für das admin panel ein:")
    passwortHashed = hashlib.sha224(str.encode(passwortNotHashed)).hexdigest()
    print(passwortHashed)
    with open('password.txt', 'w') as f:
        f.write(passwortHashed)
else:
    print("Ungültige eingabe")
