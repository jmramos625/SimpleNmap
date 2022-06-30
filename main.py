import os


def escanear(ip):
    os.system(f"nmap -A -p- -Pn {ip} -v")
    os.system(f"dirb {ip}")  # implementação do DIRB


escanear(input("Qual IP(s) gostaria de escanear: "))
