
# ESP32 DHT11 Temperature and Humidity Monitor (MicroPython)

## Overview

This MicroPython script reads temperature and humidity values from a DHT11 sensor connected to an ESP32. The values are printed every 2 seconds. GPIO4 is used as the data pin.

## Features

- Reads data from a DHT11 sensor
- Displays temperature in °C and humidity in %
- Error handling included for sensor reading failures

## GitHub Repository

- GitHub Repo: [Python_in_ESP32](https://github.com/AbisheckD/Python_in_ESP32/tree/main)

## Prerequisites

- ESP32 Devkit board  
- DHT11 sensor module  
- MicroPython firmware installed  
- USB to UART driver installed ([CP210x Driver](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers))  
- [Thonny IDE](https://thonny.org/)  

## Wiring

- DHT11 VCC → 3.3V on ESP32  
- DHT11 GND → GND on ESP32  
- DHT11 DATA → GPIO4 on ESP32  

## Resources

- 📘 **MicroPython Firmware for ESP32:** [Download here](https://micropython.org/download/ESP32_GENERIC/)  
- 🧑‍🏫 **Getting Started with MicroPython on ESP32 (Thonny):** [techtotinker.com tutorial](https://techtotinker.com/2020/09/05/000-esp32-micropython-how-to-get-started-with-micropython/)  
- 💻 **Thonny IDE Website:** [https://thonny.org](https://thonny.org)  
- 🔌 **Driver for USB-to-Serial (ESP32):** [Silicon Labs VCP Driver](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers)

## How to Run

1. Flash MicroPython firmware to the ESP32 if not done already.
2. Open [Thonny IDE](https://thonny.org).
3. Set the interpreter to **MicroPython (ESP32)** via `Tools` → `Options` → `Interpreter`.
4. Connect the DHT11 sensor to GPIO4.
5. Paste the following code in Thonny and save it as `main.py` on the device.

## Code

```python
import dht
from machine import Pin
import time

sensor = dht.DHT11(Pin(4))  # GPIO4 is connected to DHT11 DATA pin

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature: {}°C  Humidity: {}%".format(temp, hum))
    except Exception as e:
        print("Error reading sensor:", e)
    time.sleep(2)
```

## Sample Output

```
Temperature: 27°C  Humidity: 55%
Temperature: 27°C  Humidity: 56%
...
```

## License

This project is open-source and available under the MIT License.

## Contributing

Feel free to fork this repository, contribute with pull requests, or report issues.

```bash
git clone https://github.com/AbisheckD/Python_in_ESP32.git
```
