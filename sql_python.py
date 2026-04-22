import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
    user="raju1",
    password="raju")
print(mydb,"connected")