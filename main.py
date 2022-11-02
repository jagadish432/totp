from flask import Flask, request
from flask import render_template

from db import create_initial_db_resources, create_user


app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/')
def create_account():
    return render_template('register.html')


@app.route('/register', methods = ['POST'])
def register():
    try:
        data = request.form
        email = data['email']
        password = data['psw']
        print("creating user")
        create_user(email, password)
        return render_template('login.html')
    except Exception as e:
        print(str(e))

    
    


@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    create_initial_db_resources()
    app.run(debug=True)

def start_app():
    return app
