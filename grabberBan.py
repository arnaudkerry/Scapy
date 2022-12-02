from telnetlib import IP
import scapy.all
import argparse


ip = IP(dst=dst, frag = 0)
SYN = TCP(sport=sport, dport=dport, flags='S',seq=1000)
SYNACK = sr1(ip/SYN)
ACK = TCP(sport=sport, dport=dport, flags='A',seq=SYNACK.ack, ack=SYNACK.seq + 1)
test=sr1(SYN,ACK)

test.show()

send(ip/TCP(sport=sport, dport=dport, flag='A', seq=test.ack,ack=test.seq+1))
FIN=ip/TCP(sport=sport, dport=dport, flags="FA",seq=test.ack, ack=test.seq + 1)
FINACK=sr1(FIN)
cur_seq = SYNACK.ack
cur_ack = SYNACK.seq + 1

#client                                 ->      destionation = serveur
#ipsource,portsource                            ipdes,portdes
#
#D'abord : 
#Le client envoie un SYN a la destination
#La destination renvoie un SYNACK
#--> à ce moment là on a la bannière
#Le client envoie un FIN
#La destination renvoie un FINACK
#Le client envoie un ACK
#
#