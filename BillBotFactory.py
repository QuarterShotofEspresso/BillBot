from BillBot import BillBot
from Internet import Spectrum
from Gas import SoCalGas
from Twilio import Twilio
from Terminal import Terminal
from ConcreteBot import ConcreteBot

# bot factory class
class BillBotFactory:

    __return_bot = 0
    __service_list = []


    @classmethod
    def buildabot(cls, message_service_string_list = [], service_string_list = [], message = ''):
        
        for service_string in service_string_list:
            cls.append_service(service_string)

        cls.__return_bot = ConcreteBot(message, cls.__service_list)

        for message_service_string in message_service_string_list:
            cls.append_message_service(message_service_string)

        return cls.__return_bot;


    @classmethod
    def append_service(cls, service_string):
        if (service_string.lower() == 'socalgas'):
            cls.__service_list.append(SoCalGas())
        elif (service_string.lower() == 'spectrum'):
            cls.__service_list.append(Spectrum())
        else:
            raise ValueError


    @classmethod
    def append_message_service(cls, message_service_string):
        if (message_service_string.lower() == 'twilio'):
            cls.__return_bot = Twilio(cls.__return_bot)
        elif (message_service_string.lower() == 'terminal'):
            cls.__return_bot = Terminal(cls.__return_bot)
        elif (message_service_string.lower == 'email'):
            cls.__return_bot = Email(cls.__return_bot)
        else:
            raise ValueError
