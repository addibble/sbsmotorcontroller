#!/usr/bin/env python
import sys
import struct

with open(sys.argv[1], 'rb') as fp:
    data = fp.read()

def dump_gpio(data, prefix):
    crl, crh, idr, odr, bssr, brr, lckr = struct.unpack('<IIIIIII', data[0:4*7])
    types = {
        0b0000: 'IN analog',
        0b0100: 'IN floating',
        0b1000: 'IN pull',
        0b1100: 'IN invalid',
        0b0001: 'OUT push-pull 10mhz',
        0b0010: 'OUT push-pull 2mhz',
        0b0011: 'OUT push-pull 50mhz',
        0b0101: 'OUT open-drain 10mhz',
        0b0110: 'OUT open-drain 2mhz',
        0b0111: 'OUT open-drain 50mhz',
        0b1001: 'OUT alt push-pull',
        0b1010: 'OUT alt push-pull',
        0b1011: 'OUT alt push-pull',
        0b1101: 'OUT alt open-drain',
        0b1110: 'OUT alt open-drain',
        0b1111: 'OUT alt open-drain'
    }
    for pin in range(0, 16):
        if pin < 8:
            cnfmode = (crl >> (pin * 4)) & 0xf
        else:
            cnfmode = (crh >> ((pin-8) * 4)) & 0xf
        i = (idr >> pin) & 1
        o = (odr >> pin) & 1
        desc = types[cnfmode]
        if cnfmode == 0b1000:
            if i:
                desc = 'IN pull-up'
            else:
                desc = 'IN pull-down' 
        val = '-'
        if desc.startswith('IN pull'):
            val = 'HIGH' if i else 'LOW'
        elif desc.startswith('OUT push') or desc.startswith('OUT open'):
            val = 'HIGH' if o else 'LOW'
        print '%s%-2d %-20s %s' % (prefix, pin, desc, val)

dump_gpio(data[0x0800:], 'PA')
dump_gpio(data[0x0C00:], 'PB')
dump_gpio(data[0x1000:], 'PC')
#dump_gpio(data[0x1400:], 'PD')
#dump_gpio(data[0x1800:], 'PE')
#dump_gpio(data[0x1C00:], 'PF')
#dump_gpio(data[0x2000:], 'PG')



