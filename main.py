import sqlite3
import re

con = sqlite3.connect("getraenke.db")

cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS getraenke
                (name text, preis text, bestand text)''')
con.commit()

option = input("Was möchtest du machen? \n1: Getränk kaufen. \n2: Admin Panel")

if option == "1":
    print("Getränkeautomat")
    cur.execute("SELECT * FROM getraenke")
    dbOutput = cur.fetchall()
    dbOutputString = str(dbOutput)
    dbOutputStringLineBreak = re.sub(r'(\))', r'\1\n', dbOutputString)
    print(re.sub('[^a-zA-Z0-9 \n\.]', '', dbOutputStringLineBreak))
    #print(re.sub(r'[^\w]', ' ',dbOutputStringLineBreak))
    inputAuswahl = input("Welches Getränk willst du? \n Name:")
    sql = '''SELECT * FROM getraenke WHERE name=\"''' + inputAuswahl + "\";"
    for row in cur.execute(sql):
        print(row)
    print("Dein Getränk wird ausgegeben")


elif option == "2":
    print("Admin panel")
    getraenkeName = input("Wie heißt das Getränk?")
    getraenkePreis = input("Wie viel kostet es?")
    getraenkeAnzahl = input("Wie viele Getränke werden nachgefüllt?")
    cur.execute("INSERT INTO getraenke (name, preis, bestand)VALUES (?, ?, ?)",
                (getraenkeName, getraenkePreis, getraenkeAnzahl))
    con.commit()

else:
    print("Ungültige eingabe")
