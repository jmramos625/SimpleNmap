import os


def escanear(ip):
    os.system(f"nmap -A -p- -Pn {ip} -v")


escanear(input("Qual IP(s) gostaria de escanear: "))
