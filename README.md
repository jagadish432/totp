# totp
Demo project for TOTP based MFA Auth using Flask application

In a terminal, run the following commands:

1. python -m venv venv

2. source venv/bin/activate

3. pip install -r requirements.txt

4. python main.py


Open browser and open http://127.0.0.1:5000 as prompted in the terminal after the 4th step:
5. provide email and password

6. Scan the QRCode using any App-based authenticators like Google Authenticator, Microsoft Authenticator, Twilio Authy, etc..

7. Navigate to the Login Screen either by clicking on "Sign in" button, or add /login to the base URL in the browser's URL section

8. provide the registered email and the TOTP shown on the authenticator app

9. Validate you get the success page or not.