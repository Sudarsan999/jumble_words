#commands

#CREATE DATABASE jumblewords;
##ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
#CREATE USER 'administrator'@'localhost' IDENTIFIED BY 'password';
#GRANT ALL PRIVILEGES ON *.* TO 'administrator'@'localhost';


## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
import mysql.connector


myDB=mysql.connector.connect(
    		user='administrator',
    		password='password',
    		host='localhost',
    		database='jumblewords'
	)
cursor = myDB.cursor()

score=0
points=""
uname=""
#query = "create table scores (score_id INT NOT NULL AUTO_INCREMENT, username VARCHAR(200), points INT , scoredate DATE, PRIMARY KEY (score_id))"


def connectdb():
	
	
	return myDB
	
def updatescore(uname,points):
	#query="drop table scores"
	#cursor.execute(query)
	#query = "create table scores (score_id INT NOT NULL AUTO_INCREMENT, username VARCHAR(200), points INT , scoredate DATE, PRIMARY KEY (score_id))"
	query="TRUNCATE TABLE scores"
	cursor.execute(query)
	query="INSERT INTO scores (username,points,scoredate) VALUES (%s,%s,sysdate())"
	cursor.execute(query,(uname,points))
	myDB.commit()
	
def show_score():
	global score
	cursor.execute("select points from scores limit 1")
	for i in cursor.fetchall()[0]:
		score=i





