
from bluetooth import *

print "performing inquiry..."

nearby_devices = discover_devices(lookup_names = True) # Procura todos dispositivos próximos

print "found %d devices" % len(nearby_devices) # Informa quantos dispositivos foram encontrados

for name, addr in nearby_devices: # Informa os dispositivos encontrados
     print " %s - %s" % (addr, name)

    name = name      # Nome do dispositivo
    addr = addr      # Endereço do dispositivo
    port = bluetooth.get_available_port (bluetooth.RFCOMM) #  Porta RFCOMM (.get_available_port pega a primeira disponível)
    passkey = "1111" # passkey of the device you want to connect

    # Interrompe outros processos de conexões bluetooth em execução
    subprocess.call("kill -9 `pidof bluetooth-agent`",shell=True)

    # Nova conexão bluetooth
    status = subprocess.call("bluetooth-agent " + passkey + " &",shell=True)
    try:
        s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        s.connect((addr[0,port[0]))
    except bluetooth.btcommon.BluetoothError as err:
        pass

s.recv(1024)
s.send("Hello World!")

