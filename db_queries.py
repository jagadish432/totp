
Create_USERS_Table = "Create table if not exists Users(email varchar unique, password varchar)"

Insert_User = "Insert into Users(email, password) values(:email, :password)"