import subprocess, bluetooth
from bluetooth import *
from socket import *

print "performing inquiry..."

nearby_devices = bluetooth.discover_devices(duration=4, lookup_names=True, flush_cache=True) 

print "found %d devices" % len(nearby_devices) 

for addr, name in nearby_devices: 

    print " %s - %s" % (addr, name)

passkey = "1111"
address = "9C:35:EB:A2:5D:50"
port = 0x1001

try:
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((address, port))

except bluetooth.btcommon.BluetoothError as err:
    pass
    
s = socket(AF_INET, SOCK_STREAM)
s.send("Hello World")

print "teste okay"
