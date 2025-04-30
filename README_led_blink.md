# ESP32 LED Blinking using MicroPython

## Overview

This project demonstrates how to blink the onboard LED (connected to GPIO2) on an ESP32 board using MicroPython. It's a simple and effective way to get started with embedded development using Python.

## GitHub Repository

- [GitHub Repository](https://github.com/AbisheckD/Python_in_ESP32/tree/main)

## Prerequisites

- ESP32 Development Board
- MicroPython firmware for ESP32 ([Download here](https://micropython.org/download/ESP32_GENERIC/))
- USB to UART driver ([CP210x VCP](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers))
- [Thonny IDE](https://thonny.org/)
- Python installed on your computer

## Flashing MicroPython to ESP32 (Command Prompt Steps)

1. **Install esptool**  
   Open a terminal or command prompt and run:
   ```bash
   pip install esptool
   ```

2. **Erase the flash**  
   Replace `COMx` with your ESP32's actual COM port:
   ```bash
   python -m esptool --port COMx erase_flash
   ```

3. **Write the MicroPython firmware**  
   Replace the path with the correct `.bin` file location:
   ```bash
   python -m esptool --chip esp32 --port COM3 --baud 460800 write_flash -z 0x1000 "D:\Desktop_tools\micropython\esp_micropy\ESP32_GENERIC-20250415-v1.25.0.bin"
   ```
## How to Run the Code on ESP32 Using Thonny

1. Connect the ESP32 board to your computer via USB.
2. Open [Thonny IDE](https://thonny.org).
3. Set the interpreter to **MicroPython (ESP32)** via `Tools` → `Options` → `Interpreter`.
4. Choose the correct port (e.g., COMx or /dev/ttyUSBx).
5. Copy and paste the following code into Thonny.
6. Save the script as `main.py` to the device.
7. Click **Run** or press `Ctrl+R`.
## LED Blink Code

```python
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led.value(not led.value())
    sleep(0.5)
```

## Output

The onboard LED will blink every 0.5 seconds, toggling its state continuously.

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
