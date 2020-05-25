from Internet import Spectrum
from BillBot import BillBot
from Terminal import Terminal

class ConcreteBot(BillBot):
    def printMessage(self):
        return (self._Message + self._site.fetch_total())


mybot = Terminal(ConcreteBot("The final costs:\n", Spectrum()))
mybot.printMessage()
