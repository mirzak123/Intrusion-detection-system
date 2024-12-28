from paho.mqtt import publish

publish.single("IoTFundamentals/IntrusionDetectionSystem", "Intruder detected!", hostname = "test.mosquitto.org")
print("Done")
