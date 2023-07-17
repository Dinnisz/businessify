
import mysql.connector

mydb = mysql.connector.connect(
  host="businessify-instance-1.chrfb0kulzyt.eu-west-3.rds.amazonaws.com",
  user="admin",
  password="Businessify=1177"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT pswd FROM businessify.sec_users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

print('ola')



