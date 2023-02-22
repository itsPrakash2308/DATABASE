import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
host="localhost",
user="abc",
password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

mycursor = mydb.cursor() 

# mycursor.execute("select * from test.test_table")

mycursor.execute("select c1,c5 from test.test_table")
for i in mycursor.fetchall():
    print(i)
mydb.close()