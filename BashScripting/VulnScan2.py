#!/bin/python3
import socket
from IPy import IP
import pyfiglet
import subprocess
import time
from datetime import datetime
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
for port in range(int(start_port),int(end_port)):
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
                except:
               banners.append(' ')
               sock.close()
        except:
           pass
try:

         for port in range (1,4000):
                 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                 result = s.connect_ex((target, port))
                 if result ==0:
                  print ("Port {}: is open".format(port))
                 s.close()
except KeyboradInterrupt:
 print ("\n The Scan Was Canceled")



if __name__ == "__main__":
    targets = input('[+] Enter Target/s To Scan(for multiple targets use a coma): ')
    start_port = input('enter the port to start the scan: ')
    end_port = input('enter the port to end the scan: ')
    #check start time
    time_start = datetime.now().replace(microsecond=0)
print("Scanning started at:" + str(time_start))

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

#check completed time
time_completed = datetime.now().replace(microsecond=0)

#Total time the Scan took
time_total = time_completed - time_start

print("Scanning ended at:" + str(time_completed))
print("Scanning Completed in " + str(time_total))
