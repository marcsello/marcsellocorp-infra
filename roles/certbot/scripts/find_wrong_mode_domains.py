#!/usr/bin/env python3
import configparser
import os
import os.path
import sys

def main():
    desired_mode = sys.argv[1]
    liveroot = '/etc/letsencrypt/live'
    renewalconfigroot = "/etc/letsencrypt/renewal"
    domains = filter(lambda x: os.path.isdir(os.path.join(liveroot, x)), os.listdir(liveroot))

    for domain in domains:
        config = configparser.ConfigParser()

        with open(os.path.join(renewalconfigroot, f"{domain}.conf"), 'rt') as f:
            config_string = '[DEFAULT]\n' + f.read()
        config.read_string(config_string)

        mode = config.get("renewalparams", "authenticator")
        if mode != desired_mode:
            print(domain)

if __name__ == '__main__':
    main()
