
Create_USERS_Table = "Create table if not exists Users(email varchar unique, password varchar)"

Create_USER_SECRET_Table = "Create table if not exists UsersSecret(email varchar unique, totp text)"

Insert_User = "Insert into Users(email, password) values(:email, :password)"

Insert_User_Secret = "Insert into UsersSecret(email, totp) values(:email, :totp)"

Fetch_User_Secret = "Select email, totp from UsersSecret where email=:email"

Fetch_User= "Select email from Users where email=:email"