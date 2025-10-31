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
        pass

    def route_packet(self, dest_ip: str) -> str:
        pass