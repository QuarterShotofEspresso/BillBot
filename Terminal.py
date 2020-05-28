from MessageService import MessageService

class Terminal(MessageService):

    def print_message(self):
        balance_summary = self._bill_bot_base.print_message()
        print(balance_summary)
        return balance_summary

