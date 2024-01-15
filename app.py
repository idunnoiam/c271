from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant


app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/token')
def generate_token():
    #add your twilio credentials 
    TWILIO_ACCOUNT_SID = 'AC0fae3082f47eebc777d1b988fbf60ab5'
    TWILIO_SYNC_SERVICE_SID = 'ISc9149079350660dbe43dc8e392936649'
    TWILIO_API_KEY = 'SKc56172eb562af83c38f8f06ece85a94a'
    TWILIO_API_SECRET = 'tGa5d4DorPI7QRLDxBhrQc3x0D1g3cPv'

    username = request.args.get('username', fake.user_name())
    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)
    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username, token=token.to_jwt().decode())



if __name__ == "__main__":
    app.run(port=5001)

