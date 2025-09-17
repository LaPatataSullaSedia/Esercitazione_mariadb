import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="fatass",
  password="nigga"
)


mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE USER IF NOT EXISTS 'fatass'@'localhost' IDENTIFIED BY 'nigga';")
    mycursor.execute("GRANT ALL PRIVILEGES ON *.* TO 'fatass'@'localhost' WITH GRANT OPTION;")
    mycursor.execute("FLUSH PRIVILEGES;")
    print("Utente 'fatass' creato con successo e privilegi concessi.")
except mysql.connector.Error as err:
    print(f"Errore durante la creazione dell'utente: {err}")

# Chiudi la connessione
mycursor.close()
mydb.close()

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="fatass",  # Ora l'utente fatass può connettersi
        password="nigga"  # La password che hai impostato per l'utente 'fatass'
    )
    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES;")
    print(mycursor.fetchall())

    mycursor.close()
    mydb.close()
except mysql.connector.Error as err:
    print(f"Errore durante la connessione come 'fatass': {err}")