import mysql.connector

from mysql.connector import Error


db_name = "libraryDb"
user = "root"
password = "Babinz2023!"
host = "localhost"


def add_new_author(cursor, id,  name, biography):
      try:
          new_author = (id, name, biography)
          query = "INSERT INTO authors(id, name, biography) VALUES (%s, %s, %s)"
       
          cursor.execute(query, new_author)

      except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       

      except Exception as e:
         print(f"An exception occurred: \n {e}")
        

def view_author(cursor, id):
     try:
          id = (id,)
          query = "SELECT * FROM authors WHERE id= %s"
       
          cursor.execute(query, id)
          print(cursor.fetchone()) 

     except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       

     except Exception as e:
         print(f"An exception occurred: \n {e}")
          
           

def display_all_authors(cursor):
     try:
        query = "SELECT * FROM authors;"
        cursor.execute(query)
        res = cursor.fetchall()
        for row in res:
            print(row)
     except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       

     except Exception as e:
         print(f"An exception occurred: \n {e}")

def author_menu():
    conn = mysql.connector.connect(buffered=True,
            database = db_name,
            user = user,
            password = password,
            host = host
            )
    if conn is not None:
     
     
       print("***  Welcome to the Author Operations Menu! ***")
       print("\n Menu:")
       print("\n 1. Add a new author")
       print("\n 2. View author details")
       print("\n 3. Display all authors")
       print("\n 4. Back to Main Menu")

       choice = int(input("Please choose an option (1-4): "))

       if choice == 4:
            return
       try:
          cursor = conn.cursor()
     
          if choice == 1:
             id = int(input("Enter Author's Id: "))
             name = input("Enter Author's name: ")
             biography = input("Add some author highlights: ")
             add_new_author(cursor, id, name, biography)
             conn.commit()
       
          elif choice == 2:
             id = int(input("Enter Author's Id: "))
             view_author(cursor, id)
             conn.commit()

       
          elif choice == 3:
            display_all_authors(cursor)
       
          else:
              print("Invalid selection, please try again.")
       except:
        print('An exception occurred') 

