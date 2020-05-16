import BillBotFactory


BotFactory = BillBotFactory();

InternetBot = BotFactory.makeabot();
GasBot = BotFactory.makeabot();


InternetBot.sendMessage()
GasBot.sendMessage()
