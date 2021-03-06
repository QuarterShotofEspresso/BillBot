import os
import sys
import json
from MessageService import MessageService
from twilio.rest import Client

class Twilio(MessageService):

    # all roommate's numbers TODO:: Move off this page
    __numbers = []

    def print_message(self):


        fio_suite = open('/home/elvasio/Projects/billbot/input/phone_numbers.json', 'r')
        self.__numbers = json.load(fio_suite)
        #self.__numbers = [self.__numbers[0]]  # modifiying line, only sending to myself NOTE::may want to add functionlity in the future to select specfic numbers

        balance_summary = self._bill_bot_base.print_message()
        
        if( '-s' in sys.argv ):
            return balance_summary

        # collect all twilio related data
        SID = os.getenv('TWILIO_ACCOUNT_SID')
        TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
        TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')

        client = Client(SID, TOKEN)

        print('\nTexted balance_summary to:')
        for number in self.__numbers:
            client.messages.create(to = number, from_ = TWILIO_NUMBER, body = balance_summary)
            print(number)

        return balance_summary
