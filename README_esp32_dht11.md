# ESP32 with DHT11 Sensor using MicroPython

## Overview

This project demonstrates how to read temperature and humidity values from a DHT11 sensor connected to an ESP32 board using MicroPython. The readings are printed on the serial console via Thonny IDE.

## GitHub Repository

- [GitHub Repository](https://github.com/AbisheckD/Python_in_ESP32/tree/main)

## Prerequisites

- ESP32 Development Board  
- DHT11 Temperature and Humidity Sensor  
- MicroPython firmware for ESP32 ([Download here](https://micropython.org/download/ESP32_GENERIC/))  
- USB to UART driver ([CP210x VCP](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers))  
- [Thonny IDE](https://thonny.org/)  
- Python installed on your computer  

## Flashing MicroPython to ESP32 (Command Prompt Steps)

1. **Install esptool**  
   ```bash
   pip install esptool
   ```

2. **Erase the flash**  
   Replace `COM3` with your ESP32's actual COM port:  
   ```bash
   python -m esptool --port COM3 erase_flash
   ```

3. **Write the MicroPython firmware**  
   Replace the path with the actual location of your `.bin` file:  
   ```bash
   python -m esptool --chip esp32 --port COM3 --baud 460800 write_flash -z 0x1000 "D:\Desktop_tools\micropython\esp_micropy\ESP32_GENERIC-20250415-v1.25.0.bin"
   ```

## Setting Up Thonny IDE

1. Open [Thonny](https://thonny.org/).  
2. Go to `Tools > Options > Interpreter`.  
3. Select **MicroPython (ESP32)** and choose the correct COM port.  
4. Click **OK** to save.

## DHT11 Code (MicroPython)

```python
from machine import Pin
import dht
from time import sleep

sensor = dht.DHT11(Pin(4))  # Connect DHT11 data pin to GPIO4

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature:", temp, "°C")
        print("Humidity:", hum, "%")
    except OSError as e:
        print("Sensor error:", e)
    sleep(2)
```

## Output

The terminal in Thonny will display the following:
```
Temperature: 26 °C
Humidity: 55 %
```

## Helpful Resources

- 🧑‍🏫 [Getting Started Tutorial (Thonny + ESP32)](https://techtotinker.com/2020/09/05/000-esp32-micropython-how-to-get-started-with-micropython/)
- 📥 [MicroPython Firmware for ESP32](https://micropython.org/download/ESP32_GENERIC/)
- 🔌 [CP210x USB Driver](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers)

## License

MIT License

## Clone the Repo

```bash
git clone https://github.com/AbisheckD/Python_in_ESP32.git
```
