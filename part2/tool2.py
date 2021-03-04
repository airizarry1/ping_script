#!/usr/bin/env python
# In this script you will leverage functions to ping a list of devices and return the result.
# A key component of using python is writing reusable code.
# Functions give you this ability.
import os


# Verifies your os type
OS_TYPE = os.name
# Sets the count modifier to the os type
count = '-n' if OS_TYPE == 'nt' else '-c'

def create_ip_list():
    """Creates an ip address list
        return: Return the ip_list
        rtype: list
    """
    ip_list = []
    with open("ip_file.txt", "r") as file:
        for line in file:
            ip_list.append(line.strip())
    return ip_list


def ping_device(ip_list):
    """Ping ip_list and return results
        return: None
        rtype: None
    """
    results_file = open("results.txt", "w")
    ip_addresses = create_ip_list()
    for ip in ip_addresses:
        response = os.popen(f"ping {ip} {count} 1").read()
        if "Received = 1" and "Approximate" in response:
            print(f"UP {ip} Ping Successful")
            results_file.write(f"UP {ip} Ping Successful" + "\n")
        else:
            print(f"Down {ip} Ping Unsuccessful")
            results_file.write(f"Down {ip} Ping Unsuccessful" + "\n")
    results_file.close()


if __name__ == "__main__":
    ping_device(create_ip_list())
