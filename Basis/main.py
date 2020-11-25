#!/usr/bin/env python
"""
Je laat een LED aangaan, na 5 seconden schakelt deze LED terug uit. Na 2 seconden gaat deze terug aan, na 2 seconden
ook weer uit. Dit herhaal je 5 keer waarna de led in een blink toestand blijft (1 sec aan, 1 sec uit).
"""

from gpiozero import LED
import time

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"

IP = '192.168.0.204'
led = LED(pin=17, pin_factory=IP)


def main():
    for i in range(5):
        print(i)
        led.on()
        time.sleep(5)
        led.off()
        time.sleep(2)
        led.on()
        time.sleep(2)
        led.off()
        time.sleep(2)
    while True:
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
