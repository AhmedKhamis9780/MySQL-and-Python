import mysql.connector

# Replace the following variables with your database credentials
hostname = 'localhost'
username = 'root'
password = 'whatever'
database = 'BucketList'

# Connect to the MySQL server
try:
    connection = mysql.connector.connect(
        host=hostname,
        user=username,
        password=password,
        database=database
    )
    print("Connected to MySQL server")

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # SQL query to create the table
    create_table_query = """
    CREATE TABLE tbl_user (
        user_id BIGINT AUTO_INCREMENT,
        user_name VARCHAR(45),
        user_username VARCHAR(45),
        user_password VARCHAR(45),
        PRIMARY KEY (user_id)
    )
    """

    # Execute the create table query
    cursor.execute(create_table_query)
    print("Table tbl_user created successfully")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection and cursor
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

