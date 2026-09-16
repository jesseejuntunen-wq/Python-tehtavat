import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="Jesse",
    password="Jesse0802"
)

maakoodi = input("Anna maakoodi")

sql = """
    SELECT type, COUNT(*)
    FROM airport
    WHERE iso_country = %s
    GROUP BY type
    ORDER BY type
"""

kursori = yhteys.cursor()
kursori.execute(sql, (maakoodi,))

tulokset = kursori.fetchall()

for tyyppi, lukumaara in tulokset:
    print(f"{tyyppi}: {lukumaara}")

kursori.close()
yhteys.close()