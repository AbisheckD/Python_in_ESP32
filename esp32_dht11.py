import dht
from machine import Pin
import time

sensor = dht.DHT11(Pin(4))  # GPIO4 - DHT11 DATA pin

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature: {}°C  Humidity: {}%".format(temp, hum))
    except Exception as e:
        print("Error reading sensor:", e)
    time.sleep(2)
