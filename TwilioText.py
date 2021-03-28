"""
Created on Sun 12/08/2019 ‏‎02:55:27 AM 2019 

@author: Hady S. Salama
Personal Project
"""
# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
import os

# Your Account Sid and Auth Token from twilio.com/console
# Used Environment Variables. This is insecure. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+14404543940", 
                       from_="+12564748497", 
                       body="Hello from Python with Environment Variables!")