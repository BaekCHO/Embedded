import cv2, cv
import socket
import threading
import time
import TotalFunc

sendImg = ""

def getPhoto():
	global sendImg

	cam = cv2.VideoCapture(0)
	cam.set(cv.CV_CAP_PROP_FRAME_WIDTH, 320)
	cam.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 240)

	while True:
		ret, img = cam.read()
		sendImg = cv2.imencode(".jpeg", img)[1].tostring()
		key = cv2.waitKey(10)

def sendPhoto():
	global sendImg

	port = 8000

	while True:
		s = socket.socket()
		s.connect(("113.198.235.230", port))
#	print "Sending..."
		s.send(sendImg)
		s.send(str(TotalFunc.temp))
		s.send(str(TotalFunc.high))
		s.send(str(TotalFunc.altitude))
#		print "Sending is finished"

		sendImg = ""

		s.close()


if __name__ == "__main__":

	#try:
	th = threading.Thread(target = getPhoto)
	th.start()

	th2 = threading.Thread(target = sendPhoto)
	th2.start()

	th3 = threading.Thread(target = TotalFunc.save_Video)
	th3.start()

	th4 = threading.Thread(target = TotalFunc.mix_Db_Measure)
	th4.start()

	th5 = threading.Thread(target = TotalFunc.find_Gps)
	th5.start()

	#finally
	#TotalFunc.db_Select()
	#create_Graph()
