#!/usr/bin/python

import sys

gmap={"0x40010800:": "a", "0x40010c00:": "b", "0x40011000:": "c", "0x40011400:": "d"}

def mode(cr, odr, idr):
    desc=""
    mode=cr & 0x11
    if(mode == 0):
        desc="input value " + str(idr)
    elif(mode == 0b01):
        desc="output 10mhz value " + str(odr)
    elif(mode == 0b10):
        desc="output 2mhz value " + str(odr)
    elif(mode == 0b11):
        desc="output 50mhz value " + str(odr)
    cnf=cr >> 2
    if(mode == 0):
        if(cnf == 0):
            desc += " analog"
        elif(cnf == 1):
            desc += " floating"
        elif(cnf == 0b10):
            if odr == 0:
                desc += " pull-down"
            else:
                desc += " pull-up"
    else:
        if(cnf & 0b10 == 0b10):
            desc += " alternate-function "
        if(cnf & 0x1 == 0):
            desc += "push-pull"
        elif(cnf & 0x1 == 1):
            desc += "open-drain"
    return desc

for l in sys.stdin.readlines():
    try:
        (g, crl, crh, idr, odr)=l.split()[0:5]
        reg=int(crl, 16)
        odr=int(odr, 16)
        idr=int(idr, 16)
        g=gmap[g]
        for i in range(0,16):
            if(i == 8):
                reg=int(crh, 16)
            print "%s%d %s" % (g, i, mode(reg & 0b1111, odr & 1, idr & 1))
            reg=reg >> 4
            odr >> 1
            idr >> 1
    except:
        continue

