#testing if module imported
try:
    import socket
except:
    print("There was an error importing a necessary module.")
    print("Please make sure you have the 'socket' module installed.")
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
        #appending failed hosts
        except socket.gaierror:
            with open("failed.txt", "a") as output:
                output.write(name + '\n')

if __name__ == "__main__":
    main()
