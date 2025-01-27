import mysql.connector
from cryptography.fernet import Fernet

# Encryption Key Generation (Run once to create a key file)
# with open("key.key", "wb") as key_file:
#     key_file.write(Fernet.generate_key())

# Load the encryption key
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="username", #Enter your mysql Username.
        password="password", #Enter your mysql Password.
        database="PasswordManager"
    )

def reset_ids():
    connection = create_connection()
    cursor = connection.cursor()
    
    query = "SET @new_id = 0;"
    cursor.execute(query)
    query = "UPDATE Passwords SET id = (@new_id := @new_id + 1) ORDER BY id;"
    cursor.execute(query)
    query = "ALTER TABLE Passwords AUTO_INCREMENT = 1;"
    cursor.execute(query)
    
    connection.commit()
    cursor.close()
    connection.close()
    print("IDs have been reset successfully!")

def add_password():
    platform = input("Enter platform name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    key = load_key()
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(password.encode())

    connection = create_connection()
    cursor = connection.cursor()

    query = "INSERT INTO Passwords (platform, username, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (platform, username, encrypted_password))

    connection.commit()
    cursor.close()
    connection.close()
    print("Password saved successfully!")

def view_passwords():
    key = load_key()
    cipher = Fernet(key)

    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT id, platform, username, password FROM Passwords"
    cursor.execute(query)

    results = cursor.fetchall()
    print("\nSaved Passwords:")
    print("ID | Platform | Username | Password")
    print("-----------------------------------")
    for entry_id, platform, username, encrypted_password in results:
        decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()
        print(f"{entry_id} | {platform} | {username} | {decrypted_password}")

    cursor.close()
    connection.close()

def update_username():
    entry_id = int(input("Enter the ID of the entry to update the username: "))
    new_username = input("Enter the new username: ")

    connection = create_connection()
    cursor = connection.cursor()

    query = "UPDATE Passwords SET username = %s WHERE id = %s"
    cursor.execute(query, (new_username, entry_id))

    connection.commit()
    cursor.close()
    connection.close()
    print("Username updated successfully!")

def update_password():
    entry_id = int(input("Enter the ID of the entry to update the password: "))
    new_password = input("Enter the new password: ")
    
    key = load_key()
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(new_password.encode())

    connection = create_connection()
    cursor = connection.cursor()

    query = "UPDATE Passwords SET password = %s WHERE id = %s"
    cursor.execute(query, (encrypted_password, entry_id))

    connection.commit()
    cursor.close()
    connection.close()
    print("Password updated successfully!")

def delete_entry():
    entry_id = int(input("Enter the ID of the entry to delete: "))

    connection = create_connection()
    cursor = connection.cursor()

    query = "DELETE FROM Passwords WHERE id = %s"
    cursor.execute(query, (entry_id,))

    connection.commit()
    cursor.close()
    connection.close()
    print("Entry deleted successfully!")

def main():
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Update Username")
        print("4. Update Password")
        print("5. Delete Entry")
        print("6. Reset IDs")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            update_username()
        elif choice == "4":
            update_password()
        elif choice == "5":
            delete_entry()
        elif choice == "6":
            reset_ids()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
