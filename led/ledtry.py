from gpiozero import LED
from time import sleep

led = LED(12)
while True:
	led.on()
	print("LED is on")
	sleep(1)

	led.off()
	print("LED is OFF")
	sleep(1)

