#INSERTing Books into BOOKS TABLE
import mysql.connector
a=mysql.connector.connect(host='localhost',user='root',password='',database='fun')
b=a.cursor()

b.execute("insert into booklist values('Don Quixote','Miguel de Cervantes',5)")
b.execute("insert into booklist values('Pilgrim Progress','John Bunyan',3)")
b.execute("insert into booklist values('Robinson Crusoe','Daniel Defoe',15)")
b.execute("insert into booklist values('Gulliver Travels','Jonathan Swift',5)")
b.execute("insert into booklist values('Clarissa','Samuel Richardson',7)")
b.execute("insert into booklist values('Tristram Shandy','Laurence Sterne',5)")
b.execute("insert into booklist values('Tom Jones','Henry Fielding',5)")
b.execute("insert into booklist values('Dangerous','Pierre Choderlos',5)")
b.execute("insert into booklist values('Pierre Choderlos','Mary Shelley',5)")
b.execute("insert into booklist values(' Nightmare Abbey','Thomas Love',5)")
b.execute("insert into booklist values('Black Sheep','Georgette Heyer',5)")
b.execute("insert into booklist values(' The Charterhouse ','Stendhal',5)")
b.execute("insert into booklist values('Sybil',' Flora Rheta',5)")
b.execute("insert into booklist values('David Copperfield','Charles Dickens',5)")
b.execute("insert into booklist values('Jane Eyre','Charlotte Bronte',5)")
b.execute("insert into booklist values(' Vanity Fair','John Welfer',5)")
b.execute("insert into booklist values('One Rupee','Dustin Lo',5)")
b.execute("insert into booklist values('Ignited Minds','Abdul Kalam',5)")
b.execute("insert into booklist values('Sacred Woods','John Karter',9)")

a.close()
