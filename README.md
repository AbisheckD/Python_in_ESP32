# ESP32 LED Blinking Program (MicroPython)

## Overview

This is a basic MicroPython script to blink the onboard LED of the ESP32 board. It toggles the LED ON and OFF with a delay of 0.5 seconds, demonstrating GPIO control using the `machine` module.

## Features

- Blinks onboard LED connected to GPIO2  
- Uses MicroPython's built-in `machine` and `time` modules  
- Simple infinite loop with delay  

## Prerequisites

- ESP32 board (e.g., ESP32 Devkit V1)  
- MicroPython firmware installed on the ESP32  
- [Thonny IDE](https://thonny.org/) or any other serial REPL like uPyCraft or PuTTY  

## How to Flash MicroPython Firmware

1. Download the latest MicroPython `.bin` file for ESP32 from [https://micropython.org/download/esp32/](https://micropython.org/download/esp32/)
2. Install [esptool](https://github.com/espressif/esptool) using pip:
   ```bash
   pip install esptool
   ```
3. Erase the flash:
   ```bash
   esptool.py --port COMx erase_flash
   ```
4. Flash the firmware:
   ```bash
   esptool.py --chip esp32 --port COMx write_flash -z 0x1000 esp32-xxxxxx.bin
   ```

> Replace `COMx` with your actual port and `esp32-xxxxxx.bin` with the name of the MicroPython firmware file.

## How to Run the Code

1. Connect your ESP32 board via USB.
2. Open Thonny IDE or your preferred MicroPython editor.
3. Select the correct board and port from the settings.
4. Paste the following code into the editor.
5. Save it as `main.py` on the ESP32 device.
6. Run or reset the board to start blinking the LED.

## Code

```python
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led.value(not led.value())
    sleep(0.5)
```

## Expected Output

The onboard LED connected to GPIO2 of the ESP32 board will blink ON and OFF every 0.5 seconds.

---

## License

This project is open-source and available under the MIT License.

## Contributing

Feel free to fork this repository, suggest changes, or open issues for improvements!
