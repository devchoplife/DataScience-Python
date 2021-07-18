#Writin code using DB-API

from dbmodule import connect

#create connection object
connection = connect('databasename','username','password')

#create a cursor object
cursor = connection.cursor()#used to run queries and fetch reaults

#run queries
cursor.execute('select * from mytable')
results = cursor.fetchall()

#free resources
cursor.close()#always close conn to avoid unused data taking up resources
connection.close()
	