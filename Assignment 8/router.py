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
        Initializes the router with a list of routes.
        'routes' is a list of tuples, e.g.:
        [("223.1.1.0/24", "Link 0"), ("223.1.2.0/24", "Link 1")]
        """
        print(f"Initializing router with {len(routes)} routes...")
        
        self.forwarding_table = [] 
        
        self._build_forwarding_table(routes)
        
        print("Router is ready.")
        print(f"Internal Forwarding Table: {self.forwarding_table}")

    def _build_forwarding_table(self, routes: list):
        """
        Processes the human-readable routes list into an internal,
        sorted, binary format for fast lookups.
        """
        
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
        pass