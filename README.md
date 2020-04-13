# Billbot

> Author(s): Ratnodeep Bandyopadhyay ([@QuarterShotofEspresso](https://github.com/QuarterShotofEspresso))

## What's the app & why is it important?
Every week I am afraid that I haven't paid my bills. Every week there's that one day, sometimes really early in the morning, when I wake with a start, rushing over to my laptop slurring through the same enterouage of links. Painfully darting my eyes between the hexagonal characters on watch and the emboldened numbers under the Bill Due header. When the dates are coming close, I need to divide those ridiculous quantities amongst my roommates and text them each what they owe. I hate this constant, mind-numbming responsibility. Anyone could easily conclude that I'm fairly paranoid and equally lazy. And they'd be right. As in the eyes of my grandfather, laze is always feasible, it just depends how far you're willing to go.

Enter Billbot. This nifty, wee API addresses all the issues faced above. Billbot is a tool a user can easily utlize to customize their own bot in navigating, extracting, and sending information via text to all members of a user's financial party!

## Language and additional tools
The API will be written entirely in Python3. A text messaging service developed by Twilio will be used in order to text members responsible for paying bills. Future personal plans include running the bot in a Rasberry Pi to avoid hogging personal systems.

## User Input / Output
The input documents will be a text file containing all passwords and usernames for each billing site. An additional document will contain the phone numbers of all indivduals responsible for payments. The program's output is the sum from each service provider, operated upon by a function defined by the user and the totals are sent to each phone number listed in the second document.

> API

Billbot's API will be expanded as the project continues.
