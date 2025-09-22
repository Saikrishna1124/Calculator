import math

def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error: Cannot divide by zero."
        result /= num
    return result

def power(base, exponent):
    return base ** exponent

def square_root(number):
    if number < 0:
        return "Error: Cannot take square root of negative number."
    return math.sqrt(number)

def modulo(a, b):
    if b == 0:
        return "Error: Cannot modulo by zero."
    return a % b

def factorial(n):
    if n < 0 or int(n) != n:
        return "Error: Factorial only defined for non-negative integers."
    return math.factorial(int(n))
