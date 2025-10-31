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

if __name__ == "__main__":
    ip = "67.69.6.7"
    binary_ip = ip_to_binary(ip)
    print(f"The binary representation of IP {ip} is: {binary_ip}")