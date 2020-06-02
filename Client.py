from BillBotFactory import BillBotFactory

# Balance Summary contians: SoCalGas, Spectrum, PublicUtil
services = []

# Balance Summary can be delviered via terminal, email, twilio (text)
message_services = []

message_header = ""

thesupabot = BillBotFactory.buildabot(message_services, services, message_header)
thesupabot.print_message()
