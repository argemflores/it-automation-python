#!/usr/bin/env python3

# Import libraries
import os
from datetime import date
import reports
import emails

if __name__ == '__main__':
    # Define PDF document name and location, and title
    attachment = '/tmp/processed.pdf'
    title = 'Processed Update on ' + date.today().strftime("%B %d, %Y")
    data = []

    # Descriptions directory
    desc_dir = 'supplier-data/descriptions/'

    # List files inside the descriptions directory
    filenames = os.listdir(desc_dir)

    # Process each file
    for filename in filenames:
        # Append the first 2 lines (name, weight) to the data list
        with open(os.path.join(desc_dir, filename)) as file:
            data.append('name: {}<br />weight: {}'.format(file.readline(), file.readline()))

    # Format to separate fruits with double breaks
    paragraph = '<br /><br />'.join(data)

    # print(attachment, title, paragraph)

    # Generate report using title and paragraph
    reports.generate_report(attachment, title, paragraph)
    sender = 'automation@example.com'
    recipient = 'student-03-8f1ad08bdb50@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    message = emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email(message)