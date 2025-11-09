import ipaddress

def subnetting():
    print("=== Subnetting and Subnet Mask Finder ===\n")
    
    # Step 1: Input network IP and number of subnet bits to borrow
    ip = input("Enter a network IP address (e.g., 192.168.1.0): ")
    subnet_bits = int(input("Enter number of subnet bits to borrow (e.g., 2): "))

    # Step 2: Create base network (default /24 for Class C)
    network = ipaddress.IPv4Network(ip + '/24', strict=False)

    # Step 3: Calculate new subnet mask after borrowing bits
    new_prefix = 24 + subnet_bits

    print(f"\nOriginal Network       : {network}")
    print(f"Original Subnet Mask   : {network.netmask}")
    
    # Step 4: Generate subnets
    subnets = list(network.subnets(prefixlen_diff=subnet_bits))
    print(f"\nTotal Subnets Created  : {len(subnets)}")
    print(f"New Subnet Mask        : {subnets[0].netmask}\n")

    # Step 5: Display details of each subnet
    for i, subnet in enumerate(subnets):
        hosts = list(subnet.hosts())  # List of usable host IPs
        print(f"Subnet {i+1}:")
        print(f"  Network Address     : {subnet.network_address}")
        print(f"  Broadcast Address   : {subnet.broadcast_address}")
        if hosts:
            print(f"  Host Range          : {hosts[0]} - {hosts[-1]}")
        else:
            print("  Host Range          : None (no usable hosts)")
        print(f"  Total Usable Hosts  : {subnet.num_addresses - 2}\n")

if __name__ == "__main__":
    subnetting()
