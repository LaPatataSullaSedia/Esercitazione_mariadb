import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="fatass",
  password="nigga"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")


