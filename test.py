import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="Admins",
	password="Admin*256",
	database="paldex"
)

mycursor = mydb.cursor()

def addPals(val):
	sql = "INSERT INTO pals (id, name) VALUES (%d, %s)"
	mycursor.executemany(sql, val)
	mydb.commit()

pal = [
	(82, "Azurobe"),
	(100, "Anubis")
]

addPals(pal)

print(mycursor.rowcount, "was inserted.")