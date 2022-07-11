from ipaddress import ip_network, ip_address
import math

class FilterModule(object):
    """
    Some helper filters for the internal dns role
    """

    def filters(self):
        return {
            'cannonical_zone_name': self.cannonical_zone_name,
            'reverse_zone_name': self.reverse_zone_name,
            'short_reverse_pointer': self.short_reverse_pointer
        }

    def cannonical_zone_name(self, arg):
        return arg.strip('.') + '.'

    def reverse_zone_name(self, arg):

        network = ip_network(arg)
        
        if network.version == 4:
            del_elements = math.ceil((32-network.prefixlen)/8)
        else:
            del_elements = math.ceil((128-network.prefixlen)/8)

        return '.'.join(network.network_address.reverse_pointer.split('.')[del_elements:]) + '.'

    def short_reverse_pointer(self, arg, network):
        addr = ip_address(arg)
        verstr = {
            4 : "ip",
            6 : "ip6"
        }[addr.version]
        network = ip_network(network[verstr]['subnet'])
        
        if network.version == 4:
            keep_elements = math.ceil((32-network.prefixlen)/8)
        else:
            keep_elements = math.ceil((128-network.prefixlen)/8)

        return '.'.join(addr.reverse_pointer.split('.')[:keep_elements])
