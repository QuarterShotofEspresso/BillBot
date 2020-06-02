from BillBotFactory import BillBotFactory

message_services = ['terminal', 'email', 'twilio']
services = ['socalgas', 'spectrum', 'publicutil']
message_header = "Hellooo. It's RB. This number will provide our bills from now on. Emma 'n Ethan could you guys pay the amount below:P"

thesupabot = BillBotFactory.buildabot(message_services, services, message_header)
thesupabot.print_message()
