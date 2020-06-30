from BillBotFactory import BillBotFactory

# Balance Summary contians: SoCalGas, Spectrum, PublicUtil
services = ['specTRum', 'socalgas', 'publicutil', 'rent']

# Balance Summary can be delviered via terminal, email, twilio (text)
message_services = ['terminal', 'twilio']

message_header = input("Message Header: ")

thesupabot = BillBotFactory.buildabot(message_services, services, message_header)
thesupabot.print_message()
