import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="Jesse",
    password="Jesse0802"
)

icao = input("Anna lentoaseman ICAO-koodi: ")

sql = """
    SELECT name, municipality
    FROM airport
    WHERE ident = %s
"""

kursori = yhteys.cursor()
kursori.execute(sql, (icao,))

tulos = kursori.fetchone()

if tulos:
    print(f"Lentokenttä: {tulos[0]}")
    print(f"Sijaintikunta: {tulos[1]}")
else:
    print("ICAO-koodia vastaavaa lentokenttää ei löytynyt.")

kursori.close()
yhteys.close()