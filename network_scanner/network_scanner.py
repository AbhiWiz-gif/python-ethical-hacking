#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast/arp_request
    answered_list,unanswered_list = scapy.srp(arp_request_broadcast, timeout=1)
    print(answered_list.summary())

    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()
    # print(arp_request.summary())
    # print(broadcast.summary())
    # scapy.ls(scapy.ARP())
    # scapy.ls(scapy.Ether())



scan("192.168.1.1/24")