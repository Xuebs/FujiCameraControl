
#!/usr/bin/env python

import sys
import socket

PCAddr = '192.168.1.1'
PCPort24 = 24
PCPort25 = 25
masterPlcAddr = '192.168.1.2'
masterPlcPort = 1

#create instance of socket for UDP
sockMasterPlc24 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#bind listen instance to PLC
sockMasterPlc24.bind((PCAddr, PCPort24))

#create instance of socket for UDP
sockMasterPlc25 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#bind listen instance to PLC
sockMasterPlc25.bind((PCAddr, PCPort25))

while True:
	command = input("command: ")

	while (command == "read"):
		sourcePort = input("listen on which port?: ")

		if (sourcePort == '24'):
			data1, addr = sockMasterPlc24.recvfrom(8)
			print ("received message:", data1.decode('ascii'))
			break
		elif (sourcePort == '25'):
			data2, addr = sockMasterPlc25.recvfrom(1024)
			print ("received message:", data2.decode('ascii'))
			break
		else:
			break		

	while (command == "write"):
		destPort = input("what port?: ")
		PlcOut = input("send what? (max 8 bytes): ")
		messageOut = bytes(PlcOut, 'utf-8')

		if (destPort == '1'):
			sockMasterPlc24.sendto(messageOut, (masterPlcAddr,1))
		elif (destPort == '2'):
			sockMasterPlc25.sendto(messageOut, (masterPlcAddr,2))
		break

	while (command == "quit"):
		quit()
		


