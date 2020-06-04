from BillBot import BillBot
from getpass import getpass

class ConcreteBot(BillBot):

    __cumulative_message = ''
    __cumulative_total = 0

    def print_message(self):
        _password = getpass()
        for service in self._service_list:
            service_message, service_total = service.fetch_total(_password)
            self.__cumulative_message = self.__cumulative_message + '\n' + service_message
            self.__cumulative_total = self.__cumulative_total + service_total

        self._Message = '='*35 + '\n' + self._Message + '\n' + self.__cumulative_message + \
                '\n' + ('-'*35) + '\nTotal: $' + str(self.__cumulative_total) + \
                '\nTotal per Res.: $' + str(self.__cumulative_total / 4)

        return (self._Message)


