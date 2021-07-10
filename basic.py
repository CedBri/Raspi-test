from gpiozero import LED
from time import sleep

led = LED(12)

while True:
    setting = input("Enter on/off value: ")
    print(setting)
    if setting.lower() == "on":
        led.on()
    else:
        led.off()
