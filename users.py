# user interactions module
import mysql.connector

from mysql.connector import Error
from library_db_connect import connect_to_db

# Establish class for User

# Menu Actions needed:
#Adding a new user with user details. check
#Viewing user details.
#Displaying a list of all users. check

class User:
  
    def __init__(self, user_id, member_name, username, password):
        #make private attributes 
       
        self.__user_id = user_id
        self.__member_name = member_name 
        self.__username = username
        self.__password = password
       

    # getters and setters
    
   # Encapsulation:

#Apply encapsulation principles by defining private attributes and using 
# getters and setters for necessary data access.


    def get_user_id(self):
        return self.__user_id

 #   def set_library_id(self, new_library_id):
  #      self.__library_id = new_library_id


    def get_member(self):
        return self.__member_name

  #  def set_member(self, new_member_name):
  #      self.__member_name = new_member_name

    def get_username(self):
        return self.__username

  #  def set_username(self, new_username):
  #      self.__username = new_username

    def get_password(self):
        return self.__password

  #  def set_password(self, new_password):
   #     self.__password = new_password

        #user functions below  VVVV



    
def add_new_user(id, name, library_id ):
    try:

        conn = connect_to_db()

        if conn is not None:

            cursor = conn.cursor()


        new_user = (id, name, library_id)
        query = "INSERT INTO users(id, name, library_id) VALUES (%s, %s, %s)"
        cursor.execute(query, new_user)
        print(f'User has been added to database.')

    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')

    except Exception as e:
          print(f"Exception Occurred: {e}")
    
    finally :
        cursor.close()
        conn.close()

            

def view_user_details(id):
    try:

        conn = connect_to_db()

        if conn is not None:

            cursor = conn.cursor()


        id = (id,)
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, id)
        res = cursor.fetchone()
        print(f'User Details: {res}')

    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')

    except Exception as e:
          print(f"Exception Occurred: {e}")
    
    finally :
        cursor.close()
        conn.close()
    

def display_all_users():
    try:

        conn = connect_to_db()

        if conn is not None:

            cursor = conn.cursor()

        query = "SELECT * FROM users;"
        cursor.execute(query)
        res = cursor.fetchall()
        for row in res:
             print(row)

    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')

    except Exception as e:
          print(f"Exception Occurred: {e}")
          
    finally :
        cursor.close()
        conn.close()
    
def user_menu():
   
     
    while True:
               print("***  Welcome to the User Operations Menu! ***")
               print("\n Menu:")
               print("\n 1. Add a new User")
               print("\n 2. View User details")
               print("\n 3. Display all Users")
               print("\n 4. Back to Main Menu")

               choice = int(input("Please choose an option (1-4): "))
          
    
               if choice == 4:
                    return

              

               elif choice == 1:
                id = int(input("Enter User Id: "))
                name = input("Enter name: ")
                library_id = int(input("Enter new library id: "))
                add_new_user( id, name, library_id)

                   

               elif choice == 2:
                    id = int(input("Enter User Id: "))
                    view_user_details(id)

                    
       
               elif choice == 3:
                    display_all_users()
                    
               else:
                    print("Invalid selection, please try again.")

    
