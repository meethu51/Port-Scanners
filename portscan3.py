#!/usr/bin/python

#this program will scan multiple ports
import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("[*]Enter the host to scan : ")
#port = int(raw_input("[*]Enter the port to scan : "))

def portscanner(port):
        if sock.connect_ex((host,port)):
                print(colored("[!!]Port %d is closed" % (port), "red"))
        else:
                print(colored("[+]Port %d is opened" % (port), "green"))


for port in range (1,100):
	portscanner(port)
