import socket

def dns_lookup():
    print("=== DNS Lookup Program ===\n")
    print("1. IP to URL (Reverse Lookup)")
    print("2. URL to IP (Forward Lookup)")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        # Reverse DNS lookup: IP → URL
        ip_address = input("Enter IP address: ")
        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
            print(f"The URL for IP {ip_address} is: {hostname}")
        except socket.herror:
            print("Could not resolve IP address to a hostname.")
    
    elif choice == '2':
        # Forward DNS lookup: URL → IP
        url = input("Enter URL (example.com): ")
        try:
            ip_address = socket.gethostbyname(url)
            print(f"The IP address of {url} is: {ip_address}")
        except socket.gaierror:
            print("Could not resolve URL to an IP address.")
    
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    dns_lookup()
