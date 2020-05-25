from Billbot import BillBot

class MessageService(BillBot):
    
    _bill_bot_base

    def __init__(self, bill_bot_base):
        self._bill_bot_base = bill_bot_base

    def printMessage(self):
        raise NotImplementedError
