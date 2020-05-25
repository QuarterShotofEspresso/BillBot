from MessageService import MessageService

class Terminal(MessageService):

    def printMessage(self):
        balance_summary = self._bill_bot_base.printMessage()
        print(balance_summary)
        return balance_summary

