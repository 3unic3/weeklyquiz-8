import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def square(x):
    return x * x

def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(x)

def logarithm(value, base=10):
    if value <= 0:
        raise ValueError("Logarithm input must be positive")
    if base <= 0:
        raise ValueError("Logarithm base must be positive")
    if base == 1:
        raise ValueError("Logarithm base cannot be 1")
    return math.log(value, base)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def percentage(value, percent):
    return value * percent / 100
