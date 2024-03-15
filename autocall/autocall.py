# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

                        # to='+19082551638',
b=True
while(b):
    b = False
    # call = client.calls.create(
    #                         url='http://demo.twilio.com/docs/classic.mp3',
    #                         to='+19082551638',
    #                         from_='+16313270064'
    #                     )
    call = client.calls.create(
                            url='http://demo.twilio.com/docs/classic.mp3',
                            to='+16317672004',
                            from_='+16313270064'
                        )

    print(call.sid)

