# user interactions module
import mysql.connector

from mysql.connector import Error


db_name = "libraryDb"
user = "root"
password = "Babinz2023!"
host = "localhost"
        
    
def add_new_user(cursor, id, name, library_id ):
    try:
        new_user = (id, name, library_id)
        query = "INSERT INTO users(id, name, library_id) VALUES (%s, %s, %s)"
        cursor.execute(query, new_user)
        print(f'User has been added to database.')

    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')

    except Exception as e:
          print(f"Exception Occurred: {e}")
             
        

def view_user_details(cursor, id):
    try:
        id = (id,)
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, id)
        res = cursor.fetchone()
        print(f'User Details: {res}')

    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')

    except Exception as e:
          print(f"Exception Occurred: {e}")
             
       

def display_all_users(cursor):
    try:
        query = "SELECT * FROM users;"
        cursor.execute(query)
        res = cursor.fetchall()
        for row in res:
             print(row)

    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')

    except Exception as e:
          print(f"Exception Occurred: {e}")
    
def user_menu():
    # establish connection
     conn = mysql.connector.connect(buffered=True,
            database = db_name,
            user = user,
            password = password,
            host = host
            )
     
     if conn is not None:
          
               print("***  Welcome to the User Operations Menu! ***")
               print("\n Menu:")
               print("\n 1. Add a new User")
               print("\n 2. View User details")
               print("\n 3. Display all Users")
               print("\n 4. Back to Main Menu")

               choice = int(input("Please choose an option (1-4): "))
          
                
               if choice == 4:
                    return
     try:
               cursor = conn.cursor()

               if choice == 1:
                    id = int(input("Enter User Id: "))
                    name = input("Enter name: ")
                    library_id = int(input("Enter new library id: "))
                    add_new_user(cursor, id, name, library_id)

                    conn.commit()

               elif choice == 2:
                    id = int(input("Enter User Id: "))
                    view_user_details(cursor, id)

                    conn.commit()
       
               elif choice == 3:
                    display_all_users(cursor)
                    conn.commit()
               else:
                    print("Invalid selection, please try again.")

     except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       
       
     except Exception as e:
         print(f"An exception occurred:\n {e}")
   
     
     finally:
            if conn and conn.is_connected():
                conn.close()
                print("MySQL connection closed.")
    
