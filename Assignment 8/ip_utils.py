def ip_to_binary(ip_address: str) -> str:
    """
    Converts a standard dotted-decimal IP address string into a 32-bit binary string
    """
    
    octets = ip_address.split('.')

    print(f"The octets are: {octets}")

    return ""