#!/usr/bin/env python
"""
Maak een teller. Je hebt een drukknop die optelt en één die naar beneden telt.
"""

# IMPORTS
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"

# I/O CONFIG
IP = PiGPIOFactory('192.168.0.204')
BUTTON_UP = Button(pin=4, pin_factory=IP)
BUTTON_DOWN = Button(pin=5, pin_factory=IP)
BUTTON_RESET = Button(pin=6, pin_factory=IP)


def main():
    while True:
        counter = 0
        if BUTTON_UP.is_pressed:
            counter += 1
            print(counter)
        elif BUTTON_DOWN.is_pressed:
            counter -= 1
            print(counter)
        elif BUTTON_RESET.is_pressed:
            counter = 0
            print(counter)
        else:
            print(counter)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
