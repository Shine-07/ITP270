#!/bin/python3
import socket
from IPy import IP
import pyfiglet
import subprocess
import time

#//clear terminal
subprocess.call('clear', shell=True)

#//PS banner
Port_Scanner_Banner = pyfiglet.figlet_format("PORT SCANNER")
print(Port_Scanner_Banner)

#//wait one second befor proceeding
time.sleep(1)
#list to store open ports
ports = []
#list to store discovered banners
banners = []
def scan(target) :
        '''//scan target function//'''
        converted_ip = convert_ip(target)
        print('\n' + ' Scanning Target : ' + str(target))
for port in range(21,80):
            scan_port(converted_ip, port)

def convert_ip(ip):
     try:
           IP(ip)
           return(ip)
     except ValueError:
          return socket.gethostbyname(ip)

 #def get_banner(s):
        #       '''//function grab any port banner and return the data receved//'''
  #       return s.recv(1024)

def scan_port(ipaddress, port):
        try:
            sock = socket.socket()
            sock.settimeout(.01)
            sock.connect((ipaddress, port))

            try: 
                ports.apppend(port)
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                banners.append(banner)
 banners.append(banner)
            except:
               banners.append(' ')
               sock.close()
        except:
           pass

if __name__ == "__main__":
    targets = input('[+] Enter Target/s To Scan(for multiple targets use a coma): ')
    if ',' in targets:
        for ip_address in targets.split(','):
            scan(ip_address.strip(' '))
    else:
        scan(targets)
with open("vulnerable_banners.txt", 'r') as file:
     count = 0
     for banner in banners:
         file.seek(0)
         for line in file.readlines():
            if line.strip() in banner:
                print('[!!] VULNERABLE BANNER: "' + banner + '" ON PORT: ' + str(ports[count]))
         count += 1
