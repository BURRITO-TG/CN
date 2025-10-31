# File Name: ip_utils.py

def ip_to_binary(ip_address: str) -> str:
    """
    Converts a standard dotted-decimal IP address string into a 32-bit binary string.
    """
    
    # 1. Split the IP address
    octets = ip_address.split('.')
    
    binary_octets = [] 
    
    # 2. Loop through each string in the 'octets' list
    for octet_str in octets:
        # 2a. Convert to integer
        num = int(octet_str)
        
        # 2b. Convert to binary and remove "0b"
        binary_str = bin(num)[2:]
        
        # 2c. Pad with leading zeros to ensure it's 8 bits long 
        #     e.g., "1" becomes "00000001"
        #     e.g., "11000000" stays "11000000"
        padded_binary_str = binary_str.zfill(8)
        
        print(f"Original: {binary_str} -> Padded: {padded_binary_str}")
        
        # 2d. Add the 8-bit string to our list
        binary_octets.append(padded_binary_str)
    
    print(f"The padded binary octets are: {binary_octets}")
    
    # 3. Join all the 8-bit strings (e.g., ['11000000', '10101000', ...])
    #    into a single 32-bit string.
    full_binary_string = "".join(binary_octets)
    
    print(f"The full 32-bit string is: {full_binary_string}")
    
    # 4. Return the final string
    return full_binary_string

# (Continuing in ip_utils.py)

def get_network_prefix(ip_cidr: str) -> str:
    """
    Takes a CIDR notation string and returns the network prefix as a binary string.
    """
    
    # 1. Split the CIDR string "200.23.16.0/23" into the IP and the prefix length
    #    ip_address will be "200.23.16.0"
    #    prefix_len_str will be "23"
    try:
        ip_address, prefix_len_str = ip_cidr.split('/')
    except ValueError:
        print("Error: Invalid CIDR format. Expected 'IP/Prefix'.")
        return "" # Return empty string on error

    print(f"The IP part is: {ip_address}")
    print(f"The prefix length string is: {prefix_len_str}")
    
    # --- We will add more code here ---
    
    return "" # For now