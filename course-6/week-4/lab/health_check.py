#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails

def check_disk_usage(disk, percentage):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > percentage

def check_cpu_usage(percentage):
    usage = psutil.cpu_percent(1)
    return usage < percentage

def check_memory_usage(size):
    vmem = psutil.virtual_memory()
    return vmem.available / 1024**2

def check_hostname(ip, hostname):
    return socket.gethostbyname(hostname) == ip


if __name__ == "__main__":
    subject = ''
    if not check_cpu_usage(80):
        subject = 'Error - CPU usage is over 80%'
    if not check_disk_usage('/', 20):
        subject = 'Error - Available disk space is less than 20%'
    if not check_memory_usage(500):
        subject = 'Error - Available memory is less than 500MB'
    if not check_hostname('127.0.0.1', 'localhost'):
        subject = 'Error - localhost cannot be resolved to 127.0.0.1'

    if subject != '':
        #print(subject)
        sender = 'automation@example.com'
        recipient = 'student-03-8f1ad08bdb50@example.com'
        body = 'Please check your system and resolve the issue as soon as po$
        message = emails.generate_email(sender, recipient, subject, body, No$
        emails.send_email(message)


