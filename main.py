# main

#import mysql.connector

#from mysql.connector import Error

import books, genres, authors, users


db_name = "libraryDb"
user = "root"
password = "Babinz2023!"
host = "localhost"



def main():
  while True:
     """   # establish connection
    conn = mysql.connector.connect(buffered=True,
            database = db_name,
            user = user,
            password = password,
            host = host
            )
    if conn is not None: """
     
     print("***  Welcome to the Library Management System! ***")
     print("\n Menu:")
     print("\n 1. Book Operations Menu.")
     print("\n 2. Author Operations Menu.")
     print("\n 3. Genre Operations Menu. ")
     print("\n 4. User Operations Menu. ")
     print("\n 5. Quit. ")

     choice = int(input("Please choose an option (1-5): "))

     if choice == 5:
          return

     try:

            if choice == 1:
               books.book_ops_menu()
            
              
            elif choice == 2:

               authors.author_menu()

                   
            elif choice == 3:
                genres.genre_ops_menu()
                

            elif choice == 4:
               users.user_menu()
                
            
            else:
                print("Input Error. Please select a valid choice.")


     
         
     
     except Exception as e:
            print(f'An exception occurred {e}')
    

if __name__ == "__main__":
     main()
#Implement the following actions in response to menu selections 
# using the classes you've created:
#- Adding a new book with all relevant details.
# - Allowing users to borrow a book, marking it as 