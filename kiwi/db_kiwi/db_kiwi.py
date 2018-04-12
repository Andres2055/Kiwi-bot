import sqlite3 as dbapi

kiwi = dbapi.connect("kiwi.dat")
cursor = kiwi.cursor()

canal_hola = ""

cursor.execute("""create table info_server (canal_hola text)""")
				
cursor.execute("""insert into info_server
				values (?)""", (canal_hola))
				
kiwi.commit()

cursor.execute("""select * from info_server""")

for tupla in cursor:
	print(tupla[0:3])
	
cursor.close()
kiwi.close()