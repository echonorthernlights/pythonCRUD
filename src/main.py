from connect_db import connect_to_db, set_user, get_users, get_user, put_user, delete_user

print("Welcome user choose : ")
print("press 1 to :List all users")
print("press 2 to :List one user")
print("press 3 to :Insert a user")
print("press 4 to :Update a user")
print("press 5 to :Delete a user")
print("press Q/q to quit")

while True:
    connection = None
    choice = input("Enter your choice: ")
    if choice.lower() == 'q':
        break

    try:
        connection = connect_to_db()

        if choice == '1':
            data = get_users(connection)
            print(data)
        elif choice == '2':
            user_id = input("Enter user's id : ")
            result = get_user(connection, user_id)
            print(result)
        elif choice == '3':
            lastname = input("Enter your lastname : ")
            firstname = input("Enter your firstname : ")
            age = int(input("Enter your age : "))
            user = {'firstname': firstname, 'lastname': lastname, 'age': age}
            result = set_user(connection, user)
            print(result)
        elif choice == '4':
            user_id = input("Enter user's id to update : ")
            lastname = input("Enter user's new lastname : ")
            firstname = input("Enter user's new firstname : ")
            age = int(input("Enter user's new age : "))
            user = {'firstname': firstname, 'lastname': lastname, 'age': age}
            result = put_user(connection, user, user_id)
            print(result)
        elif choice == '5':
            user_id = input("Enter user's id to DELETE : ")
            result = delete_user(connection, user_id)
            print(result)
        else:
            print("Invalid choice. Please enter a valid option.")

    except Exception as e:
        print("An error occurred:", e)
    finally:
        if connection:
            connection.close()
