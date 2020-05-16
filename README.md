# Billbot

> Author(s): Ratnodeep Bandyopadhyay ([@QuarterShotofEspresso](https://github.com/QuarterShotofEspresso))

## What's the app & why is it important?
Every week I am afraid that I haven't paid my bills. Every week there's that one day--sometimes really early in the morning--when I wake with a start. Peeling the sheets off and hurling my limp arms towrads my laptop. Parsing through the same archive of links. Straining my eyes between the hexagonal characters off my clock and the emboldened numbers under the Bill Due header. When the dates are coming close, I need to divide those ridiculous quantities amongst my roommates and text them each what they owe. I hate this constant, mind-numbing responsibility. Anyone could easily conclude that I'm fairly lazy and somwhat paranoid. And they'd be right. As in the eyes of my grandfather, laze is always feasible, it just depends how far you're willing to go.

Enter Billbot. This nifty, wee API is how far I'm willing to go. Billbot is a tool a user can easily utlize to customize their own bot in navigating, extracting, and sending information via text to all members of a user's financial party!

## Language and additional tools
The API will be written entirely in Python3. A text messaging service developed by Twilio will be used in order to text members responsible for paying bills. Future personal plans include running the bot in a Rasberry Pi to avoid hogging personal systems.

## User Input / Output
The input documents will be a text file containing all passwords and usernames for each billing site. An additional document will contain the phone numbers of all indivduals responsible for payments. The program's output is the sum from each service provider, operated upon by a function defined by the user and the totals are sent to each phone number listed in the second document.

## UML Diagram
![UML Class Diagram for BillBot](https://github.com/cs100/final-project-rb/blob/master/diagrams/BillBot.png)
BillBot is made using a set of inherited scripts that are able to perform one of the following functionalities: Data Extraction, Resident Notification, and Message Customaization.
Of course, message customization isn't automated, but the user has the ability to write a unique message for the group and reuse the bot when neccesary.
Data Extraction is performed by the NavigationStrat class which has been developed with the strategy pattern. With the numerous sites that each have a unique layout requires a unique navigation techinque to extract the correct data as quickly as possible. Each site's navigation technique can be defined by the user in a `fetchTotal` function which implments the abstract NavigationStrat class. There are a number of ways to deliver the finalized message. Perhaps the message should be sent in many possible means instead of a select few. For this reason, the MessageService class was designed using the Decorator Pattern. Any number of messaging services, ranging from terminal output to texts can be delivered. In order to ease client usage and increase development speed, BillBot was encased in a simple to use API that synthesizes a bot incredibly fast. The `makeabot` function can be passed with the site's URL, path to the file containing both the username and password to that site, messaging service, and the message itself.
