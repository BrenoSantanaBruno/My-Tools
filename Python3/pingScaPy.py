from scapy.all import *
import sys

conf.verbose = 0

for ip in range(1, 256):
    iprange = "192.168.0." + str(ip)
    pacote = IP(dst=iprange)/ICMP()
    pIP = IP(dst=iprange)
    pICMP = ICMP()
    pacote = pIP/pICMP
    resp, noresp = sr(pacote, timeout=1)
    print("IP: ", iprange)
    print (resp.summary())
    print("Respostas: " , len(resp))
    print("Sem resposta: ", len(noresp))
    print ("-"*60)
    print(resp.show())
    for resposta in resp:
        print(resposta[1][IP].src, "está respondendo")


