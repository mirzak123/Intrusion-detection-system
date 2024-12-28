from paho.mqtt import publish

publish.single("IoTFundamentals/IntrusionDetectionSystem", "No intruder in proximity.", hostname = "test.mosquitto.org")
print("Done")
