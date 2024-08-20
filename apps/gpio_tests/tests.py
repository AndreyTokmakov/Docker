import RPi.GPIO as GPIO
import time


def test():
    ledPin = 21

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPin, GPIO.OUT)

    GPIO.output(ledPin, GPIO.HIGHT)
    time.sleep(5)
    GPIO.output(ledPin, GPIO.LOW)


def info():
    print(GPIO.VERSION)
    print(GPIO.RPI_INFO)


if __name__ == '__main__':
    # info()
    test()



# https://medium.com/geekculture/gpio-programming-on-the-raspberry-pi-python-libraries-e12af7e0a812

# https://www.raspberrypi.com/documentation/computers/raspberry-pi.html