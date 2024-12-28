import time

import gpiozero as GPIO

# Pin configuration
LED_PIN = 18  # Choose a GPIO pin to connect the LED (e.g., GPIO 18)

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)  # Use BCM numbering (GPIO numbers)
GPIO.setup(LED_PIN, GPIO.OUT)  # Set the LED pin as an output

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn the LED on
        print("LED ON")
        time.sleep(1)  # Keep it on for 1 second

        GPIO.output(LED_PIN, GPIO.LOW)  # Turn the LED off
        print("LED OFF")
        time.sleep(1)  # Keep it off for 1 second

except KeyboardInterrupt:
    print("\nExiting program.")

finally:
    GPIO.cleanup()  # Clean up GPIO settings
    print("GPIO cleaned up.")
