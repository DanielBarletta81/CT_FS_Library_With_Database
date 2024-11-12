
# 
#  create a robust system that allows users to browse, borrow, return, 
# and explore a collection of books and the use of modules.

###
""" def add_author(author_list):
    id = int(input("What's the new Author Id #? "))
    author_name = input("What's the new author's name? ")
    biography = input("Please provide a short biography: ")
    author_list[id] = Author(id, author_name, biography)

    print(f' New author added:  {author_name}')
    
     

def get_author_details(author_list):
        author_id = int(input("Please enter the author id: "))
        if author_id in author_list:
            print(f'Details for selected author: {author_list[author_id].get_author_name()} from their biography: {author_list[author_id].get_biography()}') 
            


def display_authors(author_list):
       
        print("Current authors:")
        for author in author_list:
            if author:
                print(f'Author ID: {author} \n Name: {author_list[author].get_author_name()}') """


#Apply encapsulation principles by defining private attributes and using getters and setters
#  for necessary data access.


#Inheritance and Polymorphism:

#Utilize inheritance to give your books a Genre. Your book class can inherit from the 
# Genre class to gain attributes like genre name, description, and category. 
# Or create book subclasses like FictionBook, NonFictionBook that inherit from the Book class. 


#Modules:

#Organize your code into modules to promote code organization and maintainability. 
# Create separate modules for classes, user interactions, and error handling.

""" 
Menu Actions:

- Adding a new book with all relevant details.
- Allowing users to borrow a book, marking it as "Borrowed."
- Allowing users to return a book, marking it as "Available."
- Searching for a book by its unique identifier (ISBN or title) and displaying its details.
- Displaying a list of all books with their unique identifiers.


- Adding a new user with user details.
- Viewing user details.
- Displaying a list of all users.

- Adding a new author with author details.
- Viewing author details.
- Displaying a list of all authors.

- Adding a new genre with genre details.
- Viewing genre details.
- Displaying a list of all genres.
 """


#User Interaction:

#Utilize the input() function within the appropriate menus to enable users to interact
#  with the CLI and select menu options.
#Implement input validation using regular expressions (regex) to ensure the correct 
# formatting of user input.


#Error Handling:

#Implement error handling using try, except, else, and finally 
# blocks to manage potential issues gracefully, such as incorrect user input or file operations.


#GitHub Repository:

#Create a GitHub repository for your project and commit code regularly.
#Maintain a clean and interactive README.md file in your GitHub repository, providing clear instructions on how to run the application and explanations of its features.
#Include a link to your GitHub repository in your project documentation.


#Project Tips
#Begin by designing a class hierarchy that represents the library's structure and entities.
#Test your code iteratively as you implement each feature to identify and address any potential bugs or issues.
#Collaborate with peers, seek assistance, and remember that learning is a collaborative effort.
