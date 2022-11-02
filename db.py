import sqlite3
from db_queries import *

conn = sqlite3.connect('dbdata.db', check_same_thread=False)

def create_initial_db_resources():
    
    conn.execute(Create_USERS_Table)

    # Create_USER_SECRET_Table = "Create table UsersSecret(email varchar, totp text) if not exists"
    

def create_user(email, password):
    conn.execute(Insert_User, {
        'email': email,
        'password': password
    })
    print("created users successfully")


