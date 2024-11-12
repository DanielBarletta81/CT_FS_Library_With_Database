### Connect to  MySQL database

import mysql.connector

from mysql.connector import Error

def connect_to_db():

    db_name = "library_mgmt_db"
    user = "root"
    password = "Babinz2023!"
    host = "localhost"

    try:
      conn = mysql.connector.connect(buffered=True,
            database = db_name,
            user = user,
            password = password,
            host = host
            )
      
      print(f"Successful connection to Database: {db_name} ")
      return conn
    
    except Error as e:
      print(f'An exception occurred{e}')
      return None