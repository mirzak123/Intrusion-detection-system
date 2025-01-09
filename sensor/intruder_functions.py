from paho.mqtt import publish


def intruder_detected(distance):
    publish.single("IoTFundamentals/IntrusionDetectionSystem", distance,hostname = "test.mosquitto.org")
    print (distance)


def intruder_left():
    publish.single("IoTFundamentals/IntrusionDetectionSystem", "No intruder in proximity.", hostname = "test.mosquitto.org")
    print ("Intruder Left!")
