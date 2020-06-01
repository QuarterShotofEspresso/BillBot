from BillBotFactory import BillBotFactory

message_services = ['terminal']
services = ['socalgas', 'spectrum']
message_header = "Hey guys, here are the amounts:"

thesupabot = BillBotFactory.buildabot(message_services, services, message_header)
thesupabot.print_message()
