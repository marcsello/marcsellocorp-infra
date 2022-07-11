This role installs bind9 and generates zone files according to the ipam dict
It is also capable of forwarding queries

The reverse zone generation is a bit clunky and only works for subnets with a netmask of 8, 16 or 24 bit in ipv4 and prefixes divisable by 8 in ipv6
