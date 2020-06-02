from BillBotFactory import BillBotFactory

message_services = ['terminal', 'email', 'twilio']
services = ['socalgas', 'spectrum', 'publicutil']
#services = ['socalgas']
message_header = "Hellooo. It's me. Could abc and xyz pay the amount below:P"

thesupabot = BillBotFactory.buildabot(message_services, services, message_header)
thesupabot.print_message()
