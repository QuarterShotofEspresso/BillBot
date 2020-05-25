from MessageService import MessageService

class Terminal(MessageService):

    def printMessage():
        balance_summary = self._bill_bot_base.printMessage()
        print( balance_summary )
        return balance_summary

