"""
Created on Sun 12/08/2019 ‏‎03:15:17 AM 2019 

@author: Hady S. Salama
Personal Project
"""

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os


# Your Account Sid and Auth Token from twilio.com/console
# Used Enviornment Variables. This is insecure. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+14404543940',
                        from_='+12564748497'
                    )

print(call.sid)