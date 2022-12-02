import sys
import scapy.all as scapy
import scapy.layers.http as http

file = sys.argv[1]
res = b''
for packet in scapy.PcapReader(file):
    if packet.haslayer(http.HTTPResponse):
        ipsource = packet[scapy.IP].src
        ipdest = packet[scapy.IP].dst
        res += bytes(packet.getlayer(http.HTTPResponse).payload)
        continue
open('data','wb').write(res)