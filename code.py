import mysql.connector
conn=mysql.connector.connect(user='root', password='', host='localhost', database='fun')
cursor=conn.cursor()

y_status='Not Returned'
n_status='Returned'
while(1):
    print('WELCOME TO MY LIBRARY\n\n')
    print('INSTRUCTIONS TO PROCEED\n\n1.Borrow Book\n2.Return\n3.Update Details\n4.Display\n5.Delete Record\n6.Exit\n\n')
    ch=int(input('Enter your choice:'))
#BORROW BOOK
    if ch==1:
        fname=input('Enter First Name:')
        lname=input('Enter Last Name:')
        phno=input('Enter Phone Number:')
        email=input('Enter Email:')
        book=input('Enter Book Name:')
        date=input('Enter Date(YYYY-MM-DD):')
    
        try:
            cursor.execute("""INSERT INTO logbook(firstname,lastname,phno,email,book,recieve_date,status) VALUES(%s,%s,%s,%s,%s,%s,%s)""", (fname, lname, phno, email,book,date,y_status))
            conn.commit ()
        except:
            conn.rollback()
        print ( '\nData entered successfully.\nHere is your book.\n\n' )
#RETURN BOOK
    elif ch==2:
        fname=input('Enter First Name:')
        lname=input('Enter Last Name:')
        book=input('Enter Book Name:')
        date1=input('Enter Date(YYYY-MM-DD):')
        try:
            cursor.execute("""update logbook set return_date=%s,status=%s where firstname=%s and book=%s;""",(date1,n_status,fname,book))
            print('\n\nBook Returned.\n\n')
        except:
            print('\n\nRecord not found\n\n')
#UPDATE RECORDS
    elif ch==3:
        fname=input('Enter First Name:')
        lname=input('Enter Last Name:')
        book=input('Enter Book Name:')
        print('---Choose what do you want to update---\n\n1.First Name\n2.Last Name\n3.Phone No\n4.Email\n5.Book\n6.Recieve date\n7.Return Date\n8.Exit\n')
        choice=int(input('Enter your choice:'))
        if choice==1:
            new=input('Enter New First Name:')
            try:
                cursor.execute("""update logbook set firstname=%s where firstname=%s and book=%s;""",(new,fname,book))
                print('\n\nRecord Updated.\n')
            except:
                print('\n\nRecord not found\n')
        elif choice==2:
            new=input('Enter New Last Name:')
            try:
                cursor.execute("""update logbook set laststname=%s where firstname=%s and book=%s;""",(new,fname,book))
                print('\n\nRecord Updated.\n\n')
            except:
                print('\n\nRecord not found\n\n')
        elif choice==3:
            new=input('Enter New Phone No:')
            try:
                cursor.execute("""update logbook set phno=%s where firstname=%s and book=%s;""",(new,fname,book))
                print('\n\nRecord Updated.\n\n')
            except:
                print('\n\nRecord not found\n\n')
        elif choice==4:
            new=input('Enter New Email:')
            try:
                cursor.execute("""update logbook set email=%s where firstname=%s and book=%s;""",(new,fname,book))
                print('\n\nRecord Updated.\n\n')
            except:
                print('\n\nRecord not found\n\n')
        elif choice==5:
            new=input('Enter New Book Name:')
            try:
                cursor.execute("""update logbook set book=%s where firstname=%s and book=%s;""",(new,fname,book))
                print('\n\nRecord Updated.\n\n')
            except:
                print('\n\nRecord not found\n\n')
        elif choice==6:
            new=input('Enter New Recieve Date(YYYY-MM-DD):')
            try:
                cursor.execute("""update logbook set recieve_date=%s where firstname=%s and book=%s;""",(new,fname,book))
                print('\n\nRecord Updated.\n\n')
            except:
                print('\n\nRecord not found\n\n')
        elif choice==7:
            new=input('Enter New Return Date(YYYY-MM-DD):')
            try:
                cursor.execute("""update logbook set return_date=%s where firstname=%s and book=%s;""",(new,fname,book))
                print('\n\nRecord Updated.\n\n')
            except:
                print('\n\nRecord not found\n\n')
        elif choice==8:
            exit()
#DISPLAY RECORD
    elif ch==4:
        boom=int(input('Select from below:\n1.See total Logbook record\n2.See Which books are Returned\n3.See which books are not returned\n4.Search by book\n5.Seach by name\n6.Exit\nEnter your choice:'))
        if boom==1:
            try:
                cursor.execute("select * from logbook;")
                result=cursor.fetchall()
                print('\n')
                for i in result:
                    for j in i:
                        print(j,end="\t")
                    print()
                print('\n')
            except:
                print('\nError:Unable to fetch data.\n\n')
        elif boom==2:
            try:
                cursor.execute("select * from logbook where status=%s;",(n_status))
                result=cursor.fetchall()
                print('\n')
                for i in result:
                    for j in i:
                        print(j,end="\t")
                    print()
                print('\n')
            except:
                print('\nError:Unable to fetch data.\n\n')
        elif boom==3:
            try:
                cursor.execute("select * from logbook where status=%s;",(y_status))
                result=cursor.fetchall()
                print('\n')
                for i in result:
                    for j in i:
                        print(j,end="\t")
                    print()
                print('\n')
            except:
                print('\nError:Unable to fetch data.\n\n')
        elif boom==4:
            try:
                find_book=input('Enter Book Name:')
                cursor.execute("select * from logbook where book=%s;",(find_book))
                result=cursor.fetchall()
                print('\n')
                for i in result:
                    for j in i:
                        print(j,end="\t")
                    print()
                print('\n')
            except:
                print('\nError:Unable to fetch data.\n\n')
        elif boom==5:
            try:
                cust_first=input("Enter Customer's first Name:")
                cust_last=input("Enter Customer's last Name:")
                cursor.execute("select * from logbook where firstname=%s and lastname=%s;",(cust_first,cust_last))
                result=cursor.fetchall()
                print('\n')
                for i in result:
                    for j in i:
                        print(j,end="\t")
                    print()
                print('\n')
            except:
                print('\nError:Unable to fetch data.\n\n')
        elif boom==6:
            exit()

#DELETE RECORD
    elif ch==5:
        fname=input('Enter first name:')
        lname=input('Enter last name:')
        book=input('Enter book name:')
        try:
            cursor.execute("""delete from logbook where firstname=%s and lastname=%s and book=%s;""",(fname,lname,book))
            print('\n\nRecord Deleted.\n\n')
        except:
            print('\n\nRecord not found\n\n')
        
            
                
                
        
#EXIT PROGRAM
    elif ch==6:
        print('\n\nThank You for coming .Visit Again!\n\n')
        exit()

    
    
    
    

