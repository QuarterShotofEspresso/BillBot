from Internet import Spectrum     # implement Internet
#import Gas          # implement Gas

class BillBot:
    
    # variables
    _Message
    __site

    # Constructor for BillBot base class
    def __init__(self, msg, site):
        self._Message = msg
        self.__site = site

    def printMessage(self):         # virtual function declaration
        raise NotImplementedError
