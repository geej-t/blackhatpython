#!/bin/python3

import socket

target_host = "127.0.0.1"
target_port = "80"

#create a socket object

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# receive some data

data, addr = client.rcvfrom(4096)

print(data)