from scapy.all import *
import sys


conf.verb = 0

# portas = [21,22,23,25,80,443,110]

#TODO melhorar a forma de receber os argumentos
#TODO adicionar opção de receber um range de portas
#TODO adicionar opção de receber um arquivo com portas
#TODO adicionar opção de receber um arquivo com ips
#TODO adicionar opção de receber um range de ips
#TODO adicionar opção de receber um arquivo com ips e portas

pIP = IP(dst=sys.argv[1])
pTCP = TCP(dport=range(int(sys.argv[2])), flags="S")
#pTCP = TCP(dport=portas, flags="S")
pacote = pIP/pTCP
resp, noresp = sr(pacote)
for resposta in resp:
    porta = resposta[1][TCP].sport
    flag = resposta[1][TCP].flags
    if flag == "SA":
        print("Porta %d ABERTA" %porta)
    else:
        print("Porta %d FECHADA" %porta)




