import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="Jesse",
    password="Jesse0802"
)

icao1 = input("Anna ensimmäisen lentoaseman ICAO-koodi: ")
icao2 = input("Anna toisen lentoaseman ICAO-koodi: ")

sql = """
    SELECT latitude_deg, longitude_deg
    FROM airport
    WHERE ident = %s
"""

kursori = yhteys.cursor()

kursori.execute(sql, (icao1,))
lentokentta1 = kursori.fetchone()

kursori.execute(sql, (icao2,))
lentokentta2 = kursori.fetchone()

if lentokentta1 is None:
    print(f"Lentokenttää {icao1} ei löytynyt.")
elif lentokentta2 is None:
    print(f"Lentokenttää {icao2} ei löytynyt.")
else:
    koordinaatit1 = (lentokentta1[0], lentokentta1[1])
    koordinaatit2 = (lentokentta2[0], lentokentta2[1])

    etaisyys = geodesic(koordinaatit1, koordinaatit2).kilometers

    print(f"Lentokenttien välinen etäisyys on {etaisyys:.1f} kilometriä.")

kursori.close()
yhteys.close()