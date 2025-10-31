def ip_to_binary(ip_address: str) -> str:
    """
    Converts a standard dotted-decimal IP address string into a 32-bit binary string
    """
    
    octets = ip_address.split('.')

    binary_octets = []
    for octet in octets:
        num = int(octet)

        binary_str=bin(num)[2:]

        print(f"String: {octet} -> Int: {num} -> Binary: {binary_str}")
        binary_octets.append(binary_str)
    print(f"The binary octets are: {binary_octets}")

    return ""

if __name__ == "__main__":
    ip = "67.69.6.7"
    binary_ip = ip_to_binary(ip)