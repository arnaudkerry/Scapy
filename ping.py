import sys
import scapy.all as scapy

ip = sys.argv[1]
count = sys.argv[2]
for i in range(int(count)):
    a = scapy.IP(dst=ip)
    b = scapy.ICMP(id=1, seq = i)
    r = scapy.sr1(a/b/'toto'.encode('utf-16'))
    for i in r:
        i.show()