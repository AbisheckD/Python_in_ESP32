# ESP32 LED Blinking Program (MicroPython)

## Overview

This is a basic MicroPython script to blink the onboard LED of the ESP32 board. It toggles the LED ON and OFF every 0.5 seconds using GPIO2, demonstrating MicroPython's control of hardware components.

## Features

- Blinks the onboard LED connected to GPIO2  
- Utilizes MicroPython's `machine` and `time` modules  
- Simple infinite loop for continuous blinking  

## GitHub Repository

- GitHub Repo: [Python_in_ESP32](https://github.com/AbisheckD/Python_in_ESP32/tree/main)

## Prerequisites

- ESP32 Devkit board  
- MicroPython firmware installed  
- USB to UART driver installed ([Silicon Labs CP210x Driver](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers))  
- [Thonny IDE](https://thonny.org/) installed  

## Resources

- 📘 **MicroPython Firmware for ESP32:** [Download here](https://micropython.org/download/ESP32_GENERIC/)  
- 🧑‍🏫 **Tutorial on Getting Started with MicroPython on ESP32 (Thonny):** [techtotinker.com tutorial](https://techtotinker.com/2020/09/05/000-esp32-micropython-how-to-get-started-with-micropython/)  
- 💻 **Thonny IDE Website:** [https://thonny.org](https://thonny.org)  
- 🔌 **Driver for USB-to-Serial (ESP32):** [Silicon Labs VCP Driver](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers)

## How to Flash MicroPython Firmware

1. Download the `.bin` firmware from [here](https://micropython.org/download/ESP32_GENERIC/).
2. Install esptool:
   ```bash
   pip install esptool
   ```
3. Erase the flash memory:
   ```bash
   esptool.py --port COMx erase_flash
   ```
4. Flash the MicroPython firmware:
   ```bash
   esptool.py --chip esp32 --port COMx write_flash -z 0x1000 esp32-xxxxxx.bin
   ```

> Replace `COMx` with the port connected to your ESP32 and `esp32-xxxxxx.bin` with your downloaded firmware filename.

## How to Run the Code on ESP32 Using Thonny

1. Connect the ESP32 board to your computer via USB.
2. Open [Thonny IDE](https://thonny.org).
3. Set the interpreter to **MicroPython (ESP32)** via `Tools` → `Options` → `Interpreter`.
4. Choose the correct port (e.g., COMx or /dev/ttyUSBx).
5. Copy and paste the following code into Thonny.
6. Save the script as `main.py` to the device.
7. Click **Run** or press `Ctrl+R`.

## Code

```python
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led.value(not led.value())
    sleep(0.5)
```

## Sample Output

The onboard LED on the ESP32 board will blink continuously with a 0.5-second interval.

---

## License

This project is open-source and available under the MIT License.

## Contributing

Feel free to fork this repository, contribute with pull requests, or report issues. Contributions are welcome!

```bash
git clone https://github.com/AbisheckD/Python_in_ESP32.git
```
