# Import required Python libraries
import math
import os
import time

import RPi.GPIO as GPIO
from intruder_functions import *

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO = 24

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

try:
    while True:
        # Allow module to settle
        time.sleep(0.5)

        # Send 10us pulse to trigger
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
        start = time.time()

        while GPIO.input(GPIO_ECHO)==0:
            start = time.time()

        while GPIO.input(GPIO_ECHO)==1:
            stop = time.time()

        # Calculate pulse length
        elapsed = stop-start

        # Distance pulse travelled in that time is time
        # multiplied by the speed of sound (cm/s)
        distancet = elapsed * 34300

        # That was the distance there and back so halve the value
        distance = distancet / 2

        os.system("clear")
        print ("Ultrasonic Measurement")
        print  ("Distance :", distance, " cm")

        if distance < 50:
            is_intruder_detected = True
            intruder_detected(math.floor(distance))
        elif distance >= 50:
            is_intruder_detected = False
            intruder_left()

except KeyboardInterrupt:
    print("Program Terminated")
    GPIO.cleanup()
