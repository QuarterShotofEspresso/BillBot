from BillBotFactory import BillBotFactory

# Balance Summary contians: SoCalGas, Spectrum, PublicUtil
services = ['specTRum', 'socalgas', 'publicutil']

# Balance Summary can be delviered via terminal, email, twilio (text)
message_services = ['terminal', 'email', 'twilio']

message_header = "Hey guys, It's me RB. Could pay these amounts pls."

thesupabot = BillBotFactory.buildabot(message_services, services, message_header)
thesupabot.print_message()
