import Adafruit_BMP.BMP085 as BMP180
import time
import picamera
import os
import gps
import threading
import MySQLdb
import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('skidrow2002', 'jam6pbd0v4')

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

sensor = BMP180.BMP085()
temp = 0
pressure = 0
altitude = 0

idx = 0
a = []
b = []

def create_Graph():
	global a, b
	print 'X = ', a, 'Y = ', b
	data = [go.Scatter(x=a,y=b)]

	plot_url = py.plot(data, filename='date-axes2')

def db_Insert(temp, pressure, altitude, current):
	db = MySQLdb.connect("localhost", "root", "login010", "deu")
	cur = db.cursor()
	sql = """insert into weather values(%s, %s, %s, %s)"""
	cur.execute(sql, (temp, pressure, altitude, current))
	db.commit()
	db.close()

def db_Select():
	global a, b
	db = MySQLdb.connect("localhost", "root", "login010", "deu")
	cur = db.cursor()
	sql = "select * from weather"
	cur.execute(sql)
	while True:
		weather = cur.fetchone()
		if not weather: break
		#weather[0] : Temp, weather[1] : Perssure, weather[2] : High, weather[3] : time
		a.append(weather[3])
		b.append(weather[0])
	cur.close()
	db.close()

def measure_Temp():
	global temp, pressure, altitude
	temp = int(sensor.read_temperature())
	pressure = int(sensor.read_pressure())
	altitude = int(sensor.read_altitude())
	#print'Temp : '+str(temp)+ ' *C'
	#print'Pressure : ' + str(pressure) + ' Pa'
	#print'Altitude : '+str(altitude) + ' m'

def mix_Db_Measure():
	global temp, pressure, altitude
	while True:
		measure_Temp()
		#current = str(time.ctime())
		db_Insert(temp, pressure, altitude, str(time.ctime()))
		time.sleep(180) # testing time 3

def save_Video():
	global idx
	with picamera.PiCamera() as picam:
		while True:
			picam.rotation = 180
			picam.start_recording('earth_'+ str(idx) + '.h264')
			picam.wait_recording(1800) #30min
			picam.stop_recording()
			idx += 1

def find_Gps():
	global session
	while True:
		try:
			report = session.next()
			if report['class'] == 'TPV':
				os.system('clear')
				print ' GPS Data'
				print '==============================================='
				print 'latitude	', getattr(report, 'lat',0.0)
				print 'longitude ', getattr(report, 'lon', '')
				print 'time utc ', getattr(report, 'time', 'nan')
				print 'altitude ', getattr(report, 'alt', 'nan')
				print 'epv ', getattr(report, 'epv', 'nan')
				print 'ept ', getattr(report, 'ept', 'nan')
				print 'speed ', getattr(report, 'speed', 'nan')
				print 'climg ', getattr(report, 'climb', 'nan')
				print '==============================================='
				time.sleep(1)

		except KeyError:
			pass
		except KeyboardInterrupt:
			quit()
		except StopIteration:
			session = None

try :
	th = threading.Thread(target = mix_Db_Measure)
	th.start()

	th = threading.Thread(target = find_Gps)
	th.start()

except Exception:
	System.out.printl("Error");
finally:
	db_Select()
	create_Graph()
