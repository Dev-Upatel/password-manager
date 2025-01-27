# Password Manager

## **Overview**
The Password Manager is a Python-based application designed to securely manage and store user passwords for various platforms. It uses MySQL as its database management system and employs cryptography to encrypt passwords, ensuring security.

---

## **Key Features**
1. **Add Passwords**
   - Save platform name, username, and encrypted password to the database.

2. **View Passwords**
   - Decrypt and display all saved passwords in a tabular format for easy viewing.

3. **Update Entries**
   - Update the username or password for an existing entry.

4. **Delete Entries**
   - Permanently remove entries from the database.

5. **Reset IDs**
   - Reorganize IDs sequentially after deletions.

6. **Data Security**
   - Passwords are stored in an encrypted format using a key file, ensuring they cannot be accessed without proper decryption.

7. **Menu-Based Interaction**
   - User-friendly menu for performing operations interactively.

---

## **Setup and Installation**

### **Prerequisites**
- Python 3.13.1
- MySQL Server
- Python Libraries:
  - `mysql-connector-python`
  - `cryptography`

### **Installation Steps**
1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/Dev-Upatel/password-saver
   cd password-saver
   ```

2. **Install Required Libraries:**
   ```bash
   pip install mysql-connector-python cryptography
   ```

3. **Setup MySQL Database:**
   - Create a database named `PasswordManager`:
     ```sql
     CREATE DATABASE PasswordManager;
     ```
   - Create the `Passwords` table:
     ```sql
     CREATE TABLE Passwords (
         id INT AUTO_INCREMENT PRIMARY KEY,
         platform VARCHAR(255),
         username VARCHAR(255),
         password TEXT
     );
     ```

4. **Generate Encryption Key:**
   - Run the following Python snippet to generate a `key.key` file:
     ```python
     from cryptography.fernet import Fernet
     with open("key.key", "wb") as key_file:
         key_file.write(Fernet.generate_key())
     ```

5. **Update Database Credentials:**
   - Edit the `create_connection` function in the Python script with your MySQL credentials:
     ```python
     def create_connection():
         return mysql.connector.connect(
             host="localhost",
             user="root",  # Enter your MySQL username
             password="Hulk.ai",  # Enter your MySQL password
             database="PasswordManager"
         )
     ```

6. **Run the Script:**
   - Start the application:
     ```bash
     python password_manager.py
     ```

---

## **How to Use**
1. **Launch the Script**
   - The program will display an interactive menu with various options:
     ```
     Password Manager
     1. Add Password
     2. View Passwords
     3. Update Username
     4. Update Password
     5. Delete Entry
     6. Reset IDs
     7. Exit
     ```

2. **Choose an Option**
   - Follow the prompts for the selected operation. For example:
     - To add a password, input the platform name, username, and password as requested.
     - To view passwords, select option `2`.

3. **Secure Password Storage**
   - All passwords are encrypted before storage, ensuring security even if the database is compromised.

4. **Exit the Application**
   - Select option `7` to quit.

---

## **Technical Details**
1. **Programming Language:**
   - Python 3.13.1

2. **Database:**
   - MySQL for persistent storage.

3. **Encryption Method:**
   - Symmetric encryption using Fernet from the `cryptography` library.

4. **Key File:**
   - The `key.key` file is used to encrypt and decrypt passwords. Ensure this file is stored securely and backed up.

---

## **Security Recommendations**
- Keep the `key.key` file secure and private.
- Use strong and unique passwords for the MySQL database.
- Regularly back up the database.
- Implement access control to restrict unauthorized usage.

---

## **Future Enhancements**
- Add search functionality to quickly locate specific passwords.
- Export passwords to an encrypted file for offline storage.
- Implement a master password to protect access to the application.
- Create a graphical user interface (GUI) for improved usability.

---

## **Support**
For assistance, please contact:
- **Email:** codebot.aii@gmail.com
- **GitHub Repository:** [https://github.com/Dev-Upatel/password-saver](https://github.com/Dev-Upatel/password-saver)
- **GitHub Profile:** [https://github.com/Dev-Upatel/](https://github.com/Dev-Upatel/)

