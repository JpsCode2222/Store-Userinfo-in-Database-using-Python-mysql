from dbhelper import DBHelper
def main():
    db=DBHelper()
    while True:
        print("*********Welcome*******")
        print()
        print("Enter 1 to insert new user")
        print("Enter 2 to display all user")
        print("Enter 3 to delete user")
        print("Enter 4 to update user")
        print("Enter 5 to exit program")
        print()
        print("************************")
        try:
            choice=int(input("Enter Input : "))
            if choice == 1:
                #insert
                uid=int(input("Enter new ID : "))
                newname=(input("Enter new name : "))
                newphone=(input("Enter new phone : "))
                db.insert_user(uid,newname,newphone)
                pass
            elif choice == 2:
                db.fetch_all()
                pass
            elif choice == 3:
                #delete
                uid=int(input("Enter ID : "))
                db.delet_User(uid)
                pass
            elif choice == 4:
                #update
                uid=int(input("Enter ID : "))
                newname=(input("Enter new name : "))
                newphone=(input("Enter new phone : "))
                db.Update_Name_Phone(uid,newname,newphone)
                pass
            elif choice == 5:
                break
            else:
                print("invalid input ! try agian")
        except Exception as e:
                print(e)
                print("invalid input ! try again ")
if __name__=="__main__":
    main()

            
