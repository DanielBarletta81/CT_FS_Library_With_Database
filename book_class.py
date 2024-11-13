import mysql.connector
from library_db_connect import connect_to_db
from mysql.connector import Error



# Create Classes here 

#Book Operations:
#        Book Operations:
#        1. Add a new book
#        2. Borrow a book
 #       3. Return a book
  #      4. Search for a book
    #    5. Display all books
# Menu Actions:

#Implement the following actions in response to menu selections using the classes
#  you've created:


#Adding a new book with all relevant details.
#Allowing users to borrow a book, marking it as "Borrowed."
#Allowing users to return a book, marking it as "Available."
#Searching for a book by its unique identifier (title) and displaying its details.
#Displaying a list of all books with their unique identifiers.
#

#
class Book:

    
  
    def __init__(self, title, author, genre, isbn):
        #make private attributes for genre and author
        
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__isbn = isbn
        
        self.__isAvailable = True

#Apply encapsulation principles by defining private attributes 
# and using getters and setters for necessary data access.

    # getters and setters
   
    def get_title(self):
        return self.__title

    def is_available(self):
        return self.__isAvailable

    def borrow_book(self):
        if self.__isAvailable:
            self.__isAvailable = False
            return True
        return False
    
    def return_book(self):
        self.__isAvailable = True

        

        ### change functions to incorporate mysql database ###

def add_a_book(id, title, author_id, isbn, publication_date, availability):
    try:
       conn = connect_to_db()

       if conn is not None:

        cursor = conn.cursor()

       new_book = (id, title, author_id, isbn, publication_date, availability)
       query = 'INSERT INTO books(id, title, author_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s, %s)'
       
       cursor.execute(query, new_book)
       conn.commit()
       print(f'New book added to library: {new_book}')

    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')

    except Exception as e:
         print(f"An exception occurred: \n {e}")
    finally :
        cursor.close()
        conn.close()

 
def borrow_book(id,  user_id, book_id, borrow_date):
    try:
         conn = connect_to_db()

         if conn is not None:

            cursor = conn.cursor()
            book_borrowed = ( id, user_id, book_id, borrow_date)
            query = 'INSERT INTO borrowed_books(id, user_id, book_id, borrow_date) VALUES (%s, %s, %s, %s)'
       
            cursor.execute(query, book_borrowed)
            conn.commit()
            print(f'Book: {book_id}, borrowed by user with id: {user_id}')

    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       
       
    except Exception as e:
         print(f"An exception occurred:\n {e}")

    finally :
        cursor.close()
        conn.close()
    
    


def return_book( id, user_id, book_id, borrow_date, return_date):
    try:
        conn = connect_to_db()

        if conn is not None:

            cursor = conn.cursor()
            book_returned = ( id, user_id, book_id, borrow_date, return_date)
            query = 'INSERT INTO borrowed_books(id, user_id, book_id, borrow_date, return_date) VALUES ( %s, %s, %s, %s, %s)'
       
            cursor.execute(query, book_returned)
            conn.commit()
            print(f'Book: {book_id}, returned by user with id: {user_id}')

    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       
       
    except Exception as e:
         print(f"An exception occurred:\n {e}") 

    finally :
        cursor.close()
        conn.close()

def book_search(isbn):

    try:
          conn = connect_to_db()

          if conn is not None:

            cursor = conn.cursor(dictionary=True)

          
            query = 'SELECT * FROM books WHERE isbn = %s'
          
       
            result= cursor.execute(query, (isbn,))
            print(cursor.fetchone()) 
            return result

    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       

    except Exception as e:
         print(f"An exception occurred: \n {e}")

    finally :
        cursor.close()
        conn.close()

def display_books():
             # SQL query to select all books
        # Execute, fetch, and print results
    try:
        conn = connect_to_db()

        if conn is not None:

            cursor = conn.cursor()
        
            query = 'SELECT * FROM books'
       
            cursor.execute(query)
            res = cursor.fetchall()

            for row in res:
                print(row)
           
    
    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       
       
    except Exception as e:
         print(f"An exception occurred: {e}")

    finally :
        cursor.close()
        conn.close()





def book_ops_menu():
        while True:
    
     
            print("***  Welcome to the Book Operations Menu! ***")
            print("\n Menu:")
            print("\n 1. Add a book")
            print("\n 2. Find a book")
            print("\n 3. Display all books")
            print("\n 4. Borrow a book")
            print("\n 5. Return a book")
            print("\n 6. Back to Main Menu")

            choice = int(input("Please choose an option (1-6): "))

            if choice == 6:
                return
            
            try:
            

                if choice == 1:
                    id = int(input("Enter new book id: "))
                    title = input("Enter book title: ")
                    author_id = int(input("Enter author id: "))
                    isbn = int(input("Enter book ISBN: "))
                    publication_date = input("Enter publication date: ")

               
                    add_a_book( id, title, author_id, isbn, publication_date, availability=1)
                    print(f'Book entitled: {title}, added to Library.')
               
       
                elif choice == 2:
                    isbn = input('Enter the ISBN of the book: ')
                    book_search(isbn)

               
                

                elif choice == 3:
                    display_books()
                


                elif choice == 4:
                    id = int(input("Enter id for transaction: "))
                    user_id = int(input("Enter user id for borrowed book: "))
                    book_id = int(input("Enter book id for borrowed book: "))
                    borrow_date = input("What date was book borrowed? ")
                    borrow_book( id, user_id, book_id, borrow_date)
                    
                
       
                elif choice == 5:
                    id = int(input("Enter id for transaction: "))
                    user_id = int(input("Enter user id for returned book: "))
                    book_id = int(input("Enter book id for returned book: "))
                    borrow_date = input("What date was book borrowed? ")
                    return_date = input("What date was book returned? ")
                    return_book(id, user_id, book_id, borrow_date, return_date)
                
       
                else:
                    print("Invalid selection, please try again.")

            except mysql.connector.Error as db_err:
                print(f' Database Error: \n {db_err}')
       
       
            except Exception as e:
                print(f"An exception occurred: {e}")

            
#Menu Actions:



#- Allowing users to borrow a book, marking it as "Borrowed."

#- Allowing users to return a book, marking it as "Available."

#- Searching for a book by its unique identifier (ISBN or title) and displaying its details.

#- Displaying a list of all books with their unique identifiers.



