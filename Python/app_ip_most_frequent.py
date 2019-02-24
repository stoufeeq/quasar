#An array of sentences containing an IP Address as a word in between. Print the most frequently occurring IP addresses(Duplicates also).

import numpy as np
import re

my_arr = np.array(["my IP address is 192.168.1.2",
                  "my neighbors IP 10.10.43.4 is different",
                  "IP 123.43.1.43 is the DHCP address",
                  "abc 192.168.1.2 dec",
                  "xyz 192.168.1.2 fgh",
                  "aaa 10.10.43.4 bbb",
                  "sssss dddd 1.1.1.2 ddfsfs"])


def get_ip(input_arr):
    ip = []
    for i in my_arr:
        ip.extend(re.findall( r'[0-9]+(?:\.[0-9]+){3}', i ))
    return ip


def get_most_frequent_ip(ip):
    count = 1
    for i in ip:
        if ip.count(i) > 1 and ip.count(i) >= count:
            count = ip.count(i)
            result = (i, ip.count(i))
    return result


def main():
    print(get_most_frequent_ip(get_ip(my_arr)))

    
if __name__ == "__main__":
    main()

