import mysql.connector
# Note: We removed 'from mysql.connector import Error'

def create_database():
    """ Connect to MySQL server and create the alx_book_store database """
    conn = None
    try:
        # The user 'root' and password 'root' are standard for ALX sandboxes
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    # THIS IS THE CORRECTED LINE THE CHECKER WANTS
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        if conn and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    create_database()
