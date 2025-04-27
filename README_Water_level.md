# ESP32 Water Level Sensor using MicroPython (10-bit ADC)

## Overview

This project reads water level data from an analog water level sensor connected to an ESP32 board using MicroPython. The ADC is configured for 10-bit resolution (0–1023), making the readings more compact and suitable for basic level detection.

## GitHub Repository

- GitHub Repo: [Python_in_ESP32](https://github.com/AbisheckD/Python_in_ESP32/tree/main)

## Prerequisites

- ESP32 Devkit Board  
- Analog Water Level Sensor  
- MicroPython flashed to ESP32  
- USB to UART bridge driver ([Silicon Labs CP210x VCP](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers))  
- [Thonny IDE](https://thonny.org/) for uploading and running code

## Wiring

| Sensor Pin     | ESP32 Pin  |
|----------------|------------|
| VCC            | 3.3V       |
| GND            | GND        |
| Analog Output  | GPIO36 (ADC1_CH0) |

> ⚠️ Use an ADC-capable pin. GPIO36 is commonly used and stable for analog reads.

## Useful Links

- 🔧 **MicroPython Firmware for ESP32**: [Download](https://micropython.org/download/ESP32_GENERIC/)
- 🧪 **Getting Started Tutorial with Thonny**: [TechToTinker Guide](https://techtotinker.com/2020/09/05/000-esp32-micropython-how-to-get-started-with-micropython/)
- 🛠 **Thonny IDE**: [https://thonny.org](https://thonny.org)
- 🔌 **USB Driver (CP210x)**: [Download VCP Driver](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers)

## Instructions

1. Flash MicroPython firmware on the ESP32 board if not already done.
2. Open Thonny IDE and set the interpreter to **MicroPython (ESP32)**.
3. Connect the sensor as per the wiring guide above.
4. Copy and upload the code below to your ESP32 as `main.py`.

## Code

```python
from machine import ADC, Pin
from time import sleep

adc = ADC(Pin(36))  # GPIO36 (ADC1_CH0)
adc.atten(ADC.ATTN_11DB)  # 0-3.3V range
adc.width(ADC.WIDTH_10BIT)  # 10-bit resolution: 0–1023

while True:
    level = adc.read()  # Returns a value between 0 and 1023
    print("Water Level Reading:", level)
    sleep(1)
```

## Output Sample

```
Water Level Reading: 428
Water Level Reading: 493
Water Level Reading: 515
...
```

## Calibration Tip

If needed, you can map the 0–1023 range to real-world water level (in cm or %) based on your tank's size and sensor position.

## License

This project is under the MIT License.

## Contributing

Contributions are welcome! Clone the repo and submit a pull request.

```bash
git clone https://github.com/AbisheckD/Python_in_ESP32.git
```

