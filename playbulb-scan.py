#!/usr/bin/env python3
from bluepy.btle import *
import struct
import argparse
MyPlaybulp = Peripheral("46:92:4B:15:AC:E6")
#parser = argparse.ArgumentParser(description='Sends color to the esp')
#parser.add_argument('red', metavar='R',type=int,nargs=1, help='red value in decimal')
#parser.add_argument('green', metavar='G',type=int,nargs=1, help='green value in decimal')
#parser.add_argument('blue', metavar='B',type=int,nargs=1, help='blue value in decimal')
#parser.add_argument('white', metavar='W',type=int,nargs=1, help='white value in decimal')
#args = vars(parser.parse_args())
services = MyPlaybulp.getServices()
for service in services:
	print (service)
	for characteristic in service.getCharacteristics():
		print(characteristic)
		print("Handle: " + str(hex(characteristic.getHandle())))
# There seems to be something broken there
		if characteristic.supportsRead() == True:
			try:
				print(characteristic.read())
				print(list('%2x'%b for b in characteristic.read()))
			except:
				print("BLE error")


#for bite in MyPlaybulp.readCharacteristic(25):
#	print (hex(bite))

# read current color
#print(struct.unpack("BBBB",MyPlaybulp.readCharacteristic(int(0x001b))))

#sendbites = (struct.pack("BBBB",args['white'][0],args['red'][0],args['green'][0],args['blue'][0]))
#MyPlaybulp.writeCharacteristic(int(0x001b),sendbites)

MyPlaybulp.disconnect()
#MyPlaybulp.writeCharacteristic(25,"00ff00ff03000101".encode())
