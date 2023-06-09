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

def get_port():
    while True:
        try:
            porta = int(input("Digite a porta: "))
            if 1 <= porta <= 65535:
                return porta
            else:
                print("Número de porta inválido. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número.")

ip = get_ip()
porta = get_port()

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    meusocket.connect((ip, porta))
    print("Conexão bem sucedida.")
    banner = meusocket.recv(1024)
    print("Banner recebido:", banner.decode())
except Exception as e:
    print("Erro ao conectar:", str(e))
finally:
    meusocket.close()
