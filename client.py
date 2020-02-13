#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:21:19 2020

@author: zeus
"""

import socket


HOST, PORT = "localhost", 4000
data = "1"

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
received = ""
try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = (str(sock.recv(1024))).strip()
    
    
    
except Exception as e:
     print(e)

print("Sent:     {}".format(data))
print("Received: {}".format(received))
sock.close()