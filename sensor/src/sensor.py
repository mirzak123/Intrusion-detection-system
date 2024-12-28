from paho.mqtt import publish
from time import sleep

try:
	while True:
		signal = input("Intruder here: ")
		if signal == "1":
			publish.single("IoTFundamentals/IntrusionDetectionSystem", "Intruder detected!", hostname = "test.mosquitto.org")
			print("Intruder detected")
			sleep(2)
		else:
			publish.single("IoTFundamentals/IntrusionDetectionSystem", "No intruders detected.", hostname = "test.mosquitto.org")
except KeyboardInterrupt:
	print("Program terminated")
