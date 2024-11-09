
import mysql.connector

from mysql.connector import Error


db_name = "libraryDb"
user = "root"
password = "Babinz2023!"
host = "localhost"

def add_a_book(cursor, id, title, author_id, genre_id, isbn, publication_date):
    try:
       new_book = (id, title, author_id, genre_id, isbn, publication_date)
       query = "INSERT INTO books(id, title, author_id, genre_id, isbn, publication_date) VALUES (%s, %s, %s, %s, %s, %s)"
       
       cursor.execute(query, new_book)

    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')

    except Exception as e:
         print(f"An exception occurred: \n {e}")


def borrow_book(cursor, id,  user_id, book_id, borrow_date):
    try:
        book_borrowed = ( id, user_id, book_id, borrow_date)
        query = "INSERT INTO borrowed_books(id, user_id, book_id, borrow_date) VALUES (%s, %s, %s, %s)"
       
        cursor.execute(query, book_borrowed)

    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       
       
    except Exception as e:
         print(f"An exception occurred:\n {e}")


def return_book(cursor, id,  user_id, book_id, return_date):
    try:
        book_returned = ( id, user_id, book_id, return_date)
        query = "INSERT INTO borrowed_books(id, user_id, book_id, return_date) VALUES ( %s, %s, %s, %s)"
       
        cursor.execute(query, book_returned)

    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       
       
    except Exception as e:
         print(f"An exception occurred:\n {e}") 



def book_search(cursor, isbn):

        try:
           isbn = (isbn,)
           query = "SELECT * FROM books WHERE isbn =%s"

             # execute query
           cursor.execute(query)
            # get results from query
           res = cursor.fetchone()
           print(res)
           
            

        except mysql.connector.Error as db_err:
            print(f' Database Error: \n {db_err}')
       
        except Exception as e:
            print(f"An exception occurred:\n {e}")


def display_books(cursor):
             # SQL query to select all books
        # Execute, fetch, and print results
    try:
        
        query = "SELECT * FROM books;"
       
        cursor.execute(query)
        res = cursor.fetchall()
        for row in res:
            print(row)
           
    
    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       
       
    except Exception as e:
         print(f"An exception occurred: {e}")





def book_ops_menu():
    # establish connection
    conn = mysql.connector.connect(buffered=True,
            database = db_name,
            user = user,
            password = password,
            host = host
            )
     
    if conn is not None:
    
     
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
            cursor = conn.cursor() 

            if choice == 1:
                id = int(input("Enter new book id: "))
                title = input("Enter book title: ")
                author_id = int(input("Enter author id: "))
                genre_id = int(input("Enter genre id: "))
                isbn = input("Enter book ISBN: ")
                publication_date = input("Enter publication date: ")
                add_a_book(cursor, id, title, author_id, genre_id, isbn, publication_date)

                conn.commit()
       
            elif choice == 2:
                isbn = input('Enter the ISBN of the book: ')
                book_search(cursor, isbn)

                conn.commit()
                

            elif choice == 3:
                display_books(cursor)
                conn.commit()


            elif choice == 4:
                id = int(input("Enter id for transaction: "))
                user_id = int(input("Enter user id for borrowed book: "))
                book_id = int(input("Enter book id for borrowed book: "))
                borrow_date = input("What date was book borrowed? ")
                borrow_book(cursor, id, user_id, book_id, borrow_date)
                conn.commit()
                
       
            elif choice == 5:
                id = int(input("Enter id for transaction: "))
                user_id = int(input("Enter user id for returned book: "))
                book_id = int(input("Enter book id for returned book: "))
                return_date = input("What date was book returned? ")
                return_book(cursor, id, user_id, book_id, return_date)
                conn.commit()
       
            else:
                 print("Invalid selection, please try again.")

    except mysql.connector.Error as db_err:
            print(f' Database Error: \n {db_err}')
       
       
    except Exception as e:
            print(f"An exception occurred: {e}")

    finally:
            if conn and conn.is_connected():
                conn.close()
                print("MySQL connection closed.")
#Menu Actions:



#- Allowing users to borrow a book, marking it as "Borrowed."

#- Allowing users to return a book, marking it as "Available."

#- Searching for a book by its unique identifier (ISBN or title) and displaying its details.

#- Displaying a list of all books with their unique identifiers.



