import BillBot
from enum import Enum

# for user
class eNavStrat(Enum):
    INTERNET = 0
    GAS = 1


class eMsgServ(Enum):
    TWILIO = 0
    EMAIL = 1
    TERMINAL = 2


# bot factory class
class BillBotFactory:
    def makeabot(self, ): # TODO:implement Paramters
        if ()
        return BillBot(); # TODO: implement Parameters
