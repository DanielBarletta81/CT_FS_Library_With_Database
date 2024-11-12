## main entry point

import mysql.connector

from mysql.connector import Error


db_name = "Library_MGMT_DB"
user = "root"
password = "Babinz2023!"
host = "localhost"


# 1. Create an improved, user-friendly command-line interface (CLI) for the Library Management
#  System with separate menus for each class of the system.
#from book_class import bookMenu
#from user_class import userMenu
from author_class import authorMenu
from book_class import book_ops_menu

"""     Welcome to the Library Management System!

    Main Menu:
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Quit """

## main menu

# main function

def main():
  while True:
        # establish connection
    conn = mysql.connector.connect(buffered=True,
            database = db_name,
            user = user,
            password = password,
            host = host
            )
    
    if conn is not None:
     
     print("***  Welcome to the Library Management System! ***")
     print("\n Menu:")
     print("\n 1. Book Operations Menu.")
     print("\n 2. Author Operations Menu.")
     print("\n 3. Genre Operations Menu. ")
     print("\n 4. User Operations Menu. ")
     print("\n 5. Quit. ")

     choice = int(input("Please choose an option (1-5): "))

     try:

      if choice == 5:
          return

      elif choice == 1:
        book_ops_menu()
      elif choice == 2:
        authorMenu()
        
      elif choice == 3:
        #userMenu()
        pass
        
     
      else:
        print("Error, invalid input. ")


     
         
     
     except Exception as e:
            print(f'An exception occurred {e}')
    

if __name__ == "__main__":
     main()
#Implement the following actions in response to menu selections 
# using the classes you've created:
#- Adding a new book with all relevant details.
# - Allowing users to borrow a book, marking it as 