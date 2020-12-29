#!/usr/bin/env python3

from email.message import EmailMessage

# Create an empty email message
message = EmailMessage()
print(message) # prints nothing

# Define sender and recipient of email
sender = 'argemgerald@gmail.com' # 'me@example.com'
recipient = 'argemflores@gmail.com' # 'you@example.com'

# Add them to the From and To fields
message['From'] = sender
message['To'] = recipient
print(message) # prints sender and recipient emails

# Add subject
message['Subject'] = 'Greetings from {} to {}'.format(sender, recipient)
print(message) # prints sender and recipient emails, and subject

# Add a message body
body = """Hey there!

I'm learning to send emails using Python!"""
message.set_content(body)
print(message) # prints sender and recipient emails, subject, body, and other details

##########

import os.path

# Define attachment path and filename
attachment_path = 'Zagreus.png'
attachment_filename = os.path.basename(attachment_path)

import mimetypes

# Guess mimetype of attachment file
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type) # prints image/png

# Split up mime_type as required by EmailMessage
mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type) # prints image
print(mime_subtype) # prints png

# Add attachment to email message
with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(attachment_path))
# print(message) # prints the email message details and a bunch of code

##########

import smtplib

# Create an smtp.SMTP object and connect to local machine
# mail_server = smtplib.SMTP('localhost') # error

# Create an SMTP connection over SSL/TLS
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')

# mail_server.set_debuglevel(1) # shows debugging information

import getpass

# Prompt password for sender's email
mail_pass = getpass.getpass('Password? ')

# Log in to mail server using credentials
mail_server.login(sender, mail_pass)

# Send the message
mail_server.send_message(message)

# Close connection to the mail server
mail_server.quit()
