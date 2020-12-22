import sys
from BillBot import BillBot


class MessageService(BillBot):
    
    _bill_bot_base = 0

    def __init__(self, bill_bot_base):
        self._bill_bot_base = bill_bot_base

    def print_message(self):
        raise NotImplementedError
