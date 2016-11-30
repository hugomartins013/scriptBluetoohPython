import subprocess, bluetooth

print "performing inquiry..."

nearby_devices = bluetooth.discover_devices(duration=4, lookup_names=True, flush_cache=True) 

print "found %d devices" % len(nearby_devices) 

for name, addr in nearby_devices: 
     print " %s - %s" % (addr, name)
 
passkey = "1111" 

subprocess.call("kill -9 `pidof bluetooth-agent`",shell = True)

status = subprocess.call("bluetooth-agent " + passkey + " & ", shell = True)
try:
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((addr, 1))

except bluetooth.btcommon.BluetoothError as err:
    pass

s.recv(1024)
s.send("Hello World!")