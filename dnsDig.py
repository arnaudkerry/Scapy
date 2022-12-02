import scapy.all as scapy
import argparse

def parse():
    parser = argparse.ArgumentParser(
        prog = "DigDns"
    )
    parser.add_argument('name')
    parser.add_argument('-s','--server')
    parser.add_argument('-t','--type')
    return parser

def dnsReq(name,server='8.8.8.8',type='A'):
    dns_req = scapy.IP(dst=server)/scapy.UDP(dport=53)/scapy.DNS(rd=1, qd=scapy.DNSQR(qname=name,qtype=type))
    answer = scapy.sr1(dns_req, verbose=0)
    #answer[scapy.DNS].an.show()
    for ans in range(0,answer[scapy.DNS].ancount):
        parseReqType(answer[scapy.DNS].an[ans])
        print()
        answer[scapy.DNS].an[ans].show()
        #print("IP : ",answer[scapy.DNS].an[ans].rdata)
        #print("Name : ",answer[scapy.DNS].an[ans].rrname.decode())
        #print("TTL : ",answer[scapy.DNS].an[ans].ttl)
        #print("TT : ",answer[scapy.DNS].an[ans].type)

def parseReqType(req):
    print(req.type)
    if req.type == 1:
        showA(req)
    if req.type == 28:
        showAAAA(req)
    if req.type == 16:
        showTXT(req)
    if req.type == 15:
        showMX(req)
    if req.type == 2:
        showNS(req)
    if req.type == 12:
        showPTR(req)
    if req.type == 252:
        showAXFR(req)


def showA(rec):
    print("Response A \
        \nName : %s \
        \nIPv4 Address : %s \
        \nTTL : %s \
    " % (rec.rrname.decode(),rec.rdata,rec.ttl))

def showAAAA(rec):
    print("Response AAAA \
        \nName : %s \
        \IPv6 Address : %s \
        \nTTL : %s \
    " % (rec.rrname.decode(),rec.rdata,rec.ttl))

def showTXT(rec):
    print("Response TXT \
        \nName : %s \
        \nTextRecord : %s \
        \nTTL : %s \
    " % (rec.rrname.decode(),rec.rdata,rec.ttl))

def showMX(rec):
    print("Response MX \
        \nName : %s \
        \nExchange : %s \
        \nTTL : %s \
        \nPriority : %s \
    " % (rec.rrname.decode(),rec.exchange,rec.ttl,rec.preference))

def showNS(rec):
    print("Response NS \
        \nName : %s \
        \nServer name : %s \
        \nTTL : %s \
    " % (rec.rrname.decode(),rec.rdata.decode(),rec.ttl))

def showAXFR(rec):
    pass

def showPTR(rec):
    print("Response PTR \
    \nName : %s \
    \nIPv4 Address : %s \
    \nTTL : %s \
" % (rec.rrname.decode(),rec.rdata,rec.ttl))

        

args = parse().parse_args()
dnsReq(args.name,args.server,args.type)