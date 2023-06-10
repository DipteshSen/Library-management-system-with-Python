#CREATING THE AVAILABLE BOOKS TABLE
import mysql.connector
a=mysql.connector.connect(host='localhost',user='root',password='',database='fun')
b=a.cursor()
#b.execute('create table booklist(bookname varchar(100),Writer varchar(200),Units int)')
b.execute("create table logbook(firstname varchar(100),lastname varchar(100),phno varchar(100),email varchar(100),book varchar(100),recieve_date date,return_date date,status varchar(100));")
a.close()


