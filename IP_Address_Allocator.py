import ipaddress

class IPAddressAllocator:
    def __init__(self, start_ip, end_ip):
        self.current_ip = ipaddress.IPv4Address(start_ip)
        self.end_ip = ipaddress.IPv4Address(end_ip)
        self.allocated_ips = set()

    def get_next_ip(self):
        while self.current_ip <= self.end_ip:
            if self.current_ip not in self.allocated_ips:
                self.allocated_ips.add(self.current_ip)
                next_ip = self.current_ip
                self.current_ip += 1
                return str(next_ip)
            self.current_ip += 1
        return None  # no IPs availables

# usage:
allocator = IPAddressAllocator("192.168.1.1", "192.168.1.10")
print(allocator.get_next_ip())  # output: "192.168.1.1"
print(allocator.get_next_ip())  # output: "192.168.1.2"
