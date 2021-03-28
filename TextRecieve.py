# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from flask import Flask, request
from twilio import twiml

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC739e6cc65ada907d6d86ab6de40a05f3'
auth_token = '5fbfd7009894b58b380c5f0015b615c1'
client = Client(account_sid, auth_token)

messages = client.messages.list(limit=20)

for record in messages:
    print(record.sid)
    print(record.body)




"""
app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    #print("From: " + number + " Body: " + message_body)

    resp = twiml.Response()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    client.messages.create(to="+14404543940", 
                       from_="+12564748497",
                       body=resp.message)
    return str(resp)

if __name__ == '__main__':
    app.run()
"""