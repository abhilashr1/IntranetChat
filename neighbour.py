# Layer 2 network neighbourhood discovery tool
# written by Benedikt Waldvogel (mail at bwaldvogel.de)

import scapy.config
import scapy.layers.l2
import scapy.route
import socket
import math
import errno



def netmask_finder(arg):
    #Finds the netmask of the network
    if (arg <= 0 or arg >= 0xFFFFFFFF):
        raise ValueError("illegal netmask value", hex(arg))
    mask = 32 - int(round(math.log(0xFFFFFFFF - arg, 2)))
    return mask

def CIDR_convert(bytes_network, bytes_netmask):
    #Endian Corrections
    network = scapy.utils.ltoa(bytes_network)

    netmask = netmask_finder(bytes_netmask)

    net = "%s/%s" % (network, netmask)
    if netmask < 16:
        print("%s is too big. skipping" % net)
        return None
    return net


def scanner(net, interface, timeout=1):
    print("arping %s on %s" % (net, interface))
    addr = []
    try:
        ans, unans = scapy.layers.l2.arping(net, iface=interface, timeout=timeout, verbose=False)
        for s, r in ans.res:
            mac = r.sprintf("%Ether.src%")
            ipadd = r.sprintf("%ARP.psrc%")
            addr.append((mac,ipadd))
    except socket.error as e:
        if e.errno == errno.EPERM:     # Operation not permitted
            print("%s. Did you run as root?", e.strerror)
        else:
            raise
    return addr


def neighbours():

    for network, netmask, _, interface, address in scapy.config.conf.route.routes:

        # skip loopback network and default gw
        if network == 0 or interface == 'lo' or address == '127.0.0.1' or address == '0.0.0.0' or netmask <= 0 or netmask == 0xFFFFFFFF or interface != scapy.config.conf.iface:
            continue

        net = CIDR_convert(network, netmask)
        addr=[]
        if net:
            addr=scanner(net, interface)
            return addr            

if __name__=='__main__':
    neighbours()