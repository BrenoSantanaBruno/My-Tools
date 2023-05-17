#!/bin/bash

import socket
import sys
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.iana.org",43))
s.send((sys.argv[1] + "\r\n").encode())

resposta = s.recv(1024).split()
whois = (resposta[19].decode())
print ("REFER: "+whois)
s.close()
print("Carregando... By DevStorm")
time.sleep(2)


s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((whois,43))
s1.send((sys.argv[1] + "\r\n").encode())
resposta2 = s1.recv(1024)
print (resposta2.decode())
s1.close()

