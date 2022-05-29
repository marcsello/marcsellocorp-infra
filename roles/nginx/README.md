This role installs NGINX and sets up vhosts and upstreams

Vhosts can serve static folders or can proxy stuff, that's everything. If you need something else, set type to custom and write the body of the location definition to the custom variable

Since SSL is meant to be terminated by HAProxy, and it's only needed in a cluster setup where vms communicate eachother, only a single cert can be configured for all vhosts. This cert should be accepted by HAProxy.

It is recommended to get these certs by the internal_cert role
