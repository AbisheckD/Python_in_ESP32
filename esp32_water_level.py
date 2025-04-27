from machine import ADC, Pin
from time import sleep

adc = ADC(Pin(36))  # GPIO36 (ADC1_CH0)
adc.atten(ADC.ATTN_11DB)  # Full range: 0-3.3V
adc.width(ADC.WIDTH_10BIT)

while True:
    level = adc.read()  # Returns a value between 0 and 4095
    print("Water Level Reading:", level)
    sleep(1)
