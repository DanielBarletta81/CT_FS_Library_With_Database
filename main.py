## main entry point

import mysql.connector

from mysql.connector import Error
from library_db_connect import connect_to_db


db_name = "Library_MGMT_DB"
user = "root"
password = "Babinz2023!"
host = "localhost"


# 1. Create an improved, user-friendly command-line interface (CLI) for the Library Management
#  System with separate menus for each class of the system.

from user_class import user_menu
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
    conn = connect_to_db()
    
    if conn is not None:
     
     print("***  Welcome to the Library Management System! ***")
     print("\n Menu:")
     print("\n 1. Book Operations Menu.")
     print("\n 2. Author Operations Menu.")
     print("\n 3. User Operations Menu. ")
     print("\n 4. Quit. ")
     print("---********************---")

     choice = int(input("Please choose an option (1-5): "))

     try:

      if choice == 5:
          return

      elif choice == 1:
        book_ops_menu()
      elif choice == 2:
        authorMenu()
      elif choice == 3:
        user_menu()
        
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