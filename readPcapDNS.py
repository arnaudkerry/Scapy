import sys
import scapy.all as scapy

file = sys.argv[1]
for packet in scapy.PcapReader(file):
    if packet.haslayer(scapy.DNS):
        packet[scapy.DNS].show()