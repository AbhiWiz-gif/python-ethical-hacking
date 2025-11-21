#!/usr/bin/env python

import scapy.all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest = "target", help = "IP address range to do scan")
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify an IP range, use --help fo more")
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return(client_list)

def print_result(results_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()
    # print(arp_request.summary()) 
    # print(broadcast.summary())
    # scapy.ls(scapy.ARP())
    # scapy.ls(scapy.Ether())

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)