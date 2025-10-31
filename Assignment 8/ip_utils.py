def ip_to_binary(ip_address: str) -> str:
    """
    Converts a standard dotted-decimal IP address string into a 32-bit binary string.
    """
    
    octets = ip_address.split('.')
    
    binary_octets = [] 
    
    for octet_str in octets:
        num = int(octet_str)
        
        binary_str = bin(num)[2:]
        
        padded_binary_str = binary_str.zfill(8)
        
        print(f"Original: {binary_str} -> Padded: {padded_binary_str}")
        
        binary_octets.append(padded_binary_str)
    
    print(f"The padded binary octets are: {binary_octets}")
    
    full_binary_string = "".join(binary_octets)
    
    print(f"The full 32-bit string is: {full_binary_string}")
    
    return full_binary_string

def get_network_prefix(ip_cidr: str) -> str:
    """
    Takes a CIDR notation string and returns the network prefix as a binary string.
    """
    
    try:
        ip_address, prefix_len_str = ip_cidr.split('/')
    except ValueError:
        print("Error: Invalid CIDR format. Expected 'IP/Prefix'.")
        return ""

    prefix_len = int(prefix_len_str)
    full_binary_ip = ip_to_binary(ip_address)
    
    network_prefix = full_binary_ip[:prefix_len]
    
    print(f"The final network prefix is: {network_prefix}")
    
    return network_prefix

if __name__ == "__main__":
    
    print("\n--- Testing Part 1: IP Utilities ---")
    
    ip1 = "192.168.1.1"
    binary_ip1 = ip_to_binary(ip1)
    print(f"\nTest: ip_to_binary({ip1})")
    print(f"Output: {binary_ip1}")
    print(f"Expected: 11000000101010000000000100000001")
    
    print("-" * 20)
    
    cidr1 = "200.23.16.0/23"
    prefix1 = get_network_prefix(cidr1)
    print(f"\nTest: get_network_prefix({cidr1})")
    print(f"Output: {prefix1}")
    print(f"Expected: 11001000000101110001000")