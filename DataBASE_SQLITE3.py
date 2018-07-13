
# Question 1
import sqlite3
conn=sqlite3.connect("database1.db")
curs=conn.cursor()
cmd1="Create table Book(bookId int(5) primary key,titleId int(5),location char(20),genre char(20));"
cmd2="Create table Titles(titleId int(5),ISBN int(13),publisherId char(10),publicationYear int(4),foreign key(titleId) references Book(titleId));"
cmd3="Create table Publishers(publisherId char(10),name char(10),streetAddress char(10),suiteNo int(3),zipCodeId int(6),foreign key(publisherId) references Titles(publisherId));"
cmd4="Create table ZipCodes(zipCodeId int(6),city char(10),state char(10),zipCode int(6),foreign key(zipCode) references Publishers(zipCodeId));"
cmd5="Create table AuthorsTitles(authorTitleId char(5),authorId char(7),titleId int(5),foreign key(titleId) references Titles(titleId));"
cmd6="Create table Authors(authorId char(7) primary key,fname char(10),mname char(10),lname char(10),foreign key(authorId) references AuthorsTitles(authorId));"
curs.execute(cmd1)
curs.execute(cmd2)
curs.execute(cmd3)
curs.execute(cmd4)
curs.execute(cmd5)
curs.execute(cmd6)
print("All the tables are created")


# Question 2
import sqlite3
conn=sqlite3.connect("database1.db")
cur=conn.cursor()
#updating some values in the tables created in test database
print("Original values of the table Book")
cmd="select * from Book;"
cur.execute(cmd)
for i in cur.fetchall():
    print(i)
print("After updating the location for bookId 2611")
cmd='update Book set location = "JALANDHAR" where bookId = 2611;'
cur.execute(cmd)
print("after updating values of the table Book")
cmd="select * from Book;"
cur.execute(cmd)
for i in cur.fetchall():
    print(i)
print("Original values of the table Authors")
cmd="select * from Authors;"
cur.execute(cmd)
for i in cur.fetchall():
    print(i)
#print("after updating values the zip code of zipcodeId of 110052")
cmd='update Authors set fname = "Harley" where authorId="Diaries"'
cur.execute(cmd)
print("after updating values of the table Authors")
cmd="select * from Authors;"
cur.execute(cmd)
for i in cur.fetchall():
    print(i)

print("Values updated")


# Question 3
import sqlite3
conn=sqlite3.connect("database1.db")
cur=conn.cursor()
#inserting values into the tables
cmd1='insert into Book values(2608,3108,"Canberra","Desire");'
cur.execute(cmd1)
cmd1='insert into Book values(2604,3104,"Bhopal","Tragedy");'
cur.execute(cmd1)
cmd1='insert into Book values(2611,3111,"Bhangarh","Horror");'
cur.execute(cmd1)
cmd2='insert into Titles values(3102,123456789012,"PN23",1997);'
cur.execute(cmd2)
cmd2='insert into Titles values(3126,123466789012,"PN26",2005);'
cur.execute(cmd2)
cmd2='insert into Titles values(3196,143456789012,"PN31",2010);'
cur.execute(cmd2)
cmd3='insert into Publishers values("AMAN2597","Akshay Kumar","Bharti_PUB",66,123000);'
cur.execute(cmd3)
cmd3='insert into Publishers values("NIKS3198","Nikhil Raj","MC_Grawhills",65,124000);'
cur.execute(cmd3)
cmd4='insert into ZipCodes values(123000,"Delhi","Delhi",110052);'
cur.execute(cmd4)
cmd4='insert into ZipCodes values(456000,"Shabibabad","Delhi",110000);'
cur.execute(cmd4)
cmd4='insert into ZipCodes values(123000,"Defense colony","Delhi",770052);'
cur.execute(cmd4)
cmd5='insert into AuthorsTitles values("Vampire","Diaries",12345);'
cur.execute(cmd5)
cmd5='insert into AuthorsTitles values("VAMPIRE","Diaries",78900);'
cur.execute(cmd5)
cmd6='insert into Authors values("Diaries","Akshay","kumar","Shaw");'
cur.execute(cmd6)
conn.commit()
print("All values are inserted")