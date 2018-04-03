#!/usr/bin/python

import subprocess
import ssl
import time
import paho.mqtt.client as mqtt
import json
import threading
from sense_hat import SenseHat

disp_type = 0
temperature = "0"
humidity = "0"

sense = SenseHat()
sense.set_rotation(180)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

#
def on_disconnect(client, userdata, rc):
    print("Disconnected with result code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	global temperature
	global humidity

	#print(msg.topic+" "+str(msg.payload))#debug
	data = json.loads(msg.payload)
	#print(data) #debug

	if msg.topic == 'iot/temperature':
		temperature = data['temperature']
	elif msg.topic == 'iot/humidity':
		humidity = data['humidity']

def on_log(client, userdata, level, buf):
	print("Debug %d: %s"%(level, buf))

def display_info():
	while True:
		if disp_type == 0:
			sense.show_message("T:"+temperature, text_colour=[255, 0, 0])
		elif disp_type == 1:
			sense.show_message("H:"+humidity, text_colour=[0, 0, 255])
		else:
			sense.clear()
			time.sleep(1)

def main():
	global disp_type
	global temperature
	global humidity

	disp_thread = threading.Thread(target=display_info)
	disp_thread.daemon = True
	disp_thread.start()

	client = mqtt.Client("pi_john_sub")

	client.tls_set( "CARoot.pem",
					"66321288b3-certificate.pem.crt",
					"66321288b3-private.pem.key",
					cert_reqs=ssl.CERT_NONE,
					tls_version=ssl.PROTOCOL_TLSv1_2)

	client.on_connect = on_connect
	client.on_disconnect = on_disconnect
	client.on_message = on_message
	#client.on_log = on_log #debug

	client.connect("a1zd8y5etgd1ze.iot.ap-northeast-1.amazonaws.com", 8883, 60)

	client.subscribe("iot/temperature")
	client.subscribe("iot/humidity")

	running = True

	while running:
		client.loop()

		for event in sense.stick.get_events():
			if ((event.direction == 'up') or (event.direction == 'down')) and (event.action == 'released'):
				running = False
			elif ((event.direction == 'left') or (event.direction == 'right')) and (event.action == 'released'):
				disp_type = disp_type + 1
				if (disp_type > 2):
					disp_type = 0

	client.disconnect()
	sense.clear()

if __name__ == '__main__':
	main()






