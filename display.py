from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time

# RS -> P26
# ENABLE -> P19
# LCD D4 -> P13
# LCD D5 -> P06
# LCD D6 -> P05
# LCD D7 -> P22

LCD_RS = 26
ENABLE = 19
LCD_D4 = 13
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 22

LCD_WIDTH = 16
LCD_HEIGHT = 2

GPIO.cleanup()

lcd = CharLCD(
    cols=LCD_WIDTH,
    rows=LCD_HEIGHT,
    pin_rs=LCD_RS,
    pin_e=ENABLE,
    pins_data=[LCD_D4, LCD_D5, LCD_D6, LCD_D7],
    numbering_mode=GPIO.BCM,
)
while True:

    lcd.write_string("Time: %s" % time.strftime("%H:%M:%S"))
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Date: %s" % time.strftime("%d/%m/%Y"))
