from twilio.rest import Client

class Sender():
    def __init__(self, ACCOUNT_ID, AUTH_TOKEN, to_number, from_number):
        self.client = Client(ACCOUNT_ID, AUTH_TOKEN)
        self.to_number = to_number
        self.from_number = from_number
    
    def send_img(self,link):
        media = link
        self.client.api.account.messages.create(to=self.to_number,
                                   from_=self.from_number,
                                   body="WE THE CREATORS",
                                   media_url=media
                                   )