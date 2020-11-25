#!/usr/bin/env python
"""
Print twee variabelen uit die optellen. De eerste variabele telt op elke seconde, de tweede elke twee seconden.
"""
import multiprocessing
import time

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"




def Tel_een_op():
    x = 0
    while True:
        time.sleep(1)
        print(x)
        x += 1

def Tel_twee_op():
    y = 0
    while True:
        time.sleep(2)
        print(y)
        y += 1


if __name__ == '__main__':  # code to execute if called from command-line
    x1 = multiprocessing.Process(target=Tel_een_op)
    x2 = multiprocessing.Process(target=Tel_twee_op)
    x1.start()
    x2.start()
