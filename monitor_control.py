from RPLCD import CharLCD
import RPi.GPIO as GPIO
from paramiko import SSHClient, AutoAddPolicy, RSAKey
from time import sleep
import sys

# Setup the GPIO

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


def write_lcd(status):

    lcd.clear()

    if status:
        lcd.write_string("Monitor is on!")
    elif not status:
        lcd.write_string("Monitor is off!")
    else:
        lcd.write_string("Error!")


def check_status(ssh, command):

    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.readlines()

    if "  Monitor is On\n" in lines:
        write_lcd(True)
        return "On"
    else:
        write_lcd(False)
        return "Off"


def main():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)

    host = "192.168.0.25"
    username = "lerusse"
    id_rsa = RSAKey.from_private_key_file("/home/pi/.ssh/id_rsa")

    command = "xset -display :0.0 q"

    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(host, 22, username, pkey=id_rsa)
    while True:
        try:
            sleep(1)
            check_status(ssh, command)
        except KeyboardInterrupt:
            sys.exit()


if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    # except Exception as e:
    # print(e)
    finally:
        GPIO.cleanup()
