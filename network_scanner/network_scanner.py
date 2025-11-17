#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()
    arp_request_broadcast = broadcast/arp_request

    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()
    # print(arp_request.summary())
    # print(broadcast.summary())
    # scapy.ls(scapy.ARP())
    # scapy.ls(scapy.Ether())



scan("192.168.1.1")