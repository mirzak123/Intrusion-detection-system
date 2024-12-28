import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

broker = "test.mosquitto.org"
port = 1883
topic = "intruder/detection"
client = mqtt.Client()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
	GPIO.output(TRIG, GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(TRIG, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(TRIG, GPIO.LOW)

	while GPIO.input(ECHO) == GPIO.LOW:
		pulse_start = time.time()

	while GPIO.input(ECHO) == GPIO.LOW:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance, 2)

	return distance

def on_connect(client, userdata, flags, rc):
	print(f"Connected to MQTT Broker with result code {rc}")

client.on_connect = on_connect
client.connect(broker, port, 60)
client.loop_start()

try:
	while True:
		distance = measure_distance()
		print(f"Distance is {distance}")

		if distance < 50:
			client.publish(topic, "Intruder detected!")
			print("Intruder detected. Message sent.")
			time.sleep(2)

		time.sleep(0.1)

except KeyboardInterrupt:
	print("Program terminated.")
	client.loop_stop
	GPIO.cleanup()
