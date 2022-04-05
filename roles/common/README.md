This is a common role that is applied to all servers. It contains everything that is common for all servers but too small to make their own role.

This includes but not limited to:
 - Installing the CA that is used to verify communication between VMs
 - Installing a motd
 - Installing my favourite debugging tools
 - Configuring hosts file, and other network stuff
 - Setting up a basic firewall
 - Configure ssh server

This role depends on the common ipam var
