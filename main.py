from flask import Flask, request
from flask import render_template
import base64
import pyotp
import time

from db import create_initial_db_resources, create_user, create_secret, get_secret

app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET_FOR_DEMO_APP"

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
        secret_string = pyotp.random_base32()
        print(secret_string)
        totp = pyotp.TOTP(secret_string)
        print(type(totp))
        create_secret(email, secret_string)
        totp_uri = totp.provisioning_uri(name=email, issuer_name="Jagadeesh TOTP Demo")
        print(totp_uri)
        print(totp.now())
        return render_template('token.html', totp_uri="https://chart.googleapis.com/chart?cht=qr&chs=500x500&chl=" + totp_uri)
    except Exception as e:
        print(str(e))
        return render_template('error.html')

    
    


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        try:     
            data = request.form
            email = data['email']
            otp = data['otp']
            user = get_secret(email)
            print(user)
            totp = user[0][1]
            totp = pyotp.TOTP(totp)
            print(otp)
            print(totp.now())
            if totp.now() != otp:
                return render_template('login_fail.html')
            return render_template('login_success.html')
        except Exception as e:
            print(str(e))
            return render_template('login_fail.html')




if __name__ == "__main__":
    create_initial_db_resources()
    app.run(debug=True)

def start_app():
    return app
