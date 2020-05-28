import json

class BillBot:
    
    # variables
    _Message = 0
    _site = 0

    # Constructor for BillBot base class
    def __init__(self, msg, site):
        self._Message = msg
        self._site = site

    def print_message(self):         # virtual function declaration
        raise NotImplementedError
