
import bluetooth
import time
import datetime

blue_addr = "20:16:02:15:71:89"

port = 1 

sock2 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock2.connect((blue_addr, port))

data = ""

turnOnTv = "a" 
turnOffTv = "b" 

morning_time = "06 : 30 : 00.000000"
morning_time2 = "06 : 30 : 00.000300"

night_time = "23 : 30 : 00.000000"
night_time2 = "23 : 30 : 00.000300"

test_time = "15 : 31 : 00.000000"
test_time2 = "15 : 31 : 00.000300"


checking = 1

while True:
	try:
		this_time = datetime.datetime.now().strftime("%H : %M : %S.%f")

		if this_time >= morning_time and this_time < morning_time2:
			sock2.send(turnOnTv)
			print "The tv turned on " + this_time
			
		elif this_time >= night_time and this_time < night_time2: 
			sock2.send(turnOffTv)
			print "The tv turned off " + this_time 
		"""
		elif this_time >= test_time and this_time < test_time2: 
	#	elif test_time3 == time.strftime("%H / %M / %S"):
			sock2.send(turnOnTv)
			if checking == 1:
				sock2.send(turnOnTv)
				checking = 0
			elif checking == 0:
				sock2.send("finished")
			print "Tv turned on " + this_time 
	#		checking = 1
		"""

	except KeyboardInterrupt:
		break

sock2.close()
