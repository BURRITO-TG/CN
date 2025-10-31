try:
    from ip_utils import ip_to_binary, get_network_prefix
except ImportError:
    print("Error: Could not find ip_utils.py.")
    print("Please make sure ip_utils.py is in the same directory.")
    exit()

class Router:
    
    def __init__(self, routes: list):
        # (This code is already written)
        print(f"Initializing router with {len(routes)} routes...")
        self.forwarding_table = [] 
        self._build_forwarding_table(routes)
        print("Router is ready.")
        print(f"Internal Forwarding Table (sorted): {self.forwarding_table}") 

    
    def _build_forwarding_table(self, routes: list):
        # (This code is already written)
        processed_table = []
        for route_tuple in routes:
            cidr = route_tuple[0]
            link = route_tuple[1]
            binary_prefix = get_network_prefix(cidr)
            prefix_len = len(binary_prefix)
            processed_table.append( (binary_prefix, prefix_len, link) )
        
        processed_table.sort(key=lambda item: item[1], reverse=True)
        self.forwarding_table = processed_table


    def route_packet(self, dest_ip: str) -> str:
        """
        Routes a single packet based on its destination IP
        using the longest prefix matching algorithm.
        """
        
        # 1. Convert the destination IP to its 32-bit binary representation 
        #    We use our helper function from Part 1
        binary_dest_ip = ip_to_binary(dest_ip)
        print(f"\nRouting packet to: {dest_ip} ({binary_dest_ip})")

        # --- We will add the loop here next ---
        
        # 2. If no match is found after the loop, return the default route 
        print("No specific match found. Using default route.")
        return "Default Gateway"