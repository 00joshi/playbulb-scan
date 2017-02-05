#!/usr/bin/env python3
from bluepy.btle import *
import struct
import argparse
parser = argparse.ArgumentParser(description='Scans a playbulb')
parser.add_argument('bmac', metavar='bmac',type=str,nargs=1, help='Bluetooth Mac')
args = vars(parser.parse_args())
blemac = args['bmac'][0]
MyPlaybulp = Peripheral(blemac)
services = MyPlaybulp.getServices()
for service in services:
	print (service)
	for characteristic in service.getCharacteristics():
		print(characteristic)
		print("    Handle: " + str(hex(characteristic.getHandle())))
		if characteristic.supportsRead() == True:
			value = ""
			try:
				value = characteristic.read()
			except:
				print("        BLE error")


			print("        " + str(value))
			print("        " + str(list('%2x'%b for b in value)))
MyPlaybulp.disconnect()
