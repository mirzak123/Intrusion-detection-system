import time

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
from gpiozero import PWMLED

# MQTT Setup
BROKER = "test.mosquitto.org"  # Use the same broker as the sensor Raspberry Pi
PORT = 1883
TOPIC = "IoTFundamentals/IntrusionDetectionSystem"
LED_PIN = 18

# Setup GPIO for LED
led = PWMLED(LED_PIN)

client = mqtt.Client()
led.value = 0

blink_led = False
blink_speed = 0
led_brightness = 1

def blink_controller():
    print(blink_speed)
    if blink_led:
        led.value = 1
        time.sleep(blink_speed)
        led.value = 0
        time.sleep(blink_speed)
	

# Callback when connected to MQTT broker
def on_connect(client, _userdata, _flags, rc):
	print(f"Connected to MQTT Broker with result code {rc}")
	client.subscribe(TOPIC)  # Subscribe to the intruder detection topic

# Callback when a message is received
def on_message(_client, _userdata, message):
	global blink_led, blink_speed, led
	msg = message.payload.decode()
	print(f"Message received: {msg}")
	if msg == "No intruder in proximity.":
		blink_led = False
		led.value = 0
	else:
		blink_led = True
		blink_speed = int(msg) * 0.02


# Configure MQTT client
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_start()

# Main loop
try:
	while True:
		# Keep the program running to listen for messages
		blink_controller()

except KeyboardInterrupt:
	print("Program terminated.")
	client.loop_stop()
	GPIO.cleanup()
