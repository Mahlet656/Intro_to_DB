import mysql.connector
from mysql.connector import Error

def create_database():
    """ Connect to MySQL server and create the alx_book_store database """
    conn = None
    try:
        # NOTE: These credentials will be used in the sandbox.
        # Replace them if you are running this on your local machine.
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        if conn and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    create_database()
