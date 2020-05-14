import os
from twilio.rest import Client

def send(body='Some body', to=''):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = os.environ['account_sid']
    auth_token = os.environ['auth_token']
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Hello from Violeta! You will get this code to work!",
                        from_='+12058097070',
                        to='+17863872263'+to
                    )

    print(message.sid)