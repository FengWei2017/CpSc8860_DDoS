#!/usr/bin/env python
"""
Check http://www.secdev.org/projects/scapy/doc/usage.html for more examples
"""
from uuid import getnode as get_mac
from scapy.all import *
import glob
import time
import random

def read_pcap(file):  # Read a pcap file and send all packets
    packets = rdpcap(file)
    sendp(packets)


def return_pkt(pkt):  # Simply swap the source and destination mac address and send the packet back
    p = eval(pkt.command())
    tmp = p.src
    p.src = p.dst
    p.dst = tmp
    sendp(p)


def sniff_return():  # Return any packets you received
    your_mac = get_mac()
    your_mac = ':'.join(("%012X" % get_mac())[i:i + 2] for i in range(0, 12, 2))  # This is your mac address
    sniff(iface='enp2s0', filter="ether src not " + your_mac, prn=return_pkt, store=0,
          count=10)  # Execute pkt_forward() when received a packet


def craft_send():  # Keep sending and receive a DNS query to 8.8.8.8 with a random interval
    for i in xrange(10):
        time.sleep(random.random() * 5)
        sr1(IP(dst="8.8.8.8") / UDP() / DNS(rd=1, qd=DNSQR(qname="www.google.com")))


def main():
    pcap_file = glob.glob('*.pcap')
    read_pcap(pcap_file[0])
    sniff_return()
    craft_send()


if __name__ == '__main__':
    main()
