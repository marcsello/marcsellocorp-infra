This role installs keepalived and sets up a simple IPv4/IPv6 Floating IP using unicast vrrp. 

Since VMs at Marcsello Corp. ususally have only one interface, this role can configure a single floating ip of each version

Don't forget to allow vrrp on your firewall
This role depends on the ipam variable
