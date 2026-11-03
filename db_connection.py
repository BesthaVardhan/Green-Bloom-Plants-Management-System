import mysql.connector


def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Vardhan888",
            database="green_bloom_db"
        )

        return connection

    except mysql.connector.Error as error:
        print("Database connection failed:", error)
        return None
if __name__ == "__main__":
    connection = get_connection()

    if connection:
        print("Database connected successfully!")
        connection.close()