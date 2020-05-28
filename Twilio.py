import os
from MessageService import MessageService
from twilio.rest import Client

class Twilio(MessageService):

    # all roommate's numbers TODO:: Move off this page
    # __numbers = ['+18588695825', '+19093683901', '+17077617349', '+17077616012']
    __numbers = ['+18588695825']
    def print_message(self):

        balance_summary = self._bill_bot_base.print_message()

        # collect all twilio related data
        SID = os.getenv('TWILIO_ACCOUNT_SID')
        TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
        TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')

        client = Client(SID, TOKEN)

        for number in self.__numbers:
            client.messages.create(to = number, from_ = TWILIO_NUMBER, body = balance_summary)

