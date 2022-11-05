import mysql.connector as connector
class DBHelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',
                                   port='3306',
                                   user='root',
                                   password='Jayad@2222',
                                   database='world')
        query='create table if not exists user(ID int primary key,Name varchar(100),Phone varchar(12))'
        cursor=self.con.cursor()
        cursor.execute(query)
        print('Table will be created in DB')

        

    #insert
    #insert data into table function
    def insert_user(self,ID,Name,Phone):

        #query of mysql
       query='insert into user(ID,Name,Phone) values({},"{}","{}")'.format(ID,Name,Phone)
       print(query)

       #cursor create
       cursor=self.con.cursor()
       cursor.execute(query)
       self.con.commit()
       print('user saved to DB')

       
    #Fetch Only User ID
    def fetch_only_ID(self):
        query='select ID from user'
        cur=self.con.cursor()
        cur.execute(query)
        print(cur)
        for i in cur:
            print("ID is : ",i[0])
            print()
            
       

    #fetch All
    #function select all data in table using cursor
    def fetch_all(self):
        query='select * from user'
        
        #create cursor of connection
        cursor=self.con.cursor()
        cursor.execute(query)
        
        #for loop for row = i (row is in the form of tupple)
        for i in cursor:
            print("ID is : ",i[0])
            print("Name is : ",i[1])
            print("Phone is : ",i[2])
            print()
            print()

    #Delet user by its ID
    def delet_User(self,ID):
        query='delete from user where ID = {}'.format(ID)
        cur=self.con.cursor()
        cur.execute(query)
        #permenent change in DB table (commit())
        self.con.commit()
        print(query)



    def Update_Name_Phone(self,ID,newName,newPhone):
        query='update user set Name="{}",Phone="{}" where ID={}'.format(newName,newPhone,ID)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('New name & New phone created')


    
