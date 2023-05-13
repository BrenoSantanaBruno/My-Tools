#!/usr/bin/python3

'''
Made by DevStorm Founder
'''


import socket


def is_valid_ipv4(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            number = int(part)
        except ValueError:
            return False
        if number < 0 or number > 255:
            return False
    return True


def get_ip():
    while True:
        ip = input("Digite o IP: ")
        if is_valid_ipv4(ip):
            return ip
        else:
            print("IP inválido. Tente novamente.")


def get_service():
    services = {
        "FTP": 21,
        "SSH": 22,
        "Telnet": 23,
        "SMTP": 25,
        "DNS": 53,
        "HTTP": 80,
        "POP3": 110,
        "IMAP": 143,
        "HTTPS": 443
    }
    while True:
        print("Escolha um serviço dos seguintes:")
        for service in services:
            print(service)
        chosen_service = input()
        if chosen_service in services:
            return services[chosen_service]
        else:
            print("Serviço inválido. Tente novamente.")


ip = get_ip()
porta = get_service()

try:
    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    meusocket.connect((ip, porta))

    banner = meusocket.recv(1024)
    print("Banner recebido:", banner.decode())

    print("Enviando dados para FTP Server - usuário")
    meusocket.send(b"USER teste\r\n")
    banner = meusocket.recv(1024)
    print("Banner recebido:", banner.decode())

    print("Enviando dados para FTP Server - senha")
    meusocket.send(b"PASS teste\r\n")
    banner = meusocket.recv(1024)
    print("Banner recebido:", banner.decode())

except Exception as e:
    print("Erro na conexão:", str(e))

finally:
    meusocket.close()
