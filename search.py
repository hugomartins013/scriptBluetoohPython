
import subprocess, bluetooth
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
=======
for addr, name in nearby_devices: 
    print " %s - %s" % (addr, name)

passkey = "1111" 
address = "5C:51:88:1A:17:46"
port = 0x1001

status = subprocess.call("bluetooth-agent " + passkey + " & ", shell = True)

print status
print passkey
print address

try:
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((address, port))
>>>>>>> Stashed changes

client_socket.close()
server_socket.close()
'''

s.recv(1024)
s.send("Hello World!")


server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "AquaPiServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )

while True:          
	print "Waiting for connection on RFCOMM channel %d" % port

	client_sock, client_info = server_sock.accept()
	print "Accepted connection from ", client_info



client_sock.close()
server_sock.close()

