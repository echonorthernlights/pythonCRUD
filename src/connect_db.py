import psycopg2
from psycopg2 import Error


def connect_to_db():
    connection = None

    try:
        connection = psycopg2.connect(
            user="postgres",
            password="root1234",
            host="localhost",
            port="5432",
            database="pydb"
        )
        print("You are connected...")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)
    # finally:
    #     # Closing the database connection.
    #     if connection:
    #         connection.close()
    #         print("PostgreSQL connection is closed")
    return connection


def get_users(connection):
    records = None
    try:

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # Executing a SQL query
        cursor.execute("SELECT * FROM users;")

        # Fetching the result
        records = cursor.fetchall()
    except (Exception, Error) as error:
        print("Error :", error)
    finally:
        # Closing the database connection.
        if connection:
            connection.close()
            print("PostgreSQL connection is closed")
    return records


def get_user(connection, user_id):
    record = None
    try:

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # Executing a SQL query
        cursor.execute("SELECT * FROM users WHERE user_id=%s;", (user_id))

        # Fetching the result
        record = cursor.fetchall()
    except (Exception, Error) as error:
        print("Error :", error)
    finally:
        # Closing the database connection.
        if connection:
            connection.close()
            print("PostgreSQL connection is closed")
    return record


def put_user(connection, user, user_id):
    cursor = connection.cursor()
    try:
        cursor.execute('UPDATE users SET firstname=%s, lastname=%s, age=%s WHERE user_id=%s',
                       (user["firstname"], user["lastname"], user["age"], user_id))
        connection.commit()  # Commit the transaction after insertion
    except (Exception, Error) as error:
        print("Error :", error)
    finally:
        # Closing the database connection.
        if connection:
            connection.close()
            print("PostgreSQL connection is closed")
    return "User updated successfully !!"


def set_user(connection, user):
    cursor = connection.cursor()
    try:
        cursor.execute('INSERT INTO users(firstname, lastname, age) VALUES(%s, %s, %s)', (user["firstname"],
                                                                                          user["lastname"],
                                                                                          user["age"]))
        connection.commit()  # Commit the transaction after insertion
    except (Exception, Error) as error:
        print("Error :", error)
    finally:
        # Closing the database connection.
        if connection:
            connection.close()
            print("PostgreSQL connection is closed")
    return "User added successfully !!"


def delete_user(connection, user_id):
    try:

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # Executing a SQL query
        cursor.execute("DELETE FROM users WHERE user_id=%s;", user_id)
        connection.commit()
    except (Exception, Error) as error:
        print("Error :", error)
    finally:
        # Closing the database connection.
        if connection:
            connection.close()
            print("PostgreSQL connection is closed")
    return "User deleted successfully !!"
