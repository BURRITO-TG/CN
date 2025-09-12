import dns.resolver

def dns_client():
    domain = 'google.com'
    record_types = ['A', 'MX', 'CNAME']
    log_file = "dns_queries.log"

    print(f"--- Performing DNS queries for {domain} ---")
    
    with open(log_file, "w") as log:
        log.write(f"DNS Query Results for {domain}\n")
        log.write("="*30 + "\n")
        
        for record_type in record_types:
            try:
                print(f"\nQuerying for {record_type} records...")
                log.write(f"\n--- {record_type} Records ---\n")
                
                answers = dns.resolver.resolve(domain, record_type)
                
                for rdata in answers:
                    print(f"  - {rdata.to_text()}")
                    log.write(f"{rdata.to_text()}\n")
            
            except dns.resolver.NoAnswer:
                print(f"  No {record_type} records found.")
                log.write("No records found.\n")
            except dns.resolver.NXDOMAIN:
                print(f"  The domain '{domain}' does not exist.")
                log.write("Domain does not exist.\n")
                break # No need to check other records if domain doesn't exist
            except Exception as e:
                print(f"  Could not resolve {record_type}: {e}")
                log.write(f"Could not resolve: {e}\n")

    print(f"\n--- All query results logged to '{log_file}' ---")

if __name__ == "__main__":
    dns_client()