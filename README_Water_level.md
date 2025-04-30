# ESP32 with Water Level Sensor using MicroPython

## Overview

This project demonstrates how to read water level values from a water level sensor connected to an ESP32 board using MicroPython. The readings are printed on the serial console via Thonny IDE.

## GitHub Repository

- [GitHub Repository](https://github.com/AbisheckD/Python_in_ESP32/tree/main)

## Prerequisites

- ESP32 Development Board  
- Water Level Sensor  
- Python installed on your computer

  ## Useful Links

- 🔧 **MicroPython Firmware for ESP32**: [Download](https://micropython.org/download/ESP32_GENERIC/)
- 🧪 **Getting Started Tutorial with Thonny**: [TechToTinker Guide](https://techtotinker.com/2020/09/05/000-esp32-micropython-how-to-get-started-with-micropython/)
- 🛠 **Thonny IDE**: [https://thonny.org](https://thonny.org)
- 🔌 **USB Driver (CP210x)**: [Download VCP Driver](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers)

## Wiring

| Sensor Pin     | ESP32 Pin  |
|----------------|------------|
| VCC            | 3.3V       |
| GND            | GND        |
| Analog Output  | GPIO36 (ADC1_CH0) |

> ⚠️ Use an ADC-capable pin. GPIO36 is commonly used and stable for analog reads.
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

1. Open Thonny.
2. Go to `Tools` > `Options` > `Interpreter`.
3. Select **MicroPython (ESP32)** and choose the correct COM port.
4. Click OK to save.

## Water Level Sensor Code (MicroPython)

```python
from machine import ADC, Pin
from time import sleep

adc = ADC(Pin(36))  # GPIO36 (ADC1_CH0)
adc.atten(ADC.ATTN_11DB)  # Full range: 0-3.3V
adc.width(ADC.WIDTH_10BIT)

while True:
    level = adc.read()  # Returns a value between 0 and 1023 (10-bit)
    print("Water Level Reading:", level)
    sleep(1)
```

## Output

The terminal in Thonny will display the following:

```
Water Level Reading: 1024
Water Level Reading: 1500
Water Level Reading: 3000
```

## Calibration Tip

If needed, you can map the 0–1023 range to real-world water level (in cm or %) based on your tank's size and sensor position.

## License

MIT License

## Clone the Repo

```bash
git clone https://github.com/AbisheckD/Python_in_ESP32.git
```

