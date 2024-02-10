from colorama import *
import os, sys

os.system("cls")

banner =  Fore.BLUE + """
 ____                            _          ____     _        
|  _ \   ___   _ __ ___    __ _ (_) _ __   |___ \   (_) _ __  
| | | | / _ \ | '_ ` _ \  / _` || || '_ \    __) |  | || '_ \ 
| |_| || (_) || | | | | || (_| || || | | |  / __/   | || |_) |
|____/  \___/ |_| |_| |_| \__,_||_||_| |_| |_____|  |_|| .__/ 
                                                       |_|    
"""
banner2 = Fore.RED + """
            Version:1.0 - By: @Bernard-Appiah
            https://github.com/graciousnm
            Support for more scripts coming soon!
"""
print(banner)
print(banner2)

print(Fore.RED + "[NOTE] " + Fore.WHITE + "Results will also be saved in " + Fore.BLUE + "ip_address.txt" +  Style.RESET_ALL+ "\n")

#testing if module imported
try:
    import socket
except:
    print("There was an error importing a necessary module.")
    print("Please make sure you have the 'socket' and 'sys' modules installed.")
    exit()

def main():
    #Getting user input for hostnames
    with open("hosts.txt", "r") as input_file:
        hosts = input_file.read()
        #turning content in text file into a list
        host = hosts.split()
    for name in host:
        try:
            #Resolving IP addresses using gethostbyname function from socket module
            ip_address = socket.gethostbyname(name)
            #appending the resolved  address to the end of each line
            with open("ip_address.txt", "a") as output:
                output.write(ip_address + '\n')
                print(Fore.GREEN +"[+] " + Fore.WHITE + name , Fore.BLUE + "==>",  Fore.YELLOW + ip_address + Style.RESET_ALL)
        #appending failed hosts
        except socket.gaierror:
            with open("failed.txt", "a") as output:
                output.write(name + '\n')

if __name__ == "__main__":
    main()
