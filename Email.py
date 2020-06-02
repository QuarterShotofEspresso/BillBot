from MessageService import MessageService
import ssl
import smtplib
import json
from getpass import getpass

class Email(MessageService):

    __emails = []

    def print_message(self):

        balance_summary = self._bill_bot_base.print_message()

        fio_suite = open('./input/emails.json', 'r')
        self.__emails = json.load(fio_suite)

        port = 465
        smtp_server = 'smtp.gmail.com'
        context = ssl.create_default_context()

        sender_email = input('Email Account: ')
        password = getpass('Email Password: ')

        server = smtplib.SMTP_SSL(smtp_server, port, context=context)
        server.login(sender_email, password)

        print('\nEmailed balance_summary to:')
        for email in self.__emails:
            server.sendmail(sender_email, email, 'Subject: Balance Summary\n\n' + balance_summary)
            print(email + '\n')

        return balance_summary
# Adapted from https://realpython.com/python-send-email/
