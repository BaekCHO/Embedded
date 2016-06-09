
import bluetooth
import threading
import time


blue_addr = "20:16:02:15:03:84"

port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((blue_addr, port))

data = ""

turnOnHumi = 1
turnOffHumi = 0

while 1:
	try:
		data += sock.recv(4096)
		data_end = data.find('\n')
		if data_end != -1:
			rec = data[:data_end]
			print data
			data = data[data_end + 1:]

		if data >= "37.00":
			sock.send(str(turnOffHumi))
		elif data < "25.00":
			sock.send(str(turnOnHumi))


sock.close()

