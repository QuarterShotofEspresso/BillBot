from Internet import Spectrum
from BillBot import BillBot
from Terminal import Terminal
from Twilio import Twilio

class ConcreteBot(BillBot):
    def print_message(self):
        return (self._Message + self._site.fetch_total())


mybot = Terminal(ConcreteBot("The final costs:\n", Spectrum()))
mybot.print_message()
