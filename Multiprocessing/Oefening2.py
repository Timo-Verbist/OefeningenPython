#!/usr/bin/env python
"""
Programmeer 3 drukknoppen. Elke drukknop stuurt een LED aan. De LED blijft 5 seconden aan en gaat dan uit.
"""

# IMPORT
import multiprocessing
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Button
from gpiozero import LED
import time

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"


IP = PiGPIOFactory('192.168.0.204')
BUTTON_one = Button(pin=4, pin_factory=IP)
BUTTON_two = Button(pin=5, pin_factory=IP)
BUTTON_three = Button(pin=6, pin_factory=IP)
LED_one = LED(pin=16, pin_factory=IP)
LED_two = LED(pin=17, pin_factory=IP)
LED_three = LED(pin=18, pin_factory=IP)

def Press_led_one():
    if BUTTON_one.is_pressed:
        LED_one.on()
        time.sleep(5)

def Press_led_two():
    if BUTTON_two.is_pressed:
        LED_two.on()
        time.sleep(5)

def Press_led_three():
    if BUTTON_three.is_pressed:
        LED_three.on()
        time.sleep(5)



if __name__ == '__main__':  # code to execute if called from command-line
    x1 = multiprocessing.Process(target=Press_led_one)
    x2 = multiprocessing.Process(target=Press_led_two)
    x3 = multiprocessing.Process(target=Press_led_three)
    x1.start()
    x2.start()
    x3.start()

