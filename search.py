
from bluetooth import *

print "performing inquiry..."

nearby_devices = discover_devices(lookup_names = True)

print "found %d devices" % len(nearby_devices)

for name, addr in nearby_devices:
     print " %s - %s" % (addr, name)

'''
server_socket=BluetoothSocket( RFCOMM )

server_socket.bind((addr, 3 ))
server_socket.listen(1)

client_socket, address = server_socket.accept()

data = client_socket.recv(1024)

client_socket.close()
server_socket.close()
'''

