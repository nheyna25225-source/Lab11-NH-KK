# https://github.com/nheyna25225-source/Lab11-NH-KK
# Partner 1: Nicholas Heyna
# Partner 2: Kaden King

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("invalid values for logarithm")
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("invalid values for logarithm")
    return math.log(b, a)

def exp(a, b):
    return a ** b

import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Log base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Log argument must be positive")
    return math.log(b, a)

def exponent(a, b):
    return a ** b




