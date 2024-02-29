import sqlite3 
import hashlib
import string


class SignUp:
    def __init__(self):
        self.dbName = "databases/users.sqlite3"
        self.connect()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id TEXT PRIMARY KEY,
                            first_name TEXT,
                            last_name TEXT,
                            birth_date TEXT,
                            telephone TEXT UNIQUE,
                            password TEXT,
                            specialization TEXT
                        )''')
        
        self.close()

    def connect(self):
        self.connection = sqlite3.connect(self.dbName)
        self.cursor = self.connection.cursor()
        print("Connected to database successfully.")

    def close(self):
        self.connection.close()
        print("Database connection closed.")


    def signUp(self, first_name, last_name, birth_date, telephone, password, specialization):
        self.connect()
        try : 
            user_info = f"{first_name}{last_name}{birth_date}{telephone}{password}{specialization}".replace(" ","W")
            id_ = hashlib.sha1(user_info.encode()).hexdigest()[:9]

            self.cursor.execute('''INSERT INTO users 
                (id, first_name, last_name, birth_date, telephone, password, specialization) 
                VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                (id_, first_name, last_name, birth_date, telephone, password, specialization))
            
            self.connection.commit()
            self.close()

            return True

        except Exception as e : 
            self.close()
            return False
        






class LogIn : 
    def __init__(self):
        self.dbName = "databases/users.sqlite3"
        self.connect()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id TEXT PRIMARY KEY,
                            first_name TEXT,
                            last_name TEXT,
                            birth_date TEXT,
                            telephone TEXT UNIQUE,
                            password TEXT,
                            specialization TEXT
                        )''')
        
        self.close()


    def connect(self):
        self.connection = sqlite3.connect(self.dbName)
        self.cursor = self.connection.cursor()
        print("Connected to database successfully.")


    def close(self):
        self.connection.close()
        print("Database connection closed.")


    def logIn(self, id_or_tel, password):
        # Check if the provided ID or telephone number matches with stored user information
        self.connect()
        self.cursor.execute('''SELECT * FROM users WHERE id=? OR telephone=?''', (id_or_tel, id_or_tel))
        user = self.cursor.fetchone()

        if user:
            # If a user with the provided ID or telephone number is found, check the password
            stored_password = user['password']
            if password == stored_password:
                return True
            else:
                return False
        else:
            self.close()
            return False


        



