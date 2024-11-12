# connect to mysql database
import mysql.connector

from mysql.connector import Error

from library_db_connect import connect_to_db








# Establish class for Authors

class Author:
  
    def __init__(self, id, name, biography):
        #make private attributes for author name and biography

        self.__id = id
        self.__name = name
        self.__biography = biography



# Menu Actions needed:
#Adding a new author with author details. 
#Viewing author details.
#Displaying a list of all authors. 


#Apply encapsulation principles by defining private attributes 
# and using getters and setters for necessary data access.

      # getters and setters
    def get_author_id(self):
        return self.__id

   
    def get_author_name(self):
        return self.__name

    
    def get_biography(self):
        return self.__biography


def add_new_author(id, name, biography):
      
    try:
       conn = connect_to_db()

       if conn is not None:

        cursor = conn.cursor()

        new_author = (id, name, biography)
        # Insert new author
        query = "INSERT INTO authors (id, name, biography) VALUES (%s, %s, %s)"
    
        cursor.execute(query, new_author)
        
        print(f"Author {new_author.name} added successfully.")
        return True

       """ cursor = conn.cursor()
           author = Author(id, name, biography)
           id = author.get_author_id()
           name = author.get_author_name()
           biography = author.get_biography()

          
           query = "INSERT INTO authors(id, name, biography) VALUES (%s, %s, %s)"
       
           cursor.execute(query, author)
 """
    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       

    except Exception as e:
        print(f"An exception occurred: \n {e}")
    
    finally :
        cursor.close()
        conn.close()




### Having issues with this one! getting db error, will come back to fix (11/12/24)
def view_author(id):
     try:
          conn = connect_to_db()

          if conn is not None:

            cursor = conn.cursor(dictionary=True)

          
          query = 'SELECT * FROM authors WHERE id = %s'
          
       
          result= cursor.execute(query, (id,))
          print(cursor.fetchone()) 
          return result

     except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       

     except Exception as e:
         print(f"An exception occurred: \n {e}")

     finally :
        cursor.close()
        conn.close()
        
 ## works
def display_all_authors():
     try:
        conn = connect_to_db()

        if conn is not None:

            cursor = conn.cursor()



        query = "SELECT * FROM authors;"
        cursor.execute(query)
        res = cursor.fetchall()
        for row in res:
            print(row)
     except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       

     except Exception as e:
         print(f"An exception occurred: \n {e}")


     finally :
        cursor.close()
        conn.close()



"""  Author Operations:
        1. Add a new author
        2. View author details
        3. Display all authors """

def authorMenu():
    
    
     
        
        while True:
    
            print("***  Welcome to the Library's Author Menu!  ***")
            print("\n Menu: ")
            print("\n 1. Add an author. ")
            print("\n 2. View author information. ")
            print("\n 3. Display all authors. ")
            print("\n 4. Return to Main Menu. ")

            choice = int(input("What would you like to do (1-4)? "))

            if choice == 4:
                return
        
            elif choice == 1:
                add_new_author(
                    id= int(input("Enter author id: ")), 
                    name = input("Enter author name: "),
                    biography = input("Provide a short bio: ")
                )
                
            elif choice == 2:
                id = int(input("enter id: ", ))
                view_author(id)
                
            elif choice == 3:
                display_all_authors()