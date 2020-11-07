from login import *
import json
import sqlite3
import random
def new_or_old():
    neld = input('''Are you:
    a.new
    b.not new
    :''')
    if neld == 'a' or neld == 'new':
        while True:
            name  = input("enter your name: ")
            if not name.isalpha():
                print('you have inpute nothing try agin')
                continue
            else:
                try:  
                    global calss
                    age = int(input("enter age: "))
                    if age > 14:
                        print('sorry we do not serve people above 14 years old.Bye')
                    elif age < 7:
                        print('sorry we do not think you will understund the books in our librari.come back when you are above 7 BYE')
                    
                    calss = int(input("enter grade: "))

                except ValueError:
                    print("sorry i did'nt understand that")
                c.execute("INSERT INTO login VALUES(?,?,?)",(name,age,calss))
                conn.commit()
                print("You are added")
                break        
                print(a) 
    #            global d
    elif neld == 'not new' or neld == 'b':
        def login():
            for i in range(3):
                name = input("pls enter your name: ")
                if name == '' or name == ' ':
                    print('you have inputed nothing try agin')
                    login()
                def age():
                    age = input("pls enter age: ")
                    if age == '' or age == ' ':
                        print('you have inputed nothing try agin')
                    age()
                age()
                def classes():
                    calss  = input("pls enter grade: ")
                    if calss == '' or calss == ' ':
                        print('you have inputed nothing try again')
                        classes()
                classes()
                with sqlite3.connect('main.db') as db:
                    c = db.cursor()
                find_user = ('SELECT * FROM login WHERE name = ? AND age = ? AND calss = ?')
                c.execute(find_user,[(name),(age),(calss)])
                results = c.fetchall()
                if results:
                    for bla in results:
                        malli = str(bla)
                        print("Welcome ")
                    break
                else:
                    print("name and age not recognised")
                    again = input("Do u want to try again?(y/n): ")
                    if again.lower() == "n":
                        print("Good Bye")
                        time.sleep(1)
                        break
        login()
    elif neld == '' or neld == ' ':
        print('you have inputed nothing pls try again')
        new_or_old()
    elif neld != 'a' or neld != 'b' or neld != 'new' or neld != 'not new':
        print('you have inputed the wrong thing pls try again')
        new_or_old()
new_or_old()
#def books():
#    f = open('books.json',) 
#    y = json.loads(x)
#
#    print(y["Mathematics for primary"])
#books()

        