#!/usr/bin/env python
"""
Maak een teller. Je hebt een drukknop die optelt en één die naar beneden telt.
"""


from gpiozero import Button
import time

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"

IP = '192.168.0.204'
button1 = Button(pin=4, pin_factory=IP)
button2 = Button(pin=5, pin_factory=IP)
counter = 0

def main():
    button1.when_released(counter.__add__(1))
    button2.when_released(counter.__sub__(1))


if __name__ == '__main__':  # code to execute if called from command-line
    main()
