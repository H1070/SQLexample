#import SQLlite
import sqlite3
#create file
db=sqlite3.connect('Python_Programming')
#get cursor object
cursor=db.cursor()



#create table
cursor.execute('''
CREATE TABLE Python_Programming (ID INTEGER PRIMARY KEY,Name TEXT, Grade INTEGER)
''')

db.commit()


cursor=db.cursor()
id1=55
name1='Carl Davis'
grade1=61

id2=66
name2='Dennis Fredrickson'
grade2=88

id3=77
name3='Jane Richards'
grade3=78

id4=12
name4='Peyton Sawyer'
grade4=45

id5=2
name5='Lucas Brooke'
grade5=99

# Insert student 1
cursor.execute('''INSERT INTO Python_Programming(id, name, grade)
                  VALUES(?,?,?)''', (id1,name1, grade1))
print('First user inserted')

# Insert student 2
cursor.execute('''INSERT INTO Python_Programming(id, name, grade)
                  VALUES(?,?,?)''', (id2, name2, grade2))
print('Second user inserted')

# Insert student 3
cursor.execute('''INSERT INTO Python_Programming(id,name, grade)
                  VALUES(?,?,?)''', (id3, name3, grade3))

print('Third user inserted')

# Insert student 4
cursor.execute('''INSERT INTO Python_Programming(id, name, grade)
                  VALUES(?,?,?)''', (id4, name4, grade4))
print('Fourth user inserted')

# Insert student 5
cursor.execute('''INSERT INTO Python_Programming(id, name, grade)
                  VALUES(?,?,?)''', (id5, name5, grade5))
print('Fifth user inserted')

db.commit()

cursor.execute('''SELECT * from Python_Programming WHERE grade >60 AND grade < 80''')

db.commit()
Python_Programming=cursor.fetchall()
print (Python_Programming)

#chnage Carl Davis grade to 65

cursor.execute('''UPDATE Python_Programming SET grade = 65 WHERE id= 55 ''')

db.commit()

#delete 
cursor.execute('''DELETE FROM Python_Programming WHERE id=66''')

db.commit()

#change grades for students with ID less than 55

cursor.execute('''UPDATE Python_Programming SET grade=75 WHERE id<55''')

db.commit()





