#!/usr/bin/env python
"""
Maak een teller. Je hebt een drukknop die optelt en één die naar beneden telt.
"""


from gpiozero import Button
import time
import msvcrt

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"

# IP = '192.168.0.204'
# button1 = Button(pin=4, pin_factory=IP)
# button2 = Button(pin=5, pin_factory=IP)
counter = 0

def main():
    print("H om op te tellen, L om af te tellen")
    while True:
        a = int(input('H om op te tellen, L om af te tellen'))
        if a == 'H':
            counter.__add__(1)
            print(counter)
        if a == 'L':
            counter.__sub__(1)
            print(counter)





main()
