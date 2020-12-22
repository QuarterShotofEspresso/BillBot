# Billbot

> Author(s): Ratnodeep Bandyopadhyay ([@QuarterShotofEspresso](https://github.com/QuarterShotofEspresso))

## What's the app & why is it important?
It's an unfortunate truth that none of my bills are synced. They're all due at different times of the month. Every week I'm afraid that I haven't paid my bills. Every week there's that one day--sometimes really early in the morning--when I wake with a start. Peeling the sheets off and hurling my limp arms towards my laptop. Parsing through the same archive of links. Straining my eyes between the hexagonal characters of my clock and the emboldened numbers under the Bill Due header. When the dates are coming close, I need to divide those ridiculous quantities amongst my roommates and text them each what they owe. I hate this constant, mind-numbing responsibility. Anyone could easily conclude that I'm fairly lazy and somewhat paranoid. And they'd be right. As in the eyes of my grandfather, laze is always feasible, it just depends how far you're willing to go.

Enter Billbot. This nifty, wee API is how far I'm willing to go. Billbot is a tool a user can easily utilize to customize their own bot in navigating, extracting, and sending information to all members of a user's financial party.

## Language and additional tools
The program will be written entirely in Python3. A text messaging service developed by Twilio will be used in order to text members responsible for paying bills. An application called geckodriver will be used to extract information from billing sites. An SMTP library will be used to send emails containing the totals. Also, future personal plans include running the bot in a Rasberry Pi to avoid hogging personal systems.

## User Input / Output
The input documents will be a text file containing all passwords and usernames for each billing site. An additional document will contain the phone numbers of all individuals responsible for payments. The program's output is the sum from each service provider, operated upon by a function defined by the user and the totals are sent to each phone number listed in an external json file.

## UML Diagram
![UML Class Diagram for BillBot](https://github.com/QuarterShotofEspresso/BillBot/blob/master/figures/BillBotUML_rev2.png)
BillBot is made using a set of inherited scripts that are able to perform one of the following functionalities: Data Extraction, Resident Notification, and Message Customization. Of course, message customization isn't automated, but the user has the ability to write a unique message for the group and reuse the bot when necessary. Data Extraction is performed by the NavigationStrat class which has been developed with the strategy pattern. With the numerous sites that each have a unique layout, this requires a unique navigation technique to extract the correct data as quickly as possible. Each site's navigation technique can be defined by the user in a `fetch_total` function which implements the abstract NavigationStrat class. To deliver the finalized message, the MessageService class was designed using the Decorator Pattern. Any number of messaging services, ranging from terminal output to texts or emails can be delivered. In order to ease client usage and increase development speed, BillBot was encased in a simple to use API that synthesizes a bot incredibly fast. The `buildabot` function can be passed with a list of the messaging services, services, and a message header that builds a bot customized to those described parameters.

## Final Report & Usage
The following python3 libraries must be installed in order for BillBot to work: `json`, `getpass`, `selenium`, `twilio`, `ssl`, and `smtplib`. Additionally, [geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.26.0) needs to be installed for those intending to use webdriver to access their billing sites. A sample user program has been provided in `Client.py`. Notice that the existing NavigationStrat implementations (Internet, Electricity, and Gas) can be reconfigured for the user's specific sites. I, for example, have designed those select programs to read the billing site's encrypted login information from a separate json file stored on my computer, and then decrypt it using a password prompted for by the script. It is up to the user to define their navigation technique starting from login information to data extraction and formatting. Regarding Messaging Services, the user can choose exactly who all they would like to contact by adding their emails and/or phone numbers in the respective files under `input/`. In the `input` directory, there are some sample texts demonstrating exactly how this information should be formatted. Below is an image that illustrates the expected output corresponding to the sample use case in `Client.py`.
```
example@example:~$ python3 Client.py
SoCalGas Password: 
Spectrum Password: 
Public Util Password: 
===================================
Hellooo. It's me. Could abc and xyz pls pay the amount below:P

SoCalGas:	    $0.00
Spectrum:	    $0.00
Public Util:	$98.58
-----------------------------------
Total: $98.58
Total per Res.: $24.645
Email Account: <your_email>@gmail.com
Email Password: 

Emailed balance_summary to:
<your_email>@gmail.com

Texted balance_summary to:
<number_1>
<number_2>
<number_3>
<number_4>
```
To give more description on how to use BillBot, there are three variables that need to be explained. The message that is created and sent is called the balance summary. The balance summary descibes the total prices each billing service requests and the cumulative cost from all services. `message_services` contains a list of strings naming each method the user wishes to send the balance summary by.

> Note: The order of the elements in `message_services` and `services` does not matter.

`services` contains a list of strings naming each billing service balance summary should contain. Finally, `message_header` is optional and will be attatched at the beginning of the balance summary. If a particular site, or message service is not wanted, then delete that string from list. `BillBotFactory.buildabot()` is nearly the final step that takes variables described in the previous steps and spits out the billbot configured with the settings you've submitted. BillBot has been designed so when everything is configuered, the script will prompt the user for any additional information. Hope it's fun to use!
