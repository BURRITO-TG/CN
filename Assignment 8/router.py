try:
    from ip_utils import ip_to_binary, get_network_prefix
except ImportError:
    print("Error: Could not find ip_utils.py.")
    print("Please make sure ip_utils.py is in the same directory.")
    exit()

class Router:
    """
    Implements a router with a forwarding table and the
    longest prefix matching algorithm.
    """
    
    def __init__(self, routes: list):
        """
        Initializes the router with a list of routes[cite: 30, 31].
        """
        print(f"Initializing router with {len(routes)} routes...")
        
        self.forwarding_table = [] 
        
        self._build_forwarding_table(routes)
        
        print("Router is ready.")
        print(f"Internal Forwarding Table (sorted): {self.forwarding_table}") 

    
    def _build_forwarding_table(self, routes: list):
        """
        Processes the human-readable routes list into an internal,
        sorted, binary format for fast lookups[cite: 36, 37].
        """
        processed_table = []
        for route_tuple in routes:
            cidr = route_tuple[0]
            link = route_tuple[1]
            
            binary_prefix = get_network_prefix(cidr)
            
            prefix_len = len(binary_prefix)
            
            processed_table.append( (binary_prefix, link) )
        
        processed_table.sort(key=lambda item: len(item[0]), reverse=True)
        
        self.forwarding_table = processed_table


    def route_packet(self, dest_ip: str) -> str:
        """
        Routes a single packet based on its destination IP
        using the longest prefix matching algorithm[cite: 40, 43].
        """
        
        binary_dest_ip = ip_to_binary(dest_ip)
        print(f"\nRouting packet to: {dest_ip} (Binary: {binary_dest_ip[:16]}...)")

        for entry in self.forwarding_table:
            binary_prefix = entry[0]
            output_link = entry[1]
            
            if binary_dest_ip.startswith(binary_prefix):
                print(f"  -> Match found: Prefix {binary_prefix} (len {len(binary_prefix)}) routes to {output_link}")
                return output_link
        
        print("  -> No specific match found. Using default route.")
        return "Default Gateway"

if __name__ == "__main__":
    
    print("\n\n--- Testing Part 2: Router ---")
    
    test_routes = [
        ("223.1.1.0/24", "Link 0"), 
        ("223.1.2.0/24", "Link 1"), 
        ("223.1.3.0/24", "Link 2"), 
        ("223.1.0.0/16", "Link 4 (ISP)")
    ]
    
    router = Router(test_routes)
    
    print("\n--- Running Test Cases ---")
    
    ip_to_route = "223.1.1.100"
    link = router.route_packet(ip_to_route)
    print(f"Result: {ip_to_route} -> {link} (Expected: Link 0)")
    assert link == "Link 0"

    ip_to_route = "223.1.2.5"
    link = router.route_packet(ip_to_route)
    print(f"Result: {ip_to_route} -> {link} (Expected: Link 1)")
    assert link == "Link 1"

    ip_to_route = "223.1.250.1"
    link = router.route_packet(ip_to_route)
    print(f"Result: {ip_to_route} -> {link} (Expected: Link 4 (ISP))")
    assert link == "Link 4 (ISP)"
    
    ip_to_route = "198.51.100.1"
    link = router.route_packet(ip_to_route)
    print(f"Result: {ip_to_route} -> {link} (Expected: Default Gateway)")
    assert link == "Default Gateway"
    
    print("\n--- All Router Tests Passed ---")