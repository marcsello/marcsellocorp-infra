This role installs NGINX and sets up vhosts and upstreams

Vhosts can serve static folders or can proxy stuff, that's everything. If you need something else, set type to custom and write the body of the location definition to the custom variable

ssl is solved by haproxy running locally, so it's not implemented here
