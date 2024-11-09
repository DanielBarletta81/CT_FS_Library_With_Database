import mysql.connector

from mysql.connector import Error


db_name = "libraryDb"
user = "root"
password = "Babinz2023!"
host = "localhost"
       

def add_new_genre( cursor, id, name, description, category):
      
    try:
       new_genre = ( id, name, description, category)
       query = "INSERT INTO genres(id, name, description, category) VALUES ( %s, %s, %s, %s)"
       
       cursor.execute(query, new_genre)


    except mysql.connector.Error as db_err:
               print(f' Database Error: \n {db_err}')
         
     
    except Exception as e:
            print(f'An exception occurred {e}')

def display_genres(cursor):
     try:
        query = "SELECT * FROM genres;"
        cursor.execute(query)
        res = cursor.fetchall()

        for row in res:
            print(row)

     except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       

     except Exception as e:
         print(f"An exception occurred: \n {e}")

    

def view_single_genre(cursor, id):
     try:
          id = (id,)
          query = "SELECT * FROM genres WHERE id= %s"
       
          cursor.execute(query, id)
          print(cursor.fetchone()) 

     except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       

     except Exception as e:
         print(f"An exception occurred: \n {e}") 


def genre_ops_menu():
# establish connection
     conn = mysql.connector.connect(buffered=True,
            database = db_name,
            user = user,
            password = password,
            host = host
            )
     
     if conn is not None:
          
               print("***  Welcome to the Genre Operations Menu! ***")
               print("\n Menu:")
               print("\n 1. Add a new genre")
               print("\n 2. View genre details")
               print("\n 3. Display all genres")
               print("\n 4. Back to Main Menu")

               choice = int(input("Please choose an option (1-4): "))
          
                
               if choice == 4:
                    return
     try:
               cursor = conn.cursor()

               if choice == 1:
                    id = int(input("Enter Genre Id: "))
                    name= input("Enter Genre Name: ")
                    description = input("Enter a brief description. ")
                    category = input("Enter category: ")
                    add_new_genre(cursor, id, name, description, category)

                    conn.commit()

               elif choice == 2:
                    id = int(input("Enter Genre Id: "))
                    view_single_genre(cursor, id)

                    conn.commit()
       
               elif choice == 3:
                    display_genres(cursor)
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

    
