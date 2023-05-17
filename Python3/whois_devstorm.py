#!/usr/bin/env python3

import socket
import sys
import time

def query_whois_server(hostname, server, port=43, timeout=5):
    """
    Consulta o servidor WHOIS fornecido para o hostname dado.

    Retorna a resposta do servidor como um objeto bytes.
    """
    with socket.create_connection((server, port), timeout=timeout) as sock:
        sock.sendall((hostname + "\r\n").encode())
        response = b''
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break  # Servidor fechou a conexão
            response += chunk
    return response

def find_refer_server(iana_response):
    """
    Analisa a resposta do servidor WHOIS da IANA para encontrar o servidor de referência.

    Retorna o servidor de referência como uma string, ou None se não puder ser encontrado.
    """
    for line in iana_response.split(b'\n'):
        if line.lower().startswith(b'refer:'):
            return line.split(b':', 1)[1].strip().decode()
    return None

def main():
    if len(sys.argv) < 2:
        print("Uso: whois.py [hostname...]")
        sys.exit(1)

    hostnames = sys.argv[1:]

    for hostname in hostnames:
        print(f"\nProcurando {hostname}...")

        print("Consultando IANA...")
        iana_response = query_whois_server(hostname, "whois.iana.org")
        refer_server = find_refer_server(iana_response)

        if not refer_server:
            print("Não foi possível encontrar o servidor de referência.")
            continue

        print("REFER: " + refer_server)

        print("Carregando... By DevStorm")
        time.sleep(2)

        print(f"Consultando {refer_server}...")
        refer_response = query_whois_server(hostname, refer_server)
        print(refer_response.decode())

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Erro: {e}", file=sys.stderr)
        sys.exit(1)
