import RPi.GPIO as GPIO
from RPLCD import CharLCD
import time

# GPIO mode
GPIO.setmode(GPIO.BCM)

# Set pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24
LCD_RS = 26
ENABLE = 19
LCD_D4 = 13
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 22
LCD_WIDTH = 16
LCD_HEIGHT = 2

lcd = CharLCD(
    cols=LCD_WIDTH,
    rows=LCD_HEIGHT,
    pin_rs=LCD_RS,
    pin_e=ENABLE,
    pins_data=[LCD_D4, LCD_D5, LCD_D6, LCD_D7],
    numbering_mode=GPIO.BCM,
)
# set GPIO direction
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def write_distance(distance):
    lcd.clear()

    lcd.write_string("Distance: %.1fcm" % distance)


def get_distance():
    # Trigger
    GPIO.output(GPIO_TRIGGER, True)

    # Set low after 0.01ms
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save Start time
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save arrival time
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # calc time delta
    elapsed = StopTime - StartTime
    # mult by sonic speed
    distance = (elapsed * 34300) / 2

    return distance


def main():
    try:
        while True:
            dist = get_distance()
            write_distance(dist)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        GPIO.cleanup()


if __name__ == "__main__":
    main()
