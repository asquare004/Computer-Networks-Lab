from scapy.all import ARP, Ether, srp

def scan_network(network_range):
    """
    Scans the provided subnet for active devices using ARP requests.
    
    :param network_range: The subnet to scan (e.g., "192.168.1.0/24").
    :return: List of tuples (IP, MAC) of active devices.
    """
    # Create an ARP request packet
    arp_request = ARP(pdst=network_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff") # Broadcast MAC address
    packet = broadcast / arp_request # Combine Ethernet and ARP layers

    # Send the packet and capture responses
    answered, _ = srp(packet, timeout=2, verbose=False)
    
    # Store the results
    results = []
    for sent, received in answered:
        results.append((received.psrc, received.hwsrc))

    return results

if __name__ == "__main__":
    # Take user input for subnet
    network_range = input("Enter the subnet to scan (e.g., 192.168.1.0/24): ")

    # Scan the network
    scanned_results = scan_network(network_range)

    # Save results to a text file
    output_file = "scan_results.txt"
    with open(output_file, "w") as file:
        file.write("IP Address\t\tMAC Address\n")
        file.write("------------------------------------------\n")
        for ip, mac in scanned_results:
            file.write(f"{ip}\t\t{mac}\n")

    print(f"\nScan complete! Results saved to {output_file}")
